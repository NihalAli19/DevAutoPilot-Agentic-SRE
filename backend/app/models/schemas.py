from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from ..services.db_service import Base


class ChatLog(Base):
    __tablename__ = "chat_logs"

    id = Column(Integer, primary_key=True, index=True)
    agent_role = Column(String(50))
    prompt = Column(Text)
    response = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())