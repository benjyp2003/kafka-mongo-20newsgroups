import threading
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .manager import Manager

app = FastAPI()
manager = Manager()


class Articles(BaseModel):
    articles: list[dict]

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Non Interesting Subscriber Service"}


@app.get("/get_not_interesting_articles", response_model=Articles)
async def get_not_interesting_articles() -> Articles:
    try:
        return manager.get_articles()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving not interesting articles data: {str(e)}")


@app.on_event("startup")
async def startup_event():
    try:
        print("Non Interesting Subscriber Service is starting up...")
        t = threading.Thread(target=manager.process_messages, args=["not_interesting_categories"], daemon=True)
        t.start()
        print("Started consuming messages...")

    except HTTPException as e:
        print(f"HTTP error during startup: {e}")