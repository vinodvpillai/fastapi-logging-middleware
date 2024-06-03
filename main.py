from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
async def root() -> dict:
    return {'message': 'Hello World'}

@app.get('/test')
async def test_root() -> dict:
    return {'message': 'Testing end point'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)