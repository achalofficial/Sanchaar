from app.agents.chat_agent import ChatAgent

agent = ChatAgent()

response = agent.respond(
    "What is the capital of India?"
)

print(response)