from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from services.db import get_db_connection
from fastapi.responses import RedirectResponse
from psycopg2.extras import DictCursor

router = APIRouter()

templates = Jinja2Templates(directory="templates/")

# -----------------------------
# POST: Todo 삭제
# -----------------------------
@router.post("/delete/{todo_id}")
def delete_todo(request: Request, todo_id: str):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(f"DELETE FROM todo WHERE id = '{todo_id}';")
        conn.commit()
    conn.close()

    # 삭제 후 다시 /todos/ 로 이동
    return RedirectResponse(url="/todos/", status_code=303)

# http://localhost:8000/todos/
@router.post("/")
async def add_todo_to_db(request: Request):
    params = await request.form()
    conn = get_db_connection()
    with conn.cursor() as cursor:
        pass
        cursor.execute(f"""INSERT INTO todo (item)
                       VALUES ('{params['item']}');""")
        conn.commit()
        
        cursor.execute(f"select id,item from todo;")
        todos = cursor.fetchall()
    conn.close()
        
    context = {
        "request": request,
        "todos": todos
    }
    return templates.TemplateResponse("todos/merged_todo.html"
                                      , context)
# http://localhost:8000/todos/
@router.get("/{todo_id}")
def get_todo(request: Request, todo_id: str):
    conn = get_db_connection()  # DB 연결 테스트 용도
    with conn.cursor(cursor_factory=DictCursor) as cursor:
        # 특정 아이템
        cursor.execute(f"""SELECT id, item 
                        FROM todo 
                        WHERE id = '{todo_id}';""")
        todo = cursor.fetchone()
    # 전체 list
        cursor.execute("""SELECT id, item 
                        FROM todo;""")
        todos = cursor.fetchall()
    conn.close()
        
    context = {
        "request": request,
        "todo": todo,
        "todos": todos
    }
    return templates.TemplateResponse("todos/merged_todo.html"
                                      , context)

# http://localhost:8000/todos/
@router.get("/")
def get_todos_html(request: Request):
    conn = get_db_connection()  # DB 연결 테스트 용도
    with conn.cursor(cursor_factory=DictCursor) as cursor:
        cursor.execute("""SELECT id, item 
                        FROM todo;""")
        todos = cursor.fetchall()
    conn.close()

    context = {
        "request": request,
        "todos": todos
    }
    return templates.TemplateResponse("todos/merged_todo.html", context)

