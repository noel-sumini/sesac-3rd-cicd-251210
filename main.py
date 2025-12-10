from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel
app = FastAPI()


class CreateTodoSchema(BaseModel):
    id:str
    title:str
    content:str


conn = psycopg2.connect(
    host = 'db-container', 
    port = 5432, 
    database ='postgres', 
    user = 'postgres', 
    password = '1234',
    cursor_factory = RealDictCursor
)

# Create

@app.post("/create", status_code=200)
def create_todo(data:CreateTodoSchema):
    
    cursor = conn.cursor()
    
    id = data.id
    title = data.title
    content = data.content


    cursor.execute("""
        INSERT INTO todos (id, title, content)
        VALUES (%s, %s, %s) RETURNING *
    """,
    (id, title, content)
    )
    new_data = cursor.fetchone()
    conn.commit()
    cursor.close()


    return new_data


# Read

@app.get("/read", status_code=200)
def read_todo(id:str):
    cursor.execute(
        """
            SELECT * FROM todos 
            WHERE id = %s
        """, 
        (id, )
    )
    data = cursor.fetchall()
    cursor.close()

    return {"data" : data}


# Update


# Delete