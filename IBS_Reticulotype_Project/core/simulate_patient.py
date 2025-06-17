import numpy as np


def generate_patient():
    """Return a random patient symptom vector."""
    return np.random.randint(0, 7, size=5).astype(np.float32)


if __name__ == "__main__":
    print(generate_patient())
