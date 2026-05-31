import os

import base64



from sarvamai import SarvamAI
from app.config import *

from app.utils.text_cleaner import remove_thinking


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

    def chat(self, message: str) -> str:

        response = self.client.chat.completions(
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ],
            model="sarvam-m"
        )

        content = response.choices[0].message.content

        return remove_thinking(content)
    

    def synthesize(self, text: str, output_path: str):

        response = self.client.text_to_speech.convert(
            text=text,
            target_language_code="hi-IN",
            model="bulbul:v3",
            temperature=0.2
        )

        audio_bytes = base64.b64decode(
            response.audios[0]
        )

        with open(output_path, "wb") as f:
            f.write(audio_bytes)

        return output_path