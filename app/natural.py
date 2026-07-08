from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from app.config import MISTRAL_API_KEY,MODEL_NAME
from app.memory import add_memory

model=ChatMistralAI(api_key=MISTRAL_API_KEY,model_name=MODEL_NAME)
prompt=ChatPromptTemplate.from_messages([
    (

        "system","""
You are an AI assistant.
Your job is to convert SQL query results into a natural language response.
Rules:
1. Be concise and professional.
2. Do not mention SQL or databases.
3. If the result is empty, say "No matching records found."
4. If the result contains numbers, summarize them naturally.
5. If the result contains multiple rows, present them in a readable way.
6.If the result contains monetary values, represent them in Indian Rupees (₹), not dollars.
When the SQL result contains dates, explain them naturally.
Instead of:
₹6900
say
The revenue from July 5, 2026 through July 8, 2026 was ₹6,900.
"""),

    (

        "human","""
User Query:
{query}
SQL Result:
{result}
"""
    )   
])

chain=prompt | model

def natural_language(r : str ,q:str):
    response=chain.invoke({'query':q,'result':r})
    return response.content
