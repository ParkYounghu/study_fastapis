# FastAPI 기본 구현

from fastapi import FastAPI

from fastapi.templating import Jinja2Templates
from fastapi import Request
templates = Jinja2Templates(directory="templates/")

app = FastAPI() # app은 class로 판정, 함수가 안에 들어가야함.

from routes.todos import router as todos_router
app.include_router(todos_router, prefix="/todos")


# 정적 파일 설정 # http://localhost:8000/images/temp.jpg
from fastapi.staticfiles import StaticFiles

app.mount("/images", StaticFiles(directory="resources/images"))
app.mount("/css", StaticFiles(directory="resources/css"))

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")





# https://localhost:8000/
@app.get("/")
async def root():
    return {"message": "Hello world"}
def root_html():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hu</title>
    </head>
    <body>
        <div>My name is ParkYoungHu</div>
    </body>
    </html>
    """
    return html_content
pass


@app.get("/html")
async def root_html():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <div>My name is ParkYoungHu</div>
    </body>
    </html>
    """
    return html_content

# http://localhost:8000/main_html
# http://192.168.0.145:8000/main_html
@app.get("/shotdocs_html")
async def main_html(request: Request):
    return templates.TemplateResponse("shotdocs.html", {"request": request})

# http://localhost:8000/main_html_context
@app.get("/main_html_context")
async def main_html_context(request: Request):
    # 템플릿에 전달할 데이터
    context = {
        "request": request,
        "title": "FastAPI + Jinja Example",
        "items": ["Apple", "Banana", "Cherry"],
        "user": {"name": "Sanghun", "age": 33}
    }
    return templates.TemplateResponse("main_context.html", context)

# http://localhost:8000/users/list
@app.get("/users/list")
async def user_list(request: Request):
    users = [
        {"name": "Alice", "age": 25, "city": "Seoul"},
        {"name": "Bob", "age": 30, "city": "Busan"},
        {"name": "Charlie", "age": 28, "city": "Daegu"}
    ]

    context = {
        "request": request,
        "user_list": users
    }
    return templates.TemplateResponse("users/list.html", context)




@app.get("/jinja")
async def jinja_example(request: Request):
    products = [
        {"name": "Laptop", "price": 1200, "tags": ["electronics", "office"]},
        {"name": "Smartphone", "price": 800, "tags": ["mobile", "electronics"]},
        {"name": "Keyboard", "price": 100, "tags": ["accessories"]},
    ]

    return templates.TemplateResponse(
        "10_jinja2.html",
        {"request": request, "products": products}
    )

# http://localhost:8000/board/detail_json?title=Third%20Post&content=This%20is%20the%20third%20post
@app.get("/board/detail_json")
async def mode_details_json(request:Request):
    # request.method
    # request.query_params
    params = dict(request.query_params)
    # return = {"title : "Third Post", "content": "This is the third post."}
    return {"title": params['title'], "content": params['content']}

# http://localhost:8000/board/detail_json?title=Third%20Post&content=This%20is%20the%20third%20post.
@app.post("/board/detail_post_json")
async def board_details_post_json(request : Request) : # request = Requset()
    # request.method
    # request.query_params
    params = dict(await request.form())

    # return {"title" : "Third Post", "content" : "This is the third post."}
    return {"title" : params['title'], "content" : params['content']}

# http://localhost:8000/board/detail_html/{detail_id}
@app.get("/board/detail_html/{detail_id}")
async def main_html(request: Request, detail_id):
    return templates.TemplateResponse("boards/detail.html"
                                      , {"request": request})


# http://localhost:8000/board/detail_html
@app.get("/board/detail_html")
async def main_html(request: Request):
    return templates.TemplateResponse("boards/detail.html"
                                      , {"request": request})



pass