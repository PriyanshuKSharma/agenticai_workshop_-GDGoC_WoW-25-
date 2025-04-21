# LangGraph Multi-Agent Workflow

This project demonstrates an advanced **multi-agent system** using the LangGraph framework on Google Vertex AI. It features a dynamic **supervisor-agent architecture** for task delegation and collaboration among specialized agents.

## 🧩 Overview

This notebook showcases:

- A **Supervisor Node** for routing tasks
- Two specialized agents:
  - **Researcher Agent**: Handles queries and info retrieval
  - **Calculator Agent**: Solves mathematical tasks
- State tracking and task delegation using LangGraph's `StateGraph`

## ⚙️ Core Components

| Node        | Functionality                        |
|-------------|--------------------------------------|
| Supervisor  | Interprets input & assigns tasks     |
| Researcher  | Responds with relevant information   |
| Calculator  | Performs mathematical calculations   |

## 📦 Requirements

- Python 3.8+
- Google Cloud Project with Vertex AI access

Install required packages:

```bash
pip install --upgrade --user \
  "google-cloud-aiplatform[evaluation,langchain,reasoningengine]" \
  "langchain_google_vertexai" \
  "langgraph" \
  "cloudpickle==3.0.0" \
  "pydantic>=2.10" \
  "requests"
```

## ☁️ Google Cloud Setup

1. Create and configure your GCP project.
2. Enable **Vertex AI API**.
3. Authenticate with:
   ```bash
   gcloud auth application-default login
   ```

## 🚀 Running the Notebook

1. Open `LangGraph_MultiAgent.ipynb` in Jupyter or Colab.
2. Follow the cell-by-cell instructions to initialize the graph and agents.
3. Input queries and observe dynamic agent interactions and task routing.

## 📊 Visualization

The LangGraph architecture and control flow are visualized using **Mermaid**, showing how agents interact and how decisions are routed.

## ✅ Best Practices

- Modularize each agent’s logic
- Use environment variables for auth
- Incorporate retry/error handling mechanisms

## 💡 Use Cases

- AI assistants that combine tools (calculator + researcher)
- Multi-agent pipelines for research, analysis, and reporting
- Workflow automation in a graph-structured environment

## 🤝 Acknowledgments

- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Google Vertex AI](https://cloud.google.com/vertex-ai)
- [LangChain Community](https://www.langchain.com/)

## GDGoC: Cloud Workshop-25
- [Bhushan Garware](https://github.com/BhushanGarware)
