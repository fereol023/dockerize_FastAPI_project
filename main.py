import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/home')
def index():
    return {'details': 'Hello, world!'}


if __name__ == '__main__':
    uvicorn.run(app) 