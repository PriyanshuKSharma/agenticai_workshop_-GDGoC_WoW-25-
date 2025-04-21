# LangGraph Introduction Notebook

This Jupyter Notebook introduces the core features of **LangGraph**, using Google Vertex AI for building a simple conversational AI system. It demonstrates how to create a graph-based conversational flow with built-in tools and state management.

## 🚀 Overview

This notebook walks through:

- Setting up **LangGraph** with **Google Vertex AI**
- Implementing a basic conversational loop
- Integrating math tools: **Add**, **Multiply**, and **Divide**
- Managing message state with `MessagesState`
- Visualizing the graph using **Mermaid.js**

## 🧠 Key Features

- ✅ Uses Vertex AI's **Gemini 2.0 Flash model**
- ✅ Demonstrates structured control flow using LangGraph
- ✅ Simple integration of multiple tools
- ✅ Visual graph representation

## 📦 Requirements

- Python 3.8+
- A Google Cloud Project with **Vertex AI enabled**

Install dependencies:

```bash
pip install --upgrade --user \
  "google-cloud-aiplatform[evaluation,langchain,reasoningengine]" \
  "langchain_google_vertexai" \
  "langgraph" \
  "cloudpickle==3.0.0" \
  "pydantic>=2.10" \
  "requests"
```

## 🛠️ Setup Instructions

1. **Enable Vertex AI API** in your Google Cloud project.
2. **Authenticate** using service account or user credentials:
   ```bash
   gcloud auth application-default login
   ```
3. **Open the notebook** in Jupyter or Colab.
4. Run each cell and follow the prompts.

## 📈 Visualization

Graph control flow is visualized using **Mermaid** diagrams, showing how nodes and state transitions are defined.

## 📌 Best Practices

- Use environment variables for secrets/keys
- Modularize your tool integrations
- Always validate API responses

## 🤝 Acknowledgments

- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Google Vertex AI](https://cloud.google.com/vertex-ai)
- [LangChain Community](https://www.langchain.com/)
- [Bhushan Garware(Cloud Workshop-25)](https://github.com/BhushanGarware)
