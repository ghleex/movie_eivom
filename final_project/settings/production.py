from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = []

import django_heroku
django_heroku.settings(locals())
