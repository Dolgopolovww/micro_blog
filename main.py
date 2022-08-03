from fastapi import FastAPI
from settings import settings
import uvicorn

app = FastAPI(
    title='usrful',
)

@app.get('/')
def res():
    return {'hi':'0000'}

if __name__ == '__main__':
    uvicorn.run('main:app',
                port=settings.server_port,
                host=settings.server_host,
                reload=True)
