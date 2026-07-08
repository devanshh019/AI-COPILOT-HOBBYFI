from langchain_mistralai import ChatMistralAI
from app.config import MISTRAL_API_KEY,MODEL_NAME
from langchain_core.prompts import ChatPromptTemplate

model=ChatMistralAI(api_key=MISTRAL_API_KEY,model_name=MODEL_NAME,temperature=0)

prompt=ChatPromptTemplate.from_messages(
    [
        (
    "system",
    """
You are an expert SQLite query generator.

Your task is to convert the user's natural language request into a valid SQLite query.

Database Schema:

users(
    id,
    name,
    email,
    sport,
    membership,
    trial_end
)

revenue(
    id,
    customer_name,
    amount,
    date
)

Examples:

Question: Show today's revenue
SQL:
SELECT SUM(amount) AS total_revenue
FROM revenue
WHERE date = date('now');

Question: List badminton users
SQL:
SELECT *
FROM users
WHERE LOWER(sport) = 'badminton';

Question: Show all premium members
SQL:
SELECT *
FROM users
WHERE LOWER(membership) = 'premium';

Question: Show Rahul's details
SQL:
SELECT *
FROM users
WHERE LOWER(name) = 'rahul';

Rules:
1. Return ONLY valid SQLite SQL.
2. Do NOT use markdown.
3. Do NOT explain the query.
4. Return exactly ONE SQL statement.
5. For text comparisons, ALWAYS use LOWER(column_name).
6. Use SELECT * unless the user specifically asks for particular columns.
7. Use SQLite syntax only.
"""
),
("human", "{query}")
    ]
)

chain=prompt | model

def sql_query(q : str):
    ans=chain.invoke({'query':q})
    return ans.content.strip()