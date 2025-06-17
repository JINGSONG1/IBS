# IBS Project synced to root level for Actions

## MCP Agent Example

This repository includes a simple demonstration of training a reinforcement learning
agent on a simulated multi-core platform (MCP). The environment loads tasks from
a time-series CSV file and rewards the agent for minimizing waiting time on each
core.

To run the example:

```bash
pip install -r requirements.txt
python IBS_Reticulotype_Project/core/train_mcp_agent.py
```

The task file `IBS_Reticulotype_Project/data/tasks_timeseries.csv` illustrates the
required timestamped format for questionnaire or task inputs.
