from fastapi import FastAPI, Request
import uvicorn
from middleware import log_middleware
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()
app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)

@app.get('/')
async def root() -> dict:
    return {'message': 'Hello World'}

@app.get('/test')
async def test_root() -> dict:
    return {'message': 'Testing end point'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)