from app.agents.chat_agent import ChatAgent

class MessageProcessor:

    def __init__(self):
        self.agent = ChatAgent()

    def process(self, message: str) -> str:
        return self.agent.respond(message)