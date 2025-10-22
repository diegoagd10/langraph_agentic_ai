# LangGraph Agentic AI Practice Projects

This file contains a curated list of practice projects to reinforce the concepts learned from the LangGraph course. Each project builds progressively on the skills covered, from basic graph building to advanced multi-agent systems.

## Beginner Projects

- [ ] **Personal Task Manager Bot**
  - Build a chatbot that manages daily tasks using simple state and conditional edges
  - Add memory to persist tasks across conversations
  - Skills: Basic graph building, state management, memory

- [ ] **Recipe Recommendation Agent**
  - Create an agent that suggests recipes based on ingredients
  - Use conditional routing to handle different user preferences
  - Skills: Conditional edges, tool creation, basic ReAct pattern

## Intermediate Projects

- [ ] **Multi-Step Research Assistant**
  - Implement a plan-and-execute agent that researches topics step-by-step
  - Break down complex queries into research, summarization, and presentation phases
  - Skills: Plan-and-execute pattern, multi-node workflows, structured output

- [ ] **Document Q&A System**
  - Build a system that answers questions about uploaded documents
  - Use hierarchical chunking to process documents and retrieve relevant sections
  - Skills: Document processing, chunking, information retrieval

- [ ] **Interactive Story Generator**
  - Create a collaborative storytelling agent with human-in-the-loop
  - Allow users to guide story direction at key plot points
  - Skills: Human-in-the-loop, state persistence, conditional routing

## Advanced Projects

- [ ] **Code Review Automation Agent**
  - Build an agent that reviews code changes and suggests improvements
  - Use plan-and-execute to break down review into analysis, testing, and feedback phases
  - Skills: Complex multi-step workflows, tool integration, structured planning

- [ ] **Personal Finance Advisor**
  - Create an agent that analyzes spending patterns and provides financial advice
  - Integrate with external APIs for market data and budgeting tools
  - Skills: Multiple tools, data processing, complex state management

- [ ] **Educational Tutor Bot**
  - Develop an adaptive learning assistant that adjusts difficulty based on user performance
  - Use memory to track learning progress and customize lessons
  - Skills: State validation, persistent memory, dynamic routing

- [ ] **Meeting Scheduler with Calendar Integration**
  - Build an agent that schedules meetings considering multiple calendars
  - Handle conflicts, send invitations, and follow up on RSVPs
  - Skills: Tool orchestration, external API integration, complex workflows

- [ ] **Content Creation Pipeline**
  - Create an end-to-end content generation system (blog posts, social media, etc.)
  - Use hierarchical processing to generate, edit, and publish content
  - Skills: Document processing, multi-stage pipelines, quality assurance loops

## Project Completion Guidelines

- Start with Beginner projects to build foundational skills
- Mark projects as completed by checking the box `[x]` when finished
- Each project can be scaled by adding features like memory, human oversight, or external integrations
- Document your implementation approach and challenges faced for each project
- Consider open-sourcing completed projects or creating tutorials for others

## Resources

- Refer back to the `1-Basics/` and `2-Replicate/` directories for implementation examples
- Use the course concepts: state management, nodes, edges, tools, memory, and validation
- Experiment with different LLM providers (OpenAI, Groq, Replicate) for variety