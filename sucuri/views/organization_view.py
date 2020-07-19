# Standard Library
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

# IIB
from sucuri.crud.crud_organization import delete_organization
from sucuri.crud.crud_organization import get_organization
from sucuri.crud.crud_organization import get_organizations
from sucuri.crud.crud_organization import post_organization
from sucuri.crud.crud_organization import update_organization
from sucuri.database.dependency import get_db
from sucuri.models.models import Organization
from sucuri.schemas.schemas import OrganizationSchema


router = APIRouter()


@router.post("/organizations/", response_model=OrganizationSchema)
async def create_organization(
    organization: OrganizationSchema, db: Session = Depends(get_db)
):
    return post_organization(organization=organization, db=db)


@router.get("/organizations/{organization_id}", response_model=OrganizationSchema)
async def get_organization_by_id(organization_id: int, db: Session = Depends(get_db)):
    organization = get_organization(organization_id, db)
    if organization is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return organization


@router.get("/organizations/", response_model=List[OrganizationSchema])
async def get_all_organizations(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    organizations = get_organizations(db=db, skip=skip, limit=limit)
    return organizations


@router.delete("/organizations/{organization_id}", response_model=OrganizationSchema)
async def delete_organization_by_id(
    organization_id: int, db: Session = Depends(get_db)
):
    return delete_organization(organization_id, db)


@router.put("/organizations/{organization_id}", response_model=OrganizationSchema)
async def update_organization_by_id(
    organization_id: int,
    organization: OrganizationSchema,
    db: Session = Depends(get_db),
):
    old_organization = get_organization(organization_id, db)
    if old_organization is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return update_organization(old_organization, organization, db)
