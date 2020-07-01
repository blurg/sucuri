# Standard Library
from enum import Enum


class MediaType(str, Enum):
    AUDIOVISUAL = "audiovisual"
    BLOG = "blog"
    PODCAST = "podcast"
    REPOSITORIO = "repositório"


class CourseType(str, Enum):
    ONLINE = "online"
    PRESENCIAL = "presencial"


class SocialMedia(str, Enum):
    TWITTER = "twitter"
    FACEBOOK = "facebook"
    INSTAGRAM = "instagram"
    YOUTUBE = "youtube"
    LINKEDIN = "linkedin"
    EMAIL = "email"
    TELEGRAM = "telegram"
