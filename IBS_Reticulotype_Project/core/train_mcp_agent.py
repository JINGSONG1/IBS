from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

from mcp_env import MCPEnvironment


def main():
    env = make_vec_env(lambda: MCPEnvironment('IBS_Reticulotype_Project/data/tasks_timeseries.csv'), n_envs=1)
    model = PPO('MlpPolicy', env, verbose=1)
    model.learn(total_timesteps=10000)
    model.save('mcp_agent_model')


if __name__ == '__main__':
    main()
