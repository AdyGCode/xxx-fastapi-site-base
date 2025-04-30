from fastapi import FastAPI,Request, HTTPException
from starlette.responses import HTMLResponse

app = FastAPI(title="FastAPI & Jinja2")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return "message Hello World"

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return "About Page"

