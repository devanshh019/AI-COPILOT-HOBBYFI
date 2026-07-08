def read_tool(query: str):

    return {
        "status": "success",
        "operation": "READ",
        "data": f"Mock Read Result for: {query}"
    }


def write_tool(query: str):

    return {
        "status": "pending_approval",
        "operation": "WRITE",
        "message": f"Approval required for: {query}"
    }