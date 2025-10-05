# Langraph Agentic AI

## Overview

This project demonstrates the use of LangGraph and LangChain to build agentic AI applications. Agentic AI refers to systems where AI agents can autonomously perform tasks, make decisions, and interact with their environment.

LangGraph is a library for building stateful, multi-actor applications with Large Language Models (LLMs), providing a graph-based framework for orchestrating complex workflows.

LangChain is a framework for developing applications powered by language models, offering components for chains, agents, and integrations.

## Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd langraph_agentic_ai
   ```

2. Create a conda environment:

   ```bash
   conda create -n venv python=3.12
   ```

3. Activate the conda environment:

   ```bash
   conda activate venv
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
   - `python-dotenv`: For loading environment variables.
   - `langchain-openai`: Integration with OpenAI models.
   - `langchain-groq`: Integration with Groq models.
   - `groq`: Groq API client.

## Usage

Once installed, you can start building your agentic AI applications. See the `1-Basics/` directory for introductory examples.

## Examples

The `1-Basics/` folder contains Jupyter notebooks with basic examples:

- `1-simple-graph.ipynb`: Demonstrates building a simple workflow using LangGraph with nodes, edges, and state management.
- `2-chatbot.ipynb`: Shows how to implement a simple chatbot using LangGraph integrated with LLMs from OpenAI and Groq.
- `3-reactive-agent.ipynb`: Demonstrates implementing a ReAct (Reasoning + Acting) agent with router functionality using LangGraph, featuring tools for contact management, email sending, and calendar events.
- `4-plan-and-execute.ipynb`: Shows how to implement a Plan-and-Execute agent that breaks down complex tasks into systematic steps using a planner, executor, and replanner architecture.
- `5-memory.ipynb`: Demonstrates how to implement conversation memory and persistence in LangGraph using checkpointers, enabling stateful conversations across multiple interactions.
- `6-human-in-the-loop.ipynb`: Shows how to implement human-in-the-loop functionality in LangGraph workflows, allowing human oversight and intervention in automated processes.
- `7-state-runtime-validation.ipynb`: Demonstrates state management and runtime validation in LangGraph, showing how to build simple workflows with proper state handling and error management.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
