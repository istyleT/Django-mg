"""
Django settings for webappmg project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
from pathlib import Path
import os 
from os import environ
import dj_database_url
import django_on_heroku

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['djwebappmg-version1.herokuapp.com']

LOGIN_URL = "auth/login"

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sellmg',
    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'webappmg.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'webappmg.wsgi.application'

DATABASES = {
    
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,  'db.sqlite3'),
    }
}

DATABASES['default'] = dj_database_url.config(default='postgres://igoizeksefnzes:edb1aef7f7cd24cf56e028f62da3d94c6c694c818650f7217e6565f75fd70001@ec2-44-195-132-31.compute-1.amazonaws.com:5432/denegok7gstlh9')

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS =[os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

django_on_heroku.settings(locals())

## Build paths inside the project like this: BASE_DIR / 'subdir'.
## Quick-start development settings - unsuitable for production
## See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/
## SECURITY WARNING: keep the secret key used in production secret
## SECURITY WARNING: don't run with debug turned on in production!
## Default primary key field type
## https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases



################## Test settings ############
#from pathlib import Path
#import os 
#from os import environ
#BASE_DIR = Path(__file__).resolve().parent.parent
#SECRET_KEY = '*'
#DEBUG = True
#ALLOWED_HOSTS = ['127.0.0.1']
#LOGIN_URL = "auth/login"
#INSTALLED_APPS = [
#    'django.contrib.admin',
#    'django.contrib.auth',
#    'django.contrib.contenttypes',
#    'django.contrib.sessions',
#    'django.contrib.messages',
#    'django.contrib.staticfiles',
#    'sellmg',
#    
#    
#]
#
#MIDDLEWARE = [
#    'django.middleware.security.SecurityMiddleware',
#    'whitenoise.middleware.WhiteNoiseMiddleware',
#    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.messages.middleware.MessageMiddleware',
#    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#]
#
#ROOT_URLCONF = 'webappmg.urls'
#
#TEMPLATES = [
#    {
#        'BACKEND': 'django.template.backends.django.DjangoTemplates',
#        'DIRS': [os.path.join(BASE_DIR, 'templates')],
#        'APP_DIRS': True,
#        'OPTIONS': {
#            'context_processors': [
#                'django.template.context_processors.debug',
#                'django.template.context_processors.request',
#                'django.contrib.auth.context_processors.auth',
#                'django.contrib.messages.context_processors.messages',
#            ],
#        },
#    },
#]
#
#WSGI_APPLICATION = 'webappmg.wsgi.application'
#
#DATABASES = {
#    
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR,  'db.sqlite3'),
#    }
#}
#
#AUTH_PASSWORD_VALIDATORS = [
#    {
#        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#    },
#]
#
#LANGUAGE_CODE = 'en-us'
#TIME_ZONE = 'UTC'
#USE_I18N = True
#USE_TZ = True
#
#STATIC_URL = '/static/'
#STATICFILES_DIRS =[os.path.join(BASE_DIR, 'static')]
#STATIC_ROOT = BASE_DIR / 'staticfiles'
#
#DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'