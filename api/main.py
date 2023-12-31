import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings

from routers import auth, user

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(auth.router)
app.include_router(user.router)


@app.get('/')
async def root():
    return {'message': 'Everything is working'}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=settings.api_port)
