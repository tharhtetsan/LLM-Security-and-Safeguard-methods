from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
import uvicorn


# Initialize FastAPI application
app = FastAPI()

# Serve static files (such as your index.html)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Route to serve the HTML file directly
@app.get("/", response_class=HTMLResponse)
async def read_index():
    file_path = "static/index.html"  # path to the index.html file
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            html_content = file.read()
        return HTMLResponse(content=html_content)
    else:
        return HTMLResponse(content="<h1>File not found!</h1>", status_code=404)


if __name__ == "__main__":
    uvicorn.run("admin:app", host='0.0.0.0', port=8888, reload=True)