from fastapi import HTTPException
from app.models.user import User
from config.auth import AuthHandler
from datetime import datetime

authHandler = AuthHandler()


async def login(data, session):
    user = session.query(User).filter(User.email == data.email).all()
    if len(user) == 0:
        raise HTTPException(status_code=422, detail="Email belum terdaftar")
    if not authHandler.verify_password(data.password, user[0].password):
        raise HTTPException(status_code=401, detail="Kredensial Salah")
    token = authHandler.encode_token(user[0].id)
    return {
        "token": token,
        "detail": "success logged in"
    }

async def register(data, session):
    user = session.query(User).filter(User.email.contains(data.email))
    if 'email' in user:
        raise HTTPException(status_code=422, detail="Email telah terdaftar")
    hashed_password = authHandler.get_password_hash(data.password)
    try:
        user = User(
            name = data.name,
            email = data.email,
            password = hashed_password,
            status = 'basic',
            created_at = datetime.now()
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        token = authHandler.encode_token(user.id)
        return {
            "token": token,
            "detail": "success register new account"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
async def me(data, session):
    del data.password
    return data