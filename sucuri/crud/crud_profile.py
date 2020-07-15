from sqlalchemy.orm import Session

# IIB
from sucuri.database.dependency import get_db
from sucuri.models.models import Profile
from sucuri.schemas.schemas import ProfileSchema


def post_profile(profile: ProfileSchema, db: Session):
    db_profile = Profile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile


def get_profile(profile_id: int, db: Session):
    return db.query(Profile).filter(Profile.id == profile_id).first()


def get_profiles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Profile).offset(skip).limit(limit).all()


def delete_profile(profile_id: int, db: Session):
    db.query(Profile).filter(Profile.id == profile_id).delete()
    db.commit()
    return
