# IBS Reticulotype Project

This project demonstrates a minimal reinforcement learning setup for simulating
and managing IBS patient symptoms. The repository contains a simple Gym-based
environment, a PPO agent implementation, evaluation utilities and a FastAPI
service.

## Structure

- `core/` – environment, agent and orchestration code
- `explanation/` – simplified Medical Care Pathway logic
- `evaluation/` – helpers for running experiments
- `deployment/` – FastAPI backend and Streamlit demo
- `data/` – example synthetic patient records

## Usage

Install dependencies and start the API:

```bash
pip install -r requirements.txt
uvicorn IBS_Reticulotype_Project.deployment.backend_deployment:app --reload
```

To train the agent from the command line:

```bash
python -m IBS_Reticulotype_Project.core.train_rl_agent --timesteps 5000
```
