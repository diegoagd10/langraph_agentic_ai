"""
LangGraph Combined Example: ReAct Agent + Memory + Human-in-the-Loop

This example demonstrates:
1. ReAct Agent - Agent that DECIDES vs EXECUTES (two separate nodes!)
2. Memory - Persisting conversation across interactions
3. Human-in-the-Loop - Pausing for human input
"""

import os
from typing import TypedDict, Annotated, Literal
from dotenv import load_dotenv

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import interrupt
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()

# ============================================================================
# STATE
# ============================================================================

class AgentState(TypedDict):
    """State that tracks messages throughout the conversation"""
    messages: Annotated[list, add_messages]


# ============================================================================
# TOOLS
# ============================================================================

@tool
def get_weather(city: str) -> str:
    """Get the current weather for a city"""
    weather_data = {
        "san francisco": "☀️ Sunny, 72°F",
        "new york": "🌧️ Rainy, 58°F",
        "london": "☁️ Cloudy, 55°F"
    }
    result = weather_data.get(city.lower(), "🤷 Weather data not available")
    print(f"   🔧 EXECUTING TOOL: get_weather('{city}') → {result}")
    return result


@tool
def send_email(recipient: str, subject: str) -> str:
    """Send an email to a recipient"""
    result = f"Email sent to {recipient}"
    print(f"   🔧 EXECUTING TOOL: send_email('{recipient}', '{subject}') → {result}")
    return result


@tool
def ask_human(question: str) -> str:
    """Ask a human for input when you need clarification"""
    print(f"   ⏸️  PAUSING: Waiting for human response to: '{question}'")
    response = interrupt({"question": question})
    return response.get("answer", "No response provided")


tools = [get_weather, send_email, ask_human]


# ============================================================================
# REACT AGENT NODES
# ============================================================================

def create_react_agent():
    llm = ChatOpenAI(model="gpt-4o")
    llm_with_tools = llm.bind_tools(tools)  # LLM knows what tools exist

    # ------------------------------------------------------------------
    # AGENT NODE: LLM DECIDES what to do (doesn't execute!)
    # ------------------------------------------------------------------
    def agent(state: AgentState):
        print("\n🤖 AGENT NODE: LLM is deciding what to do...")
        response = llm_with_tools.invoke(state["messages"])

        # The LLM returns a message with tool_calls (a PLAN, not execution!)
        if hasattr(response, 'tool_calls') and response.tool_calls:
            print(f"   📋 LLM decided to call: {[tc['name'] for tc in response.tool_calls]}")
        else:
            print(f"   💬 LLM decided to respond directly")

        return {"messages": [response]}

    # ------------------------------------------------------------------
    # TOOLS NODE: Actually EXECUTES the tools
    # ------------------------------------------------------------------
    def execute_tools(state: AgentState):
        print("\n⚙️  TOOLS NODE: Executing the tools...")
        tool_map = {tool.name: tool for tool in tools}
        last_message = state["messages"][-1]

        tool_messages = []
        for tool_call in last_message.tool_calls:
            tool = tool_map[tool_call["name"]]
            # THIS is where the tool actually runs!
            result = tool.invoke(tool_call["args"])

            tool_messages.append({
                "role": "tool",
                "content": str(result),
                "tool_call_id": tool_call["id"]
            })

        return {"messages": tool_messages}

    # ------------------------------------------------------------------
    # ROUTER: Check if tools need to be executed
    # ------------------------------------------------------------------
    def should_continue(state: AgentState) -> Literal["tools", "end"]:
        last_message = state["messages"][-1]
        if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
            print("   ➡️  Router: Going to TOOLS node")
            return "tools"
        print("   ➡️  Router: Going to END (done!)")
        return "end"

    # Build the graph
    workflow = StateGraph(AgentState)
    workflow.add_node("agent", agent)
    workflow.add_node("tools", execute_tools)

    workflow.add_edge(START, "agent")
    workflow.add_conditional_edges("agent", should_continue, {
        "tools": "tools",
        "end": END
    })
    workflow.add_edge("tools", "agent")  # Loop back after executing tools

    # Add memory
    memory = InMemorySaver()
    return workflow.compile(checkpointer=memory)


# ============================================================================
# EXAMPLES
# ============================================================================

def main():
    print("=" * 70)
    print("LangGraph: Understanding Agent vs Tools Nodes")
    print("=" * 70)

    graph = create_react_agent()
    config = {"configurable": {"thread_id": "demo_123"}}

    # Example 1: Single tool call
    print("\n\n" + "=" * 70)
    print("📌 EXAMPLE 1: Simple Tool Call")
    print("=" * 70)
    print("User: What's the weather in London?")

    result = graph.invoke({
        "messages": [{"role": "user", "content": "What's the weather in London?"}]
    }, config)

    print(f"\n✅ Final Response: {result['messages'][-1].content}")

    # Example 2: Multi-step (shows the loop)
    print("\n\n" + "=" * 70)
    print("📌 EXAMPLE 2: Multi-Step Task (Shows ReAct Loop)")
    print("=" * 70)
    print("User: Check weather in New York and email it to boss@company.com")

    config2 = {"configurable": {"thread_id": "demo_456"}}
    result = graph.invoke({
        "messages": [{
            "role": "user",
            "content": "Check weather in New York and email the result to boss@company.com"
        }]
    }, config2)

    print(f"\n✅ Final Response: {result['messages'][-1].content}")

    # Example 3: Memory
    print("\n\n" + "=" * 70)
    print("📌 EXAMPLE 3: Memory (Uses previous context)")
    print("=" * 70)
    print("User: What was the weather there?")

    result = graph.invoke({
        "messages": [{"role": "user", "content": "What was the weather there?"}]
    }, config2)

    print(f"\n✅ Final Response: {result['messages'][-1].content}")

    # Summary
    print("\n\n" + "=" * 70)
    print("📚 KEY INSIGHT:")
    print("=" * 70)
    print("""
1. AGENT NODE (with llm_with_tools):
   - LLM sees what tools are available
   - LLM DECIDES which tools to call
   - Returns a message with 'tool_calls' (instructions, not execution!)

2. TOOLS NODE:
   - ACTUALLY EXECUTES the tools
   - Returns results back to the agent

3. ROUTER:
   - If tool_calls exist → go to TOOLS node
   - If no tool_calls → END (agent gave final answer)

This separation allows:
   ✓ Control over execution (logging, error handling)
   ✓ Human-in-the-loop (pause before executing)
   ✓ Multi-step reasoning (agent → tools → agent → tools → ...)
    """)


if __name__ == "__main__":
    main()
