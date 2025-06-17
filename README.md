# IBS Reticulotype Project

This repository contains a minimal research environment for experimenting with reinforcement learning approaches to irritable bowel syndrome (IBS). The provided code defines a small Gym environment that simulates a patient and a training script using `stable-baselines3`.

## Setup

Install dependencies (may take a few minutes):

```bash
pip install -r requirements.txt
```

## Training

To train the PPO agent on the synthetic patient data run:

```bash
python IBS_Reticulotype_Project/core/train_rl_agent.py
```

The trained model will be saved as `ppo_ibs.zip`.
