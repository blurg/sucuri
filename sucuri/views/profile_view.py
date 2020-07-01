from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

# IIB
from sucuri.crud.crud_profile import post_profile
from sucuri.database.dependency import get_db
from sucuri.schemas.schemas import ProfileSchema


router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.post("/profiles/", response_model=ProfileSchema)
def create_profile(profile: ProfileSchema, db: Session = Depends(get_db)):
    return post_profile(profile=profile, db=db)
