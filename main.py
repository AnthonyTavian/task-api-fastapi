from fastapi import FastAPI

app = FastAPI(title= "Task FastAPI")


@app.get("/")
def read_root():
    return {"message": "Task API is running!"}

@app.get("/tasks")
def get_tasks():
    return {"id": 1, "title": "Estudar FastAPI", "done": False}