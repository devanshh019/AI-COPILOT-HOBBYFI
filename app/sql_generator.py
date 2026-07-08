from langchain_mistralai import ChatMistralAI
from app.config import MISTRAL_API_KEY,MODEL_NAME
from langchain_core.prompts import ChatPromptTemplate

model=ChatMistralAI(api_key=MISTRAL_API_KEY,model_name=MODEL_NAME,temperature=0)

prompt=ChatPromptTemplate.from_messages(
    [
        ('system','''You are an SQLite expert.

Database Schema:

users(
id,name,email,sport,membership,trial_end
)
         
revenue(
id,customer_name,amount,date
)
         
Rules:
1. Generate ONLY SQLite SQL.
2. Do NOT use markdown.
3. Do NOT explain anything.
4. Return only ONE SQL query.
"""

    )'''),
    ('human','{query}')
    ]
)

chain=prompt | model

def sql_query(q : str):
    ans=chain.invoke({'query':q})
    return ans.content.strip()