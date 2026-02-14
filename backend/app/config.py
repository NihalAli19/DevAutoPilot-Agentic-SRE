import logging
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Azure OpenAI
    AZURE_OPENAI_API_KEY: str
    AZURE_OPENAI_ENDPOINT: str
    AZURE_OPENAI_API_VERSION: str
    AZURE_OPENAI_DEPLOYMENT_NAME: str

    # Database
    DATABASE_URL: str

    # App
    APP_NAME: str = "DevAutoPilot"
    DEBUG: bool = False

    class Config:
        env_file = ".env"


settings = Settings()


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )