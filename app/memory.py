conversation_history = []
MAX_HISTORY = 4
def get_context():
    context = ""

    for chat in conversation_history:
        context += f"""
User: {chat['user']}
Assistant: {chat['assistant']}
"""

    return context

def add_memory(user:str,response:str):
    conversation_history.append({
        'user':user,
        'assistant':response
    })
    if(len(conversation_history)>MAX_HISTORY): 
        conversation_history.pop(0)