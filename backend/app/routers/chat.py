from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..services.openai_service import get_agent_response
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

class ChatRequest(BaseModel):
    prompt: str
    agent_role: str = "SRE"

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        logger.info(f"📩 Chat request received: {request.prompt[:50]}...")

        response_text = await get_agent_response(
            request.prompt,
            request.agent_role
        )

        return {
            "response": response_text,
            "agent": request.agent_role,
            "status": "success"
        }

    except Exception as e:
        logger.error(f"❌ Chat Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))