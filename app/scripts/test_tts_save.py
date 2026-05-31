from app.llms.sarvam_client import SarvamClient

client = SarvamClient()

path = client.synthesize(
    "नमस्ते अचल जी। संचार सफलतापूर्वक काम कर रहा है।",
    "output.wav"
)

print(path)