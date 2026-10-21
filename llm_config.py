
import os
import logging

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

logger = logging.getLogger(__name__)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing from .env")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is missing from .env")


# ==========================================
# Primary LLM: Groq
# ==========================================

primary_llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=GROQ_API_KEY,
    temperature=0,
    max_retries=0,
)


# ==========================================
# Secondary LLM: Google Gemini
# ==========================================

secondary_llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0,
)


# ==========================================
# Automatic LLM Fallback
# ==========================================

llm = primary_llm.with_fallbacks(
    [secondary_llm],
    exceptions_to_handle=(Exception,),
)

logger.info("LLM fallback configured: Groq -> Gemini")
