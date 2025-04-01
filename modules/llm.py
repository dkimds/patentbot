from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

os.environ["LANGSMITH_TRACING"] = "true"
load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def get_llm():
    return llm