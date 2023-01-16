from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session
from app.models.user import Register, Login
from config.session import get_session
from app.controllers import authController
from config.auth import AuthHandler
from helpers.validation import validate

authHandler = AuthHandler()

router = APIRouter()

@router.post('/register', status_code=201)
async def register(data : Register, session : Session = Depends(get_session)):
    validate(data, [
        [
            "name", ["required","min:8"]
        ],
        [
            "password", ["required","min:8"]
        ],
        [
            "email", ["required", "email"]
        ]
    ])
    return await authController.register(data, session)

@router.post('/login', status_code=200)
async def login(data: Login, session : Session = Depends(get_session)):
    validate(data, [
        [
            "password", ["required","min:8"]
        ],
        [
            "email", ["required", "email"]
        ]
    ])
    return await authController.login(data, session)

@router.get('/me', status_code=200)
async def me(session : Session = Depends(get_session), data = Depends(authHandler.auth_wrapper)):
    return await authController.me(data, session)