from app.sql_generator import sql_query
from app.db import execute
def read_tool(query: str):
    sql=sql_query(query)
    res=execute(sql)
    return {
        'generated sql':sql,
        'results':res
    }
    


def write_tool(query):
    return {
        "status": "PENDING_APPROVAL",
        "query": query,
        "message": "Owner approval is required before executing this action."
    }