from sqlalchemy.orm import Session

# IIB
from sucuri.database.dependency import get_db
from sucuri.models.models import Organization
from sucuri.schemas.schemas import OrganizationSchema


def post_organization(organization: OrganizationSchema, db: Session):
    db_organization = Organization(**organization.dict())
    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)
    return db_organization


def get_organization(organization_id: int, db: Session):
    return db.query(Organization).filter(Organization.id == organization_id).first()


def get_organizations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Organization).offset(skip).limit(limit).all()


def delete_organization(organization_id: int, db: Session):
    db.query(Organization).filter(Organization.id == organization_id).delete()
    db.commit()
    return


def update_organization(
    old_organization: Organization, organization: OrganizationSchema, db: Session
):
    db_organization = Organization(**organization.dict())
    old_organization.name = db_organization.name
    old_organization.about = db_organization.about
    old_organization.social_media = db_organization.social_media
    old_organization.owner = (
        db_organization.owner if db_organization.owner else old_organization.owner
    )
    old_organization.members = (
        db_organization.members if db_organization.members else old_organization.members
    )
    db.commit()
    return
