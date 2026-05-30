from app.llms.sarvam_client import SarvamClient


class ChatAgent:

    def __init__(self):
        self.client = SarvamClient()

    def respond(self, message: str) -> str:
        return self.client.generate(message)