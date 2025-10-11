# Langraph Agentic AI

## Overview

This project demonstrates the use of LangGraph and LangChain to build agentic AI applications. Agentic AI refers to systems where AI agents can autonomously perform tasks, make decisions, and interact with their environment.

LangGraph is a library for building stateful, multi-actor applications with Large Language Models (LLMs), providing a graph-based framework for orchestrating complex workflows.

LangChain is a framework for developing applications powered by language models, offering components for chains, agents, and integrations.

Additionally, this project includes examples replicating recipes from the IBM Granite Community Cookbook, showcasing advanced use cases such as document summarization using IBM Granite models via the Replicate API.

## Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd langraph_agentic_ai
   ```

2. Create a conda environment:

   ```bash
   conda create -n langgraph-dev python=3.12
   ```

3. Activate the conda environment:

   ```bash
   conda activate langgraph-dev
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   This will install the following packages:

   - `langchain`: Core framework for building LLM applications.
   - `langgraph`: Library for creating graph-based AI workflows.
   - `langchain-core`: Essential abstractions and utilities for LangChain.
   - `langchain-community`: Community-contributed integrations and components.
   - `ibm_granite_community`: Utilities for IBM Granite models.
   - `python-dotenv`: For loading environment variables.
   - `langchain-openai`: Integration with OpenAI models.
   - `langchain-groq`: Integration with Groq models.
   - `replicate`: Replicate API client.
   - `groq`: Groq API client.
   - `docling`: Document processing library.
   - `transformers`: Hugging Face transformers for tokenization.

## Usage

Once installed, you can start building your agentic AI applications. See the `1-Basics/` directory for introductory examples and `2-Replicate/` for advanced examples using IBM Granite models.

## Examples

The `1-Basics/` folder contains Jupyter notebooks with basic examples:

- `1-simple-graph.ipynb`: Demonstrates building a simple workflow using LangGraph with nodes, edges, and state management.
- `2-chatbot.ipynb`: Shows how to implement a simple chatbot using LangGraph integrated with LLMs from OpenAI and Groq.
- `3-reactive-agent.ipynb`: Demonstrates implementing a ReAct (Reasoning + Acting) agent with router functionality using LangGraph, featuring tools for contact management, email sending, and calendar events.
- `4-plan-and-execute.ipynb`: Shows how to implement a Plan-and-Execute agent that breaks down complex tasks into systematic steps using a planner, executor, and replanner architecture.
- `5-memory.ipynb`: Demonstrates how to implement conversation memory and persistence in LangGraph using checkpointers, enabling stateful conversations across multiple interactions.
- `6-human-in-the-loop.ipynb`: Shows how to implement human-in-the-loop functionality in LangGraph workflows, allowing human oversight and intervention in automated processes.
- `7-state-runtime-validation.ipynb`: Demonstrates state management and runtime validation in LangGraph, showing how to build simple workflows with proper state handling and error management.

The `2-Replicate/` folder contains examples using the Replicate API with IBM Granite models:

- `getting-started.ipynb`: Basic setup and usage of IBM Granite models via Replicate for simple text generation tasks.
- `summarize.ipynb`: Advanced document summarization workflow using hierarchical chunking with Docling to process book chapters, generate individual summaries, and create a unified book summary.
- `summarize_langchain_only.ipynb`: Similar document summarization but implemented using only standard LangChain components without custom Granite utilities.

## Dependencies

The project dependencies are listed in `requirements.txt` and include core LangChain and LangGraph packages, integrations with various LLM providers, and specialized libraries for document processing and IBM Granite model utilities.

## Special Thanks

Special thanks to IBM and the IBM Granite Community for their contributions, particularly the resource at https://github.com/ibm-granite-community/granite-snack-cookbook/blob/main/recipes/Summarize/Summarize.ipynb.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
