from sqlalchemy import Column
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import LargeBinary
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import relationship
from sqlalchemy_utils import JSONType
from sqlalchemy_utils import URLType

# IIB
from sucuri.database.config import Base

from .enums import CourseType
from .enums import MediaType


association_table = Table(
    "association_table",
    Base.metadata,
    Column("profile_id", Integer, ForeignKey("profile.id")),
    Column("project_id", Integer, ForeignKey("project.id")),
)

association_label = Table(
    "association_label",
    Base.metadata,
    Column("label_id", Integer, ForeignKey("label.id")),
    Column("project_id", Integer, ForeignKey("project.id")),
)

association_org = Table(
    "association_org",
    Base.metadata,
    Column("org_id", Integer, ForeignKey("organization.id")),
    Column("profile_id", Integer, ForeignKey("profile.id")),
)


class Organization(Base):
    __tablename__ = "organization"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    about = Column(String)
    url = Column(URLType)
    social_media = Column(JSONType)
    owner = Column(Integer, ForeignKey("profile.id"))
    members = relationship("Profile", secondary=association_org, backref="orgs")


class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    social_media = Column(JSONType)


class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, index=True)
    about = Column(String)
    name = Column(String, index=True)
    url = Column(URLType)
    org = Column(Integer, ForeignKey("organization.id"))
    social_media = Column(JSONType)
    thumbnail = Column(URLType, nullable=True)
    team = relationship("Profile", secondary=association_table, backref="projects")

    media_type = Column(
        Enum(MediaType, values_callable=lambda obj: [e.value for e in obj]),
        nullable=False,
        default=MediaType.AUDIOVISUAL.value,
        server_default=MediaType.AUDIOVISUAL.value,
    )
    course_type = Column(
        Enum(CourseType, values_callable=lambda obj: [e.value for e in obj]),
        nullable=True,
        default=CourseType.ONLINE.value,
        server_default=CourseType.ONLINE.value,
    )


class Label(Base):
    __tablename__ = "label"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String)
    description = Column(String)
    projects = relationship("Project", secondary=association_label, backref="labels")
