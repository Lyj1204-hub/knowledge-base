from fastapi import FastAPI

app = FastAPI(
    title="Personal Knowledge Base API",
    description="个人知识库管理系统接口",
    version="0.1.0",
)


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "知识库服务运行正常",
    }