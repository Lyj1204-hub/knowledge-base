from fastapi import FastAPI
from app.services import NoteService
from app.storage import NoteStorage

app = FastAPI(
    title="Personal Knowledge Base API",
    description="个人知识库管理系统接口",
    version="0.1.0",
)

storage = NoteStorage("data/notes.json")
service = NoteService(storage)


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "知识库服务运行正常",
    }


@app.get("/notes")
def get_notes():
    return service.list_notes()