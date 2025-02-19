import os
import gymnasium

from ppo import PPO

if not os.path.exists("train_model"):
    os.makedirs("train_model")

env = gymnasium.make("MountainCarContinuous-v0", render_mode="rgb_array")
model = PPO("MlpPolicy", env, verbose=1, n_steps=400, n_steps_episode=400, n_epochs=30, device="cuda", seed=60)
# model = PPO("MlpPolicy", env, verbose=1, n_steps=400, n_steps_episode=400, n_epochs=30, device="cuda", seed=73)
# model = PPO("MlpPolicy", env, verbose=1, n_steps=400, n_steps_episode=400, n_epochs=30, device="cuda", seed=308)
# model = PPO("MlpPolicy", env, verbose=1, n_steps=400, n_steps_episode=400, n_epochs=30, device="cuda", seed=319)
# model = PPO("MlpPolicy", env, verbose=1, n_steps=400, n_steps_episode=400, n_epochs=30, device="cuda", seed=358)
# model = PPO("MlpPolicy", env, verbose=1, n_steps=400, n_steps_episode=400, n_epochs=30, device="cuda", seed=422)
# model = PPO("MlpPolicy", env, verbose=1, n_steps=400, n_steps_episode=400, n_epochs=30, device="cuda", seed=437)

_, state_orbit, action_orbit, reward_iteration, max_position_iteration, F_nn, F_unknown, W_iteration, Num, W_learned, iteration = model.learn7(total_timesteps=20000)






































