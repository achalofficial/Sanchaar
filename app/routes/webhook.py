from fastapi import APIRouter, Request

router = APIRouter()


@router.post("/webhook")
async def webhook(request: Request):
    payload = await request.json()

    print("Webhook received:")
    print(payload)

    return {
        "status": "received"
    }