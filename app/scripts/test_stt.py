from app.llms.sarvam_client import SarvamClient

client = SarvamClient()

response = client.transcribe(
    "app/samples/sample_2.mp3"
)

print(response)