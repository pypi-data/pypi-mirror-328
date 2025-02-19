#!/usr/bin/env python3

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Dict, Any, List
import yaml
import os
import uvicorn

app = FastAPI()

# Use absolute path for templates directory
templates_dir = os.path.join(os.path.dirname(__file__), "templates")
templates = Jinja2Templates(directory=templates_dir)

# Store the YAML directory path
yaml_dir = "."

class YAMLData(BaseModel):
    data: List[Dict[str, Any]]

@app.get("/", response_class=HTMLResponse)
async def root():
    return templates.TemplateResponse("index.html", {"request": {}})

@app.get("/api/files")
async def list_files():
    yaml_files = []
    for root, _, files in os.walk(yaml_dir):
        for file in files:
            if file.endswith(".yaml"):
                yaml_files.append(os.path.relpath(os.path.join(root, file), yaml_dir))
    return {"files": yaml_files}

@app.get("/api/file/{file_path:path}")
async def get_file(file_path: str):
    try:
        full_path = os.path.join(yaml_dir, file_path)
        with open(full_path, 'r') as file:
            data = yaml.safe_load(file)
            if not isinstance(data, list):
                data = [data]
            return {"data": data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/file/{file_path:path}")
async def save_file(file_path: str, yaml_data: YAMLData):
    try:
        full_path = os.path.join(yaml_dir, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as file:
            yaml.safe_dump(yaml_data.data, file)
        return {"message": "File saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def main(host: str = "127.0.0.1", port: int = 8000, yaml_dir_path: str = "."):
    global yaml_dir
    yaml_dir = yaml_dir_path
    uvicorn.run(app, host=host, port=port)