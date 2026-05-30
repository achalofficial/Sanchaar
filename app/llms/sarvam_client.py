import os

from sarvamai import SarvamAI
from app.config import *


class SarvamClient:

    def __init__(self):
        self.client = SarvamAI(
            api_subscription_key=os.getenv(
                "SARVAM_API_KEY"
            )
        )

    def transcribe(self, file_path):
        with open(file_path, "rb") as audio_file:
            return self.client.speech_to_text.transcribe(
                file=audio_file
            )