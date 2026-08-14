from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


from ai_engine import generate_response

from database import (
    initialize,
    save_conversation,
    create_task,
    get_tasks
)


app = FastAPI(

    title="Astra AI",

    description=
        "Personal Academic and Career Copilot",

    version="1.0.0"

)


app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)


initialize()


# -------------------------
# MODELS
# -------------------------

class ChatRequest(BaseModel):

    message: str


class TaskRequest(BaseModel):

    title: str


# -------------------------
# HOME
# -------------------------

@app.get("/")
def home():

    return {

        "application":
            "Astra AI",

        "status":
            "online",

        "description":
            "Academic and Career Copilot"

    }


# -------------------------
# HEALTH
# -------------------------

@app.get("/api/health")
def health():

    return {

        "status":
            "healthy"

    }


# -------------------------
# AI CHAT
# -------------------------

@app.post("/api/chat")
def chat(request: ChatRequest):

    response =
        generate_response(
            request.message
        )


    save_conversation(

        request.message,

        response

    )


    return {

        "response":
            response

    }


# -------------------------
# TASKS
# -------------------------

@app.post("/api/tasks")
def add_task(
    request: TaskRequest
):

    task_id =
        create_task(
            request.title
        )


    return {

        "success":
            True,

        "task_id":
            task_id

    }


@app.get("/api/tasks")
def tasks():

    return {

        "tasks":
            get_tasks()

    }


# -------------------------
# RUN
# -------------------------

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(

        "main:app",

        host="0.0.0.0",

        port=8000,

        reload=True

    )