from sqlalchemy import (
    LargeBinary,
    ForeignKey,
    Integer,
    Column,
    String,
    Table,
    Enum
)
from sqlalchemy.orm import relationship
from sqlalchemy_utils import (
    JSONType,
    URLType
)

from sql_sucuri.database import Base
from .enums import MediaType, CourseType


association_table = Table(
    'association_table', Base.metadata,
    Column('profile_id', String, ForeignKey('profile.id')),
    Column('project_id', String, ForeignKey('project.id'))
)

association_label = Table(
    'association_label', Base.metadata,
    Column('label_id', String, ForeignKey('label.id')),
    Column('project_id', String, ForeignKey('project.id'))
)

association_org = Table(
    'association_org', Base.metadata,
    Column('org_id', String, ForeignKey('organization.id')),
    Column('profile_id', String, ForeignKey('profile.id'))
)


class Organization(Base):
    __tablename__ = 'organization'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    about = Column(String)
    url = Column(URLType)
    social_media = Column(JSONType)
    owner = Column(String, ForeignKey('profile.id'))
    projects = relationship('project', back_populates='org')
    members = relationship(
        'profile',
        secondary=association_org,
        back_populates='orgs'
    )


class Profile(Base):
    __tablename__ = 'profile'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    social_media = Column(JSONType)

    orgs_owned = relationship('organization', back_populates='owner')
    orgs = relationship(
        'organization',
        secondary=association_org,
        back_populates='members'
    )
    projects = relationship(
        'project',
        secondary=association_table,
        back_populates='team'
    )


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True, index=True)
    about = Column(String)
    name = Column(String, index=True)
    url = Column(URLType)
    org = Column(String, ForeignKey('organization.id'))
    social_media = Column(JSONType)
    thumbnail = Column(LargeBinary)
    team = relationship(
        'profile',
        secondary=association_table,
        back_populates='projects'
    )
    labels = relationship(
        'label',
        secondary=association_label,
        back_populates='projects'
    )
    media_type = Column(
        Enum(MediaType, values_callable=lambda obj: [e.value for e in obj]),
        nullable=False,
        default=MediaType.AUDIOVISUAL.value,
        server_default=MediaType.AUDIOVISUAL.value
    )
    course_type = Column(
        Enum(CourseType, values_callable=lambda obj: [e.value for e in obj]),
        nullable=True,
        default=CourseType.ONLINE.value,
        server_default=CourseType.ONLINE.value
    )


class Label(Base):
    id = Column(Integer, primary_key=True, index=True)
    label = Column(String)
    description = Column(String)
    projects = relationship(
        'project',
        secondary=association_label,
        back_populates='labels'
    )
