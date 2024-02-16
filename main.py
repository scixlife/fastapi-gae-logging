# based on code from Better Stack https://youtu.be/1RLFSOwpf88?si=p9b1W5grkswXn3BO
from fastapi import FastAPI
import uvicorn
from logger import logger
from middleware import log_middleware
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()
app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)
logger.info("Starting API...")

@app.get('/')
async def index() -> dict:
    #logger.info('Request to index page.')
    return {'message': 'Hello, World!'}

@app.get('/upload/video')
async def upload_videos() -> dict:
    #logger.info('Request to video upload page.')
    return {'message': 'Video uploaded.'}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
