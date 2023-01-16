import jwt
from fastapi import HTTPException, Security, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from config.session import get_session
from app.models.user import User
import os

class AuthHandler():
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = os.getenv('SECRET')

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)
    
    def encode_token(self, user_id):
        payload = {
            'exp': datetime.now() + timedelta(days=1),
            'iat': datetime.now(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            self.secret,
            algorithm="HS256"
        )

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms="HS256")
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token Expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Token Invalid")

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security), session : Session = Depends(get_session)):
        user = session.query(User).get(self.decode_token(auth.credentials))
        return user