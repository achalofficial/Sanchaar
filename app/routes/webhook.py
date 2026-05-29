from fastapi import APIRouter, Request

from app.services.message_processor import MessageProcessor

router = APIRouter()

processor = MessageProcessor()


@router.post("/webhook")
async def webhook(request: Request):
    payload = await request.json()

    message = payload.get("message", "")

    response = processor.process(message)

    return {
        "response": response
    }