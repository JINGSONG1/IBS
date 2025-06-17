import requests
import streamlit as st

API_URL = "http://localhost:8000"

st.title("IBS Reticulotype Simulator")

anxiety = st.slider("Anxiety", 0, 10, 5)
sleep_quality = st.slider("Sleep Quality", 0, 10, 5)
diarrhea_freq = st.slider("Diarrhea Frequency", 0, 10, 3)
constipation_freq = st.slider("Constipation Frequency", 0, 10, 2)
bloating_freq = st.slider("Bloating Frequency", 0, 10, 4)

if st.button("Simulate"):
    payload = {
        "anxiety": anxiety,
        "sleep_quality": sleep_quality,
        "diarrhea_freq": diarrhea_freq,
        "constipation_freq": constipation_freq,
        "bloating_freq": bloating_freq,
    }
    resp = requests.post(f"{API_URL}/simulate", json=payload)
    st.json(resp.json())
