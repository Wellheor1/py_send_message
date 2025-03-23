import uvicorn

from settings import ADDRESS, PORT

if __name__ == "__main__":
    uvicorn.run(f"main:app", host=ADDRESS, port=PORT, reload=True)