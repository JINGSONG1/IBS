from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np

from ..core.doctor_agent import DoctorAgent
from ..core.ibs_env import IBSPatientEnv
from ..explanation.real_mcp_engine import recommend_action

app = FastAPI(title="IBS Reticulotype API")

env = IBSPatientEnv()
agent = DoctorAgent(env)

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "synthetic_patients.csv"


class Patient(BaseModel):
    anxiety: int
    sleep_quality: int
    diarrhea_freq: int
    constipation_freq: int
    bloating_freq: int


@app.get("/")
def read_root():
    return {"status": "ok"}


@app.get("/patients")
def get_patients():
    df = pd.read_csv(DATA_PATH)
    return df.to_dict(orient="records")


@app.post("/train")
def train(timesteps: int = 1000):
    agent.train(timesteps)
    return {"trained": timesteps}


@app.post("/simulate")
def simulate(patient: Patient):
    state = np.array([
        patient.anxiety,
        patient.sleep_quality,
        patient.diarrhea_freq,
        patient.constipation_freq,
        patient.bloating_freq,
    ], dtype=np.float32)
    action = recommend_action(state)
    next_state, reward, done, _ = env.step(action)
    return {
        "action": action,
        "next_state": next_state.tolist(),
        "reward": reward,
        "done": done,
    }
