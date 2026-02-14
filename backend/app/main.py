import logging
from fastapi import FastAPI
from .routers import chat, health, analysis
from .services.db_service import engine, Base
from .config import settings, setup_logging

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)

# Initialize App
app = FastAPI(title="DevAutoPilot API", version="1.0.0")

@app.on_event("startup")
async def startup_event():
    logger.info("🚀 DevAutoPilot is starting up...")
    
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("✅ Database tables verified.")
    except Exception as e:
        logger.warning(f"Database connection failed: {e}. Continuing without database...")

# Routers
app.include_router(chat.router, prefix="/api/v1", tags=["Chat"])
app.include_router(health.router, tags=["Health"])
app.include_router(analysis.router, prefix="/api/v1", tags=["Analysis"])

@app.get("/")
def root():
    return {"message": "DevAutoPilot Agentic Platform is Running 🚀"}