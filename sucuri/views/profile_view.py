# Standard Library
from typing import List

from fastapi import Depends
from fastapi import APIRouter
from fastapi import HTTPException
from sqlalchemy.orm import Session

# IIB
from sucuri.database.config import SessionLocal
from sucuri.database.config import engine
from sucuri.models.models import Base
from sucuri.models.models import Profile
from sucuri.schemas.schemas import ProfileSchema


router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def root():
    return {"message": "Hello World"}



@router.post("/profiles/", response_model=ProfileSchema)
def create_profile(profile: ProfileSchema, db: Session = Depends(get_db)):
    print(profile.dict())


    db_profile = Profile(**profile.dict())
    print('db_profile: ', db_profile)
    db.add(db_profile)
    print('add db_profile: ')
    db.commit()
    print('commit')
    db.refresh(db_profile)
    return db_profile
