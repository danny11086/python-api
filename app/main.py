from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routes import alarm

app = FastAPI()

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(alarm.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
