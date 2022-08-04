from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response

from microblog.blog import router
from settings import settings
import uvicorn
from routers import routers
from src.app.db.db import SessionLocal

app = FastAPI(
    title='usrful',
)

@app.middleware('http')
async def db_session_middleware(request: Request, call_next):
    response = Response('Internal server error', status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

app.include_router(routers)


if __name__ == '__main__':
    uvicorn.run('main:app',
                port=settings.server_port,
                host=settings.server_host,
                reload=True)
