from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.database import Base, engine
from routes import authRoute

"""
Initializing FastApi
"""
app = FastAPI()

"""
For creating table in database.
Warning, this code always execute migration if something changed in app/models/*.py
"""
Base.metadata.create_all(engine)


"""
For enabling Cross Origin Resource Sharing (CORS).
You can edit allow_origins to your clients target or leave it with '*' if you want to allow all origin.
You can edit allow_methods to your allowed methods (POST, GET, etc) or leave it with '*' if you want to allow all methods.
You can edit allow_headers to your allowed headers (Content-Type, Accept, etc) or leave it with '*' if you want to allow all headers.
"""
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
Test url. you can delete it.
"""
@app.get('/api/check')
async def root():
    return {
        "message": "ok"
    }

"""
For including your routes file. It can be auto generate by executing command :
'py gen.py make:route yourroutename'
Or you can pass it by your self.
"""
app.include_router(authRoute.router, prefix="/api/auth", tags=["Authentication"])