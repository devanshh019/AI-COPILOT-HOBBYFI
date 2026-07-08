BLOCKED_KEYWORDS = [
    "drop table",
    "delete database",
    "truncate",
    "ignore previous instructions",
    "system prompt",
    "hack",
    "bypass"
]

def check_guardrail(query: str):
    query = query.lower()

    for keyword in BLOCKED_KEYWORDS:
        if keyword in query:
            return False, f"Blocked by Guardrail: '{keyword}' detected."

    return True, "Safe"