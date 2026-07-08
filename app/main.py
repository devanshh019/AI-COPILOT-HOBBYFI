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

    decision = check_guardrail(request.query)
    if decision != "ALLOW":
        return {
            "status": "BLOCKED",
            "message": "Request blocked by AI Guardrail."
        }
    return run_agent(request.query)
