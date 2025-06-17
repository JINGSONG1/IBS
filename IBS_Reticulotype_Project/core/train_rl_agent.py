from .agent_orchestrator import AgentOrchestrator


def main(timesteps: int = 1000):
    orchestrator = AgentOrchestrator()
    orchestrator.train(timesteps)
    print("Training finished")


if __name__ == "__main__":
    main()
