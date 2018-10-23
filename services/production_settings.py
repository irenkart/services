from .settings import *


ALLOWED_HOSTS = ['live-code.pp.ua']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'services',
        'USER': 'user_services',
        'PASSWORD': '407mQcVfN5MeTN',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}