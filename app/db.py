import sqlite3

DB_PATH='database/hobbyfi.db'

def execute(sql :str):
    conn=sqlite3.connect(DB_PATH)
    conn.row_factory=sqlite3.Row
    cursor=conn.cursor()

    try:
        cursor.execute(sql)
        rows=cursor.fetchall()
        result=[dict(row) for row in rows]
        conn.commit()
        return result
    
    except Exception as e:
        return{
            'status':"ERROR",
            'message':str(e)
        }
    finally:
        conn.close()