# Standard Library
from typing import ByteString
from typing import List
from typing import Optional

from pydantic import BaseModel

from sucuri.models.enums import MediaType
from sucuri.models.enums import CourseType
from sucuri.models.enums import SocialMedia


class SocialMediaSchema(BaseModel):
    type: SocialMedia
    value: str


class OrganizationSchema(BaseModel):
    id: int
    name: str
    about: str
    url: str
    social_media: str
    owner: Optional[int] = None
    projects: Optional[List[int]] = None
    members: Optional[List[int]] = None

    class Config:
        orm_mode = True


class ProfileSchema(BaseModel):
    name: str
    social_media: SocialMediaSchema
    
    class Config:
        orm_mode = True


class ProjectSchema(BaseModel):
    id: int
    about: str
    name: str
    url: str
    org: Optional[int] = None
    social_media: str
    thumbnail: Optional[str] = None
    team: Optional[List[int]] = None
    labels: Optional[List[int]] = None
    media_type: MediaType
    course_type: CourseType

    class Config:
        orm_mode = True


class LabelSchema(BaseModel):
    id: int
    label: str
    description: str
    projects: Optional[List[int]] = None

    class Config:
        orm_mode = True
