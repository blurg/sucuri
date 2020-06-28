from enum import Enum


class MediaType(Enum):
    AUDIOVISUAL = 'audiovisual'
    BLOG = 'blog'
    PODCAST = 'podcast'
    REPOSITORIO = 'repositório'


class CourseType(Enum):
    ONLINE = 'online'
    PRESENCIAL = 'presencial'


class SocialMedia(Enum):
    TWITTER = 'twitter'
    FACEBOOK = 'facebook'
    INSTAGRAM = 'instagram'
    YOUTUBE = 'youtube'
    LINKEDIN = 'linkedin'
    EMAIL = 'email'
    TELEGRAM = 'telegram'
