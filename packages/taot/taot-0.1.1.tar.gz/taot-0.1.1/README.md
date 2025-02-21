# Tool Ahead of Time (TAoT)

A Python package for creating and managing tool-enabled AI agents using LangChain and OpenAI.

## Installation

```bash
pip install taot
```

## Usage

```python
from taot import create_system_message_taot, create_react_agent_taot
from langchain_openai import ChatOpenAI

# Initialize
model = ChatOpenAI()

# Create system message
system_message = "Your system message here..."
system_message_taot = create_system_message_taot(system_message)

# Prepare messages
messages = [
    {"role": "system", "content": system_message_taot},
    {"role": "user", "content": "Your user message here..."}
]

# Create and invoke agent
agent = create_react_agent_taot(model, tools=[your_tools])
response = agent.invoke({"messages": messages})
```