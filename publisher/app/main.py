from fastapi import FastAPI, HTTPException

from publisher.app.manager import Manager


app = FastAPI()
MANAGER = None

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
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")



@app.on_event("startup")
async def startup():
    try:
        print("Starting up the Publisher API")
        global MANAGER
        MANAGER = Manager()
    except Exception as e:
        print(f"Error during startup: {e}")