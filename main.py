# FastAPI 기본 구현

from fastapi import FastAPI


app = FastAPI() # app은 class로 판정, 함수가 안에 들어가야함.

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

from fastapi.templating import Jinja2Templates
from fastapi import Request
templates = Jinja2Templates(directory="templates/")

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



# 정적 파일 설정 # http://localhost:8000/images/temp.jpg
from fastapi.staticfiles import StaticFiles

app.mount("/images", StaticFiles(directory="resources/images"))
app.mount("/css", StaticFiles(directory="resources/css"))

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

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


pass