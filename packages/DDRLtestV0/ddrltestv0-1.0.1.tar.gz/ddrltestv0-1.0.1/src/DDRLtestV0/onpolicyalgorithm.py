import sys
import time
import warnings
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar, Union

import numpy as np
import torch as th
from gymnasium import spaces
import math
import copy

from stable_baselines3.common.base_class import BaseAlgorithm
from stable_baselines3.common.buffers import DictRolloutBuffer, RolloutBuffer
from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3.common.policies import ActorCriticPolicy
from stable_baselines3.common.type_aliases import GymEnv, MaybeCallback, Schedule
from stable_baselines3.common.utils import obs_as_tensor, safe_mean
from stable_baselines3.common.vec_env import VecEnv

from typing import Optional
from gymnasium.envs.classic_control import utils

SelfOnPolicyAlgorithm = TypeVar("SelfOnPolicyAlgorithm", bound="OnPolicyAlgorithm")


class OnPolicyAlgorithm(BaseAlgorithm):
    """
    The base for On-Policy algorithms (ex: A2C/PPO).

    :param policy: The policy model to use (MlpPolicy, CnnPolicy, ...)
    :param env: The environment to learn from (if registered in Gym, can be str)
    :param learning_rate: The learning rate, it can be a function
        of the current progress remaining (from 1 to 0)
    :param n_steps: The number of steps to run for each environment per update
        (i.e. batch size is n_steps * n_env where n_env is number of environment copies running in parallel)
    :param gamma: Discount factor
    :param gae_lambda: Factor for trade-off of bias vs variance for Generalized Advantage Estimator.
        Equivalent to classic advantage when set to 1.
    :param ent_coef: Entropy coefficient for the loss calculation
    :param vf_coef: Value function coefficient for the loss calculation
    :param max_grad_norm: The maximum value for the gradient clipping
    :param use_sde: Whether to use generalized State Dependent Exploration (gSDE)
        instead of action noise exploration (default: False)
    :param sde_sample_freq: Sample a new noise matrix every n steps when using gSDE
        Default: -1 (only sample at the beginning of the rollout)
    :param rollout_buffer_class: Rollout buffer class to use. If ``None``, it will be automatically selected.
    :param rollout_buffer_kwargs: Keyword arguments to pass to the rollout buffer on creation.
    :param stats_window_size: Window size for the rollout logging, specifying the number of episodes to average
        the reported success rate, mean episode length, and mean reward over
    :param tensorboard_log: the log location for tensorboard (if None, no logging)
    :param monitor_wrapper: When creating an environment, whether to wrap it
        or not in a Monitor wrapper.
    :param policy_kwargs: additional arguments to be passed to the policy on creation
    :param verbose: Verbosity level: 0 for no output, 1 for info messages (such as device or wrappers used), 2 for
        debug messages
    :param seed: Seed for the pseudo random generators
    :param device: Device (cpu, cuda, ...) on which the code should be run.
        Setting it to auto, the code will be run on the GPU if possible.
    :param _init_setup_model: Whether or not to build the network at the creation of the instance
    :param supported_action_spaces: The action spaces supported by the algorithm.
    """

    rollout_buffer: RolloutBuffer  ## for episode collect
    # rollout_buffer2: RolloutBuffer ## for deterministic learning

    policy: ActorCriticPolicy

    def __init__(
            self,
            policy: Union[str, Type[ActorCriticPolicy]],
            env: Union[GymEnv, str],
            learning_rate: Union[float, Schedule],
            n_steps: int,
            n_steps_episode: int,
            gamma: float,
            gae_lambda: float,
            ent_coef: float,
            vf_coef: float,
            max_grad_norm: float,
            use_sde: bool,
            sde_sample_freq: int,
            rollout_buffer_class: Optional[Type[RolloutBuffer]] = None,
            rollout_buffer_kwargs: Optional[Dict[str, Any]] = None,
            stats_window_size: int = 100,
            tensorboard_log: Optional[str] = None,
            monitor_wrapper: bool = True,
            policy_kwargs: Optional[Dict[str, Any]] = None,
            verbose: int = 0,
            seed: Optional[int] = None,
            device: Union[th.device, str] = "auto",
            _init_setup_model: bool = True,
            supported_action_spaces: Optional[Tuple[Type[spaces.Space], ...]] = None,
    ):
        super().__init__(
            policy=policy,
            env=env,
            learning_rate=learning_rate,
            policy_kwargs=policy_kwargs,
            verbose=verbose,
            device=device,
            use_sde=use_sde,
            sde_sample_freq=sde_sample_freq,
            support_multi_env=True,
            monitor_wrapper=monitor_wrapper,
            seed=seed,
            stats_window_size=stats_window_size,
            tensorboard_log=tensorboard_log,
            supported_action_spaces=supported_action_spaces,
        )

        self.n_steps = n_steps
        self.n_steps_episode = n_steps_episode
        self.gamma = gamma
        self.gae_lambda = gae_lambda
        self.ent_coef = ent_coef
        self.vf_coef = vf_coef
        self.max_grad_norm = max_grad_norm
        self.rollout_buffer_class = rollout_buffer_class
        self.rollout_buffer_kwargs = rollout_buffer_kwargs or {}

        self.min_value = None,
        self.average_rewards = None,
        ### 以上是sb3自带的变量

        ### 以下6个是自定义的变量
        self.last_values = None,
        self.dones = None,
        self.W_last_learned = None,  ##初始化一个权值属性
        self.central = None,
        self.is_terminated = False
        self.action_prev = None

        if _init_setup_model:
            self._setup_model()

    ### 以下4个是自定义的函数
    def update_W(self, W):
        self.W_last_learned = W

    def update_W2(self, W2):
        self.W_last_learned2 = W2

    def update_Cent(self, cent):
        self.central = cent

    def update_Cent2(self, cent2):
        self.central2 = cent2

    def _setup_model(self) -> None:
        self._setup_lr_schedule()
        self.set_random_seed(self.seed)

        if self.rollout_buffer_class is None:
            if isinstance(self.observation_space, spaces.Dict):
                self.rollout_buffer_class = DictRolloutBuffer
            else:
                self.rollout_buffer_class = RolloutBuffer

        self.rollout_buffer = self.rollout_buffer_class(
            self.n_steps,
            self.observation_space,  # type: ignore[arg-type]
            self.action_space,
            device=self.device,
            gamma=self.gamma,
            gae_lambda=self.gae_lambda,
            n_envs=self.n_envs,
            **self.rollout_buffer_kwargs,
        )
        self.policy = self.policy_class(  # type: ignore[assignment]
            self.observation_space, self.action_space, self.lr_schedule, use_sde=self.use_sde, **self.policy_kwargs
        )
        self.policy = self.policy.to(self.device)
        # Warn when not using CPU with MlpPolicy
        self._maybe_recommend_cpu()

    def _maybe_recommend_cpu(self, mlp_class_name: str = "ActorCriticPolicy") -> None:
        """
        Recommend to use CPU only when using A2C/PPO with MlpPolicy.

        :param: The name of the class for the default MlpPolicy.
        """
        policy_class_name = self.policy_class.__name__
        if self.device != th.device("cpu") and policy_class_name == mlp_class_name:
            warnings.warn(
                f"You are trying to run {self.__class__.__name__} on the GPU, "
                "but it is primarily intended to run on the CPU when not using a CNN policy "
                f"(you are using {policy_class_name} which should be a MlpPolicy). "
                "See https://github.com/DLR-RM/stable-baselines3/issues/1245 "
                "for more info. "
                "You can pass `device='cpu'` or `export CUDA_VISIBLE_DEVICES=` to force using the CPU."
                "Note: The model will train, but the GPU utilization will be poor and "
                "the training might take longer than on CPU.",
                UserWarning,
            )

    ### 收集训练数据，为训练动力学模型，较sb3源代码略有改动。此处只收集数据，不涉及动力学模型训练
    def collect_rollouts(
            self,
            env: VecEnv,
            callback: BaseCallback,
            rollout_buffer: RolloutBuffer,
            n_rollout_steps: int,
    ) -> bool:
        """
        Collect experiences using the current policy and fill a ``RolloutBuffer``.
        The term rollout here refers to the model-free notion and should not
        be used with the concept of rollout used in model-based RL or planning.

        :param env: The training environment
        :param callback: Callback that will be called at each step
            (and at the beginning and end of the rollout)
        :param rollout_buffer: Buffer to fill with rollouts
        :param n_rollout_steps: Number of experiences to collect per environment
        :return: True if function returned with at least `n_rollout_steps`
            collected, False if callback terminated rollout prematurely.
        """
        assert self._last_obs is not None, "No previous observation was provided"
        self.policy.set_training_mode(False)

        n_step = 0
        rollout_buffer.reset()
        # Sample new weights for the state dependent exploration
        if self.use_sde:
            self.policy.reset_noise(env.num_envs)

        callback.on_rollout_start()

        while n_step < n_rollout_steps:
            if self.use_sde and self.sde_sample_freq > 0 and n_step % self.sde_sample_freq == 0:
                # Sample a new noise matrix
                self.policy.reset_noise(env.num_envs)

            with th.no_grad():
                # Convert to pytorch tensor or to TensorDict
                obs_tensor = obs_as_tensor(self._last_obs, self.device)
                if n_step % 50 == 0:
                    actions, values, log_probs = self.policy(obs_tensor)
                    pre_action = copy.deepcopy(actions)
                else:
                    _, values, log_probs = self.policy(obs_tensor)
                    actions = pre_action
            actions = actions.cpu().numpy()

            clipped_actions = np.clip(actions, self.min_action, self.max_action)    ###
            clipped_actions = np.clip(actions, self.action_space.low, self.action_space.high)
            new_obs, rewards, dones, infos = env.step(clipped_actions)

            if dones:
                self.is_terminated = True

            self.num_timesteps += env.num_envs

            # Give access to local variables
            callback.update_locals(locals())
            if not callback.on_step():
                return False

            self._update_info_buffer(infos, dones)
            n_step += 1

            if isinstance(self.action_space, spaces.Discrete):
                # Reshape in case of discrete action
                actions = actions.reshape(-1, 1)

            # Handle timeout by bootstrapping with value function
            # see GitHub issue #633
            for idx, done in enumerate(dones):
                if (
                        done
                        and infos[idx].get("terminal_observation") is not None
                        and infos[idx].get("TimeLimit.truncated", False)
                ):
                    terminal_obs = self.policy.obs_to_tensor(infos[idx]["terminal_observation"])[0]
                    with th.no_grad():
                        terminal_value = self.policy.predict_values(terminal_obs)[0]  # type: ignore[arg-type]
                    rewards[idx] += self.gamma * terminal_value

            rollout_buffer.add(
                self._last_obs,  # type: ignore[arg-type]
                actions,
                rewards,
                self._last_episode_starts,  # type: ignore[arg-type]
                values,
                log_probs,
            )
            self._last_obs = new_obs  # type: ignore[assignment]
            self._last_episode_starts = dones

        with th.no_grad():
            # Compute value for the last timestep
            values = self.policy.predict_values(obs_as_tensor(new_obs, self.device))  # type: ignore[arg-type]

        self.last_values = copy.deepcopy(values)
        self.dones = copy.deepcopy(dones)
        rollout_buffer.compute_returns_and_advantage(last_values=values, dones=dones)

        callback.update_locals(locals())

        callback.on_rollout_end()

        return True

    def train(self) -> None:
        """
        Consume current rollout data and update policy parameters.
        Implemented by individual algorithms.
        """
        raise NotImplementedError

    def _dump_logs(self, iteration: int) -> None:
        """
        Write log.

        :param iteration: Current logging iteration
        """
        assert self.ep_info_buffer is not None
        assert self.ep_success_buffer is not None

        time_elapsed = max((time.time_ns() - self.start_time) / 1e9, sys.float_info.epsilon)
        fps = int((self.num_timesteps - self._num_timesteps_at_start) / time_elapsed)
        self.logger.record("time/iterations", iteration, exclude="tensorboard")
        if len(self.ep_info_buffer) > 0 and len(self.ep_info_buffer[0]) > 0:
            self.logger.record("rollout/ep_rew_mean",
                               safe_mean([ep_info["r"] for ep_info in self.ep_info_buffer]))  ## average reward
            self.average_rewards = safe_mean([ep_info["r"] for ep_info in self.ep_info_buffer])
            self.logger.record("rollout/ep_len_mean", safe_mean([ep_info["l"] for ep_info in self.ep_info_buffer]))
            self.logger.record("rollout/ep_rew_curr", self.ep_info_buffer[-1]["r"])     #####
        self.logger.record("time/fps", fps)
        self.logger.record("time/time_elapsed", int(time_elapsed), exclude="tensorboard")
        self.logger.record("time/total_timesteps", self.num_timesteps, exclude="tensorboard")
        if len(self.ep_success_buffer) > 0:
            self.logger.record("rollout/success_rate", safe_mean(self.ep_success_buffer))
        # self.logger.record("train/entropy_loss", np.mean(entropy_losses))
        self.logger.dump(step=self.num_timesteps)

    ### sb3原本的训练代码。其中只包含策略训练，不包含动力学训练
    def learn(
            self: SelfOnPolicyAlgorithm,
            total_timesteps: int,
            callback: MaybeCallback = None,
            log_interval: int = 1,
            tb_log_name: str = "OnPolicyAlgorithm",
            reset_num_timesteps: bool = True,
            progress_bar: bool = False,
    ) -> SelfOnPolicyAlgorithm:
        iteration = 0

        total_timesteps, callback = self._setup_learn(
            total_timesteps,
            callback,
            reset_num_timesteps,
            tb_log_name,
            progress_bar,
        )

        callback.on_training_start(locals(), globals())

        assert self.env is not None

        while self.num_timesteps < total_timesteps:
            continue_training = self.collect_rollouts(self.env, callback, self.rollout_buffer,
                                                      n_rollout_steps=self.n_steps)

            if not continue_training:
                break

            iteration += 1
            self._update_current_progress_remaining(self.num_timesteps, total_timesteps)

            # Display training infos
            if log_interval is not None and iteration % log_interval == 0:
                assert self.ep_info_buffer is not None
                self._dump_logs(iteration)

            self.train()

        callback.on_training_end()

        return self

    ### 改进sb3的训练代码。添加了含动力学训练部分
    def learn7(
            self: SelfOnPolicyAlgorithm,
            total_timesteps: int,
            callback: MaybeCallback = None,
            log_interval: int = 1,
            tb_log_name: str = "OnPolicyAlgorithm",
            reset_num_timesteps: bool = True,
            progress_bar: bool = False,
    ) -> SelfOnPolicyAlgorithm:
        iteration = 0

        total_timesteps, callback = self._setup_learn(
            total_timesteps,
            callback,
            reset_num_timesteps,
            tb_log_name,
            progress_bar,
        )

        callback.on_training_start(locals(), globals())

        assert self.env is not None

        ##--------------------RBF神经网络布点，此时的环境动力学模型的输入有三个分别是 position，velocity，force--------------------------------------#
        e1 = np.arange(-1.2, 0.6, 0.6)  ##position    参照官方文档
        # e2=np.arange(-0.07 , 0.07 , 0.07)        ##velocity
        e3 = np.arange(-1, 1, 0.5)  ##force

        len_e1 = len(e1)
        # len_e2=len(e2)
        len_e3 = len(e3)
        Cent_matrix = []

        for i1 in range(len_e1):
            for i3 in range(len_e3):
                Cent = [e1[i1], e3[i3]]
                Cent_matrix.append(Cent)
        ##取神经元向量 element=Cent_matrix[i][j]   每一行是一个神经元
        self.update_Cent(Cent_matrix)

        [Num, Dimension] = np.shape(Cent_matrix)  ## Num为神经元的个数, Dimension为状态维数

        # ----------------------------------------------------------------------------------------------------------------------------------#

        # -----------------------------参数初始化-----------------------------------------------------------------------------------------------
        eta1 = 0.6 * 1.25  # RBF 神经网络感受野
        eta2 = 0.07 * 1.25
        eta3 = 0.5 * 1.25

        Ts = 0.02  # 采样间隔 0.02s
        gamma = 6  # RBF学习律
        sigma = 0.00  # RBF偏置参数
        alpha = 0.3  # 动态估计器系数

        total_timesteps = total_timesteps
        n_steps = 8000  # 确定学习需要的步长

        min_action = -1
        max_action = 1
        goal_position = 0.45

        estimation = np.zeros(n_steps + 1)  ## 动态估计器初始值 velocity 维度

        W_estimation = np.zeros([Num, n_steps + 1])  # RBF网络权值初始值
        S_regression = np.zeros([Num, n_steps + 1])  # 存放每次迭代的S值

        W_learned = []  ##定义一个空矩阵
        W_not_need = []
        W_need = []
        average_window = 10  ##计算残差的平均窗口长度

        self.min_value = -0.3  ##限定一个任务级轨迹范围

        self.min_action = -1
        self.max_action = 1

        print("total_timesteps:", total_timesteps)
        # -------------------------------------------------------------------------------------------------------

        ##---------------------------用于存放轨迹---------------------------------------------------------
        state_orbit = np.empty((0, 2), dtype=float)  # 初始形状为 (0, 2)，表示没有行但有 2 列
        action_orbit = np.empty((0, 1), dtype=float)
        reward_iteration = np.empty((0, 1), dtype=float)
        average_episode_reward = np.empty((0, 1), dtype=float)
        max_position_iteration = np.empty((0, 1), dtype=float)
        W_iteration = []  ##用于存放迭代步骤中的 W_estimation
        W_iteration2 = []  ##用于存放逆向模型的权值
        F_unknown = []  ##用于存放迭代步骤 中的 f
        F_nn = []  ##用于存放迭代步骤中的 f_nn

        model_numbers = 0

        ##------------------------------------------------------------------------------------------------

        while self.num_timesteps < total_timesteps:

            self.is_terminated = False
            continue_training = self.collect_rollouts(self.env, callback, self.rollout_buffer,
                                                      n_rollout_steps=self.n_steps_episode)

            observations = copy.deepcopy(np.squeeze(self.rollout_buffer.observations, axis=1))  ## (10, 1, 2) -> (10, 2)
            actions = copy.deepcopy(np.squeeze(self.rollout_buffer.actions, axis=1))  ## (10, 1, 1) -> (10, 1)
            rewards = copy.deepcopy(self.rollout_buffer.rewards)  ##  (10, 1)

            car_position = observations[:, 0]  ##  (10, )

            force = np.zeros([len(actions), 1])
            for i in range(len(actions)):
                force[i] = min(max(actions[i], min_action), max_action)

            ##存储每次迭代的数据
            state_orbit = np.vstack([observations] * 20)
            action_orbit = np.vstack([force] * 20)
            max_position_iteration = np.vstack([max_position_iteration, [np.max(car_position)]])  ##当前迭代最大位置

            print("max_pos:", np.max(car_position))  ##本轮迭代的最大位置
            print("self.min_value:", self.min_value)

            if self.is_terminated:
                task_orbit_flag = 1
            else:
                task_orbit_flag = 0

            if np.max(car_position) > 0.43:
                self.min_value = 0.43
            elif np.max(car_position) > self.min_value:
                self.min_value = np.max(car_position)

            if True:

                ##-------------------------------------------前向动力学的RBF神经网络回归向量------------------------------------------#
                for j in range(n_steps - 1):
                    position = state_orbit[j][0]  # x1 = position
                    velocity = state_orbit[j][1]  # x2 = velocity
                    # action = actions[j]
                    force1 = action_orbit[j]  ## uk

                    ##next state
                    next_velocity = state_orbit[j + 1][1]  # x2(j+1)
                    # RBF神经网络的回归向量  只有两个维度 position 和 action (Force)

                    ## 前向动力学函数
                    Z_input = [position, force1]
                    S_input = np.zeros((Num, 1))

                    for index in np.arange(0, Num):
                        S_input[index] = np.exp(-((Z_input[0] - Cent_matrix[index][0])) ** 2 / (eta1 ** 2) - (
                            (Z_input[1] - Cent_matrix[index][1])) ** 2 / (eta3 ** 2))

                    # ------------------------------------------对当前轨迹进行环境建模(Forward)--------------------------------------------------------------------#

                    # 构建RBF神经网络辨识器

                    estimation[j + 1] = velocity + alpha * (estimation[j] - velocity) + Ts * np.dot(
                        np.transpose(W_estimation[:, j]), S_input)
                    estimation_error = estimation[j + 1] - next_velocity

                    S_vector = S_input.reshape(Num)  ##变成一维矩阵 array
                    ##环境模型辨识器神经网络更新率
                    W_estimation[:, j + 1] = W_estimation[:, j] - Ts * (
                            gamma * S_vector * estimation_error + sigma * W_estimation[:, j])  ## 更新率的正负号 list 不能直接乘一个数   array 可以
                    S_regression[:, j] = S_vector  ##保存每步的回归向量S
                # -------------------------------------------------------------------------------------------------------------------------------------------#

                ##------------------------------------------保存学到的RBF神经网络权值 正向a动力学模型的权值-------------------------------------------------------------------------------#
                if task_orbit_flag == 0:
                    W_not_need.append(np.transpose(np.mean(W_estimation[:, -100:], axis=1)))
                if task_orbit_flag == 1:
                    W_need.append(np.transpose(np.mean(W_estimation[:, -100:], axis=1)))
                W_learned.append(np.transpose(np.mean(W_estimation[:, -100:], axis=1)))  ##  动态添加行   保存所有的模型
                bar_W = copy.deepcopy(W_learned[-1])
                f_nn = Ts * np.dot(bar_W, S_regression)  ##  神经网络建模结果  得到一个一维向量（n_steps, ）
                f = 0.0015 * force.reshape(-1) - 0.0025 * np.cos(3 * np.array(car_position))  ##  默认前面是有Ts的
                F_nn.append(f_nn)
                F_unknown.append(f)
                W_iteration.append(W_estimation)

                ##-----------------------------------------------------------------end----------------------------------------------------------------------------------------------#

            if True:
                # if W_need:
                num_rows = len(W_learned)
                residual_error = np.zeros(
                    (num_rows, self.n_steps_episode + 1))  ##用于存储第i次迭代 比较前i个学到的环境模型的 n_rollout_steps 步的动力学残差
                bar_estimation = np.zeros((num_rows, self.n_steps_episode + 1))  ## 动态辨识器 velocity维度

            # -----------------------------------------利用上一步得到的建模结果，计算当前迭代的正向探索奖励----------------------------------------------#

            new_reward = np.ones([self.n_steps_episode, 1])

            if True:
                # if  W_need:
                for k in np.arange(0, num_rows):  ## k 表示利用之前任务轨迹学到的环境模型
                    for j in np.arange(0, self.n_steps_episode - 1):
                        pos = observations[j][0]
                        vel = observations[j][1]
                        nex_vel = observations[j + 1][1]
                        forc = force[j]
                        Z_forward = [pos, forc]
                        S_forward = np.zeros((Num, 1))
                        for index in np.arange(0, Num):
                            S_forward[index] = np.exp(-((Z_forward[0] - Cent_matrix[index][0])) ** 2 / (eta1 ** 2) - (
                                (Z_forward[1] - Cent_matrix[index][1])) ** 2 / (eta3 ** 2))

                        bar_estimation[k, j + 1] = vel + alpha * (bar_estimation[k, j] - vel) + Ts * np.dot(
                            W_learned[k], S_forward)
                        bar_estimation[k, j + 1] = np.clip(bar_estimation[k, j + 1], -0.07, 0.07)
                        residual_error[k, j + 1] = bar_estimation[k, j + 1] - nex_vel  ##辨识器残差

                ##计算每步的前向动力学模型探索奖励
                for q in range(self.n_steps_episode):

                    if q > average_window:
                        L2_norm_velocity = np.linalg.norm(residual_error[:, q - average_window: q], ord=2,
                                                          axis=1) / average_window

                        total_residual = np.sum(L2_norm_velocity)  ##正向动力学差异总和
                        new_reward[q] = 10 * (np.exp(total_residual) - 1)
                        # new_reward[q] = 50*np.exp(-total_residual)
                    else:
                        L2_norm_velocity = np.linalg.norm(residual_error[:, q: q + average_window], ord=2,
                                                          axis=1) / average_window

                        total_residual = np.sum(L2_norm_velocity)  ##动力学差异总和
                        new_reward[q] = 10 * (np.exp(total_residual) - 1)

                # ------------------------------------------------end----------------------------------------------------------------------------------#

                dim0 = self.rollout_buffer.observations.shape[0]

                vel_reward = 1000 * self.rollout_buffer.observations.reshape(dim0, 2)[:, 1].reshape(dim0,
                                                                                                    1)  # .reshape(-1,1)

                self.rollout_buffer.rewards += new_reward * vel_reward

                self.rollout_buffer.compute_returns_and_advantage(last_values=self.last_values,
                                                                  dones=self.dones)  ## 利用更新后的reward计算优势函数advantage
                callback.update_locals(locals())
                callback.on_rollout_end()

            # ---------------------------------------------------end-------------------------------------------------------------------------------#
            model_numbers += 1

            if not continue_training:
                break

            iteration += 1  ##这里相当于每次for循环结束 i+1
            self._update_current_progress_remaining(self.num_timesteps, total_timesteps)

            self._dump_logs(iteration)
            reward_iteration = np.vstack([reward_iteration, [self.average_rewards]])

            self.train()

        print("W_need number", len(W_need))

        callback.on_training_end()

        return self, state_orbit, action_orbit, reward_iteration, max_position_iteration, F_nn, F_unknown, W_iteration, Num, W_learned, iteration

    def _get_torch_save_params(self) -> Tuple[List[str], List[str]]:
        state_dicts = ["policy", "policy.optimizer"]

        return state_dicts, []


