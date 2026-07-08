from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage
from app.config import MISTRAL_API_KEY, MODEL_NAME
from app.tools import read_tool,write_tool


llm = ChatMistralAI(
    model=MODEL_NAME,
    api_key=MISTRAL_API_KEY,
    temperature=0
)


def classify_query(query: str) -> str:

    prompt = f"""
You are an AI router.

Your job is ONLY to classify the user's request.

Rules:

Return READ if the user wants to retrieve or view information.

Examples:
- Show today's revenue
- List all users
- Display memberships

Return WRITE if the user wants to modify data.

Examples:
- Update membership
- Extend Rahul's trial
- Change email

Follow-up questions are also valid requests.

Examples:
- which 3 days?
- last 2 days
- yesterday?
- today?
- his details
- her trial
- their membership
- what about him?
- show it again

If a follow-up question refers to previous conversation,
classify it according to the previous intent.

These are READ requests unless the user is asking to modify data.

If you're unsure, return UNKNOWN.

Respond with ONLY one word:
READ
WRITE
UNKNOWN

User Query:
{query}

"""

    response = llm.invoke([HumanMessage(content=prompt)])

    return response.content.strip().upper()


def run_agent(query :str):
    dec=classify_query(query)

    if(dec.lower()=='read'):
        return read_tool(query)
    elif(dec.lower()=='write'):
        return write_tool(query)
    else:
        return dec