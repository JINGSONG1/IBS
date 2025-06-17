import pandas as pd
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from ibs_env import IBSEnv


def main():
    df = pd.read_csv('../data/synthetic_patients.csv')
    env = make_vec_env(lambda: IBSEnv(df), n_envs=1)
    model = PPO('MlpPolicy', env, verbose=1)
    model.learn(total_timesteps=1000)
    model.save('ppo_ibs')


if __name__ == '__main__':
    main()
