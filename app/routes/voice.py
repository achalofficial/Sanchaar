from fastapi import APIRouter, UploadFile, File

from app.services.voice_processor import VoiceProcessor

router = APIRouter()

processor = VoiceProcessor()


@router.post("/voice")
async def process_voice(
    audio: UploadFile = File(...)
):

    temp_path = f"/tmp/{audio.filename}"

    with open(temp_path, "wb") as buffer:
        buffer.write(await audio.read())

    result = processor.process(
        temp_path
    )

    return result