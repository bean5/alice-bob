from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
async def get_root():
    return {"message": "ok"}


@app.get("/health")
async def get_health():
    return {"message": "ok"}


@app.get("/hello")
async def get_hello():
    return {"message": "hello"}


@app.post("/verify")
async def post_verify():
    return {"message": "TODO"}


def main():
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=os.environ.get("PORT", 8080))


if __name__ == "__main__":
    main()
