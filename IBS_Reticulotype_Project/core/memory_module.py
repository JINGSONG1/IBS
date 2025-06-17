class ExperienceBuffer:
    """Simple memory buffer for storing transitions."""

    def __init__(self):
        self.buffer = []

    def add(self, state, action, reward, next_state, done):
        self.buffer.append((state, action, reward, next_state, done))

    def clear(self):
        self.buffer.clear()

    def __len__(self):
        return len(self.buffer)
