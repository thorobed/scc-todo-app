from fastapi import FastAPI
import sqlite3


app = FastAPI()

@app.get('/get_tasks')
def get_tasks():
    with sqlite3.connect("./todos.db") as conn:
        query = conn.execute("SELECT * FROM todos;")
        result = query.fetchall

        response = []
        for todo in result:
            todo_json = {
                'id': todo[0],
                'todo': todo[1]
            }
            response.append(todo_json)
        return response

@app.get('/create_tasks')
def create_tasks(todo: str):
    with sqlite3.connect('./todos.db') as conn:
        try:
            query = conn.execute("INSERT INTO todos (todo) VALUES (?)", (todo,))
            return True
        except:
            return "Error"
        
@app.get('/delete_task')
def delete_task(id: int):
    with sqlite3.connect('./todos.db') as conn:
        try:
            query = conn.execute('DELETE ROM todos WHERE id=?', (id,))
            return True
        except:
            return "Error"