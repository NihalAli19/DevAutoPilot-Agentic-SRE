from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert
from ..services.openai_service import get_agent_response
from ..services.db_service import get_db
from ..models.schemas import ChatLog
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


class ChatRequest(BaseModel):
    prompt: str
    agent_role: str = "SRE"


@router.post("/chat")
async def chat_endpoint(
    request: ChatRequest,
    db: AsyncSession = Depends(get_db)
):
    try:
        logger.info(f"📩 Chat request received: {request.prompt[:50]}...")

        # 1️⃣ Get AI response
        response_text = await get_agent_response(
            request.prompt,
            request.agent_role
        )

        # 2️⃣ Store in database
        chat_entry = ChatLog(
            agent_role=request.agent_role,
            prompt=request.prompt,
            response=response_text
        )

        db.add(chat_entry)
        await db.commit()

        return {
            "response": response_text,
            "agent": request.agent_role,
            "status": "success"
        }

    except Exception as e:
        logger.error(f"❌ Chat Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))