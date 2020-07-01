from fastapi import Depends
from sqlalchemy.orm import Session

# IIB
from sucuri.database.dependency import get_db
from sucuri.models.models import Profile
from sucuri.schemas.schemas import ProfileSchema


def post_profile(profile: ProfileSchema, db: Session = Depends(get_db)):
    db_profile = Profile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile
