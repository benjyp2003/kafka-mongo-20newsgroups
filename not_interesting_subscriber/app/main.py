
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from manager import Manager

app = FastAPI()
manager = Manager()


class Articles(BaseModel):
    articles: list[dict]

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Interesting Subscriber Service"}


@app.get("/get_not_interesting_articles", response_model=Articles)
async def get_interesting_articles() -> Articles:
    try:
        if manager is None:
            raise HTTPException(status_code=500, detail="Manager not initialized")
        return manager.get_articles()
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving not interesting articles data: {str(e)}")

@app.on_event("startup")
async def startup_event():
    try:
        print("Non Interesting Subscriber Service is starting up...")
        global manager
        if manager is None:
            manager = Manager()

    except HTTPException as e:
        print(f"HTTP error during startup: {e}")