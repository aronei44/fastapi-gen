from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.database import Base, engine
from routes import authRoute

app = FastAPI()

Base.metadata.create_all(engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/api/check')
async def root():
    return {
        "message": "ok"
    }

app.include_router(authRoute.router, prefix="/api/auth", tags=["Authentication"])