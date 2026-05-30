from app.agents.chat_agent import ChatAgent
from app.llms.sarvam_client import SarvamClient


class VoiceProcessor:

    def __init__(self):
        self.stt = SarvamClient()
        self.agent = ChatAgent()

    def process(self, audio_path: str):

        transcript_response = self.stt.transcribe(
            audio_path
        )

        transcript = transcript_response.transcript

        response = self.agent.respond(
            transcript
        )

        return {
            "transcript": transcript,
            "response": response
        }