import uvicorn

from app.settings import ADDRESS, PORT

if __name__ == "__main__":
    uvicorn.run(f"app.main:app", host=ADDRESS, port=PORT, reload=True)
