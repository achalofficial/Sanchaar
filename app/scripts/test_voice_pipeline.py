from app.services.voice_processor import VoiceProcessor

processor = VoiceProcessor()

result = processor.process(
    "app/samples/sample_2.mp3"
)

print(result)