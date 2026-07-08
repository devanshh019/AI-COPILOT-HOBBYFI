from fastapi import FastAPI
from pydantic import BaseModel

from app.guardrail import check_guardrail
from app.agent import run_agent

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "AI Copilot HobbyFi API is running 🚀"
    }


class ChatRequest(BaseModel):
    query: str


@app.post("/chat")
def chat(request: ChatRequest):

    allowed, message = check_guardrail(request.query)

    if not allowed:
        return {
            "status": "blocked",
            "message": message
        }

    return run_agent(request.query)