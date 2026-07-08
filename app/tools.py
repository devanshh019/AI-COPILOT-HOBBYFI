from app.sql_generator import sql_query
from app.natural import natural_language
from app.db import execute
from app.memory import add_memory

DEBUG=False
def read_tool(query: str):
    sql=sql_query(query)
    res=execute(sql)
    ans=natural_language(res,query)
    add_memory(query,ans)

    if DEBUG:
        return {
            'sql':sql,
            'result':res,
            'ans':ans
        }
    else: 
        return ans
    


def write_tool(query: str):

    sql = sql_query(query)
    print("\nGenerated SQL:")

    print(sql)

    choice = input("\nApprove this query? (y/n): ").strip().lower()

    if choice == "y":

        result = execute(sql)
        add_memory(query,'Database updated successfully')
        if DEBUG:
            return {

                "status": "SUCCESS",

                "message": "Database updated successfully.",

                "sql": sql

            }
        else:
            return "SUCCESS DB UPDATED"
    else:
        add_memory(query,'CANCELED')
        return {

            "status": "CANCELLED",

            "message": "Update cancelled by user."

        }