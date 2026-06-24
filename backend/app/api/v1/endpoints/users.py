from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.v1.dependencies.auth import get_current_user
from app.db.session import get_db
from app.db.models.user import User
from app.db.repositories.user import UserRepository
from app.schemas.user import UserCreate, UserResponse

router = APIRouter()


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(payload: UserCreate, db: AsyncSession = Depends(get_db)):
    repo = UserRepository(db)
    if await repo.get_by_email(payload.email):
        raise HTTPException(status_code=400, detail="Email ya registrado")
    return await repo.create(payload)


@router.get("/me", response_model=UserResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user
