from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import create_access_token, verify_password
from app.db.repositories.user import UserRepository
from app.schemas.token import Token


class AuthService:
    def __init__(self, db: AsyncSession):
        self.repo = UserRepository(db)

    async def authenticate(self, email: str, password: str) -> Optional[Token]:
        user = await self.repo.get_by_email(email)
        if not user or not verify_password(password, user.hashed_password):
            return None
        return Token(access_token=create_access_token(subject=user.email))
