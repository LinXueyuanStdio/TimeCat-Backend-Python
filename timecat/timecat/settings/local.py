from .base import *

SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='pxr%7o=ng&vi$h$*^$%y$*r5n&8hm3$@#-y!9j70xh&&^5)3bv'
)

DEBUG = env.bool('DJANGO_DEBUG', default=True)

CORS_ORIGIN_ALLOW_ALL = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

# REST_FRAMEWORK['HIDE_DOCS'] = True

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'accountbook',
        'USER': 'root',
        'PASSWORD': '122425lxy',
        'HOST': '127.0.0.1'
    }
}