import uvicorn

if __name__ == "__main__":
    uvicorn.run(f"main:app", host='127.0.0.1', port=10000, reload=True)