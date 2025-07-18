from openai import AsyncOpenAI

from agent.configs import *
from agent.schema.message import Message


client = AsyncOpenAI(api_key=GROQ_API_KEY, base_url=BASE_URL, timeout=REQUEST_TIMEOUT_SECONDS)


async def create_chat_completion_service(messages: list[Message], model=MODEL_NAME) -> Message:
    response = await client.chat.completions.create(
        model=model,
        messages=[msg.model_dump() for msg in messages]
    )
    output = response.choices[0].message
    return Message(
        role=output.role,
        content={"content": output.content}
    )