from fastapi import FastAPI, HTTPException

from .manager import Manager


app = FastAPI()
MANAGER = Manager()

@app.get("/")
async def read_root():
    try:
        return {"message": "Welcome to the Publisher API"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")


@app.get("/publish")
async def publish():
    try:
         MANAGER.publish()
         return {"message": "Data published successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")


