import logging
from openai import AzureOpenAI
from ..config import settings

logger = logging.getLogger(__name__)

client = AzureOpenAI(
    api_key=settings.AZURE_OPENAI_API_KEY,
    azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
    api_version=settings.AZURE_OPENAI_API_VERSION
)

async def get_agent_response(prompt: str, agent_role: str):

    system_prompt = f"You are a DevOps {agent_role} specialist."

    logger.info("🤖 Sending request to Azure OpenAI...")

    response = client.chat.completions.create(
        model=settings.AZURE_OPENAI_DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        max_completion_tokens=800
    )

    logger.info("✅ Received response from Azure OpenAI")

    return response.choices[0].message.content