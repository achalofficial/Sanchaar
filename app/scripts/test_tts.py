from app.llms.sarvam_client import SarvamClient

client = SarvamClient()

response = client.client.text_to_speech.convert(
    text="नमस्ते अचल जी। संचार सफलतापूर्वक काम कर रहा है।",
    target_language_code="hi-IN",
    model="bulbul:v3",
    temperature=0.2
)

print(response)