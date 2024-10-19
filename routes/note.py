
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from models.note import Note

from config.db import con

from schema.note import noteEntity , notesEntity

template = Jinja2Templates(directory="template")

note = APIRouter()


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = con.notes.notes.find()
    newDocs = []

    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "title": doc["title"],
            "description": doc["description"]
        })

    return template.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})

@note.post("/")
async def add_note(request: Request):
    form = await request.form()
    print(form)
    inserted_note = con.notes.notes.insert_one(dict(form))
    print(inserted_note)
    return {"message": "Note added successfully."}