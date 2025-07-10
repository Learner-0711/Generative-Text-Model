import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_token = os.getenv("OPENROUTER_API_KEY")

# Instantiate client
gpt_agent = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_token
)

def get_ai_reply(user_query, model_name="openai/gpt-4o-mini", max_reply_len=250, randomness=0.6):
    """
    Sends a query to the language model and retrieves its response.
    """
    try:
        reply = gpt_agent.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "Respond clearly and intelligently."},
                {"role": "user", "content": user_query}
            ],
            max_tokens=max_reply_len,
            temperature=randomness
        )
        return reply.choices[0].message.content.strip()
    except Exception as ex:
        return f"[Error] {str(ex)}"
