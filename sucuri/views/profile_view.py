# Standard Library
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

# IIB
from sucuri.crud.crud_profile import delete_profile
from sucuri.crud.crud_profile import get_profile
from sucuri.crud.crud_profile import get_profiles
from sucuri.crud.crud_profile import post_profile
from sucuri.crud.crud_profile import update_profile
from sucuri.database.dependency import get_db
from sucuri.models.models import Profile
from sucuri.schemas.schemas import ProfileSchema


router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.post("/profiles/", response_model=ProfileSchema)
async def create_profile(profile: ProfileSchema, db: Session = Depends(get_db)):
    return post_profile(profile=profile, db=db)


@router.get("/profiles/{profile_id}", response_model=ProfileSchema)
async def get_profile_by_id(profile_id: int, db: Session = Depends(get_db)):
    profile = get_profile(profile_id, db)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile


@router.get("/profiles/", response_model=List[ProfileSchema])
async def get_all_profiles(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    profiles = get_profiles(db=db, skip=skip, limit=limit)
    return profiles


@router.delete("/profiles/{profile_id}", response_model=ProfileSchema)
async def delete_profile_by_id(profile_id: int, db: Session = Depends(get_db)):
    return delete_profile(profile_id, db)


@router.put("/profiles/{profile_id}", response_model=ProfileSchema)
async def update_profile_by_id(
    profile_id: int, profile: ProfileSchema, db: Session = Depends(get_db)
):
    old_profile = get_profile(profile_id, db)
    if old_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return update_profile(old_profile, profile, db)
