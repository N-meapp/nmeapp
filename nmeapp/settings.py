"""
Django settings for nmeapp project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
import environ

env = environ.Env(
    DEBUG=(bool, False)
)

# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Read the .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-52da-#m3+q2qlp_9k48dm$#$ue_@^1du(v+)-d*t9br8wu)@dz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')


ALLOWED_HOSTS = ['nmeapp.in', 'www.nmeapp.in']
# ALLOWED_HOSTS = []



CSRF_TRUSTED_ORIGINS = [
        'http://nmeapp.in',
        'https://nmeapp.in'  # Add both HTTP and HTTPS if using SSL
        ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'django.contrib.sitemaps',
    'cloudinary',
    'cloudinary_storage',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nmeapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'blog/templates'],
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

WSGI_APPLICATION = 'nmeapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# STATIC_URL = '/static/'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),  
# ]

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # <-- Add this

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import cloudinary
import cloudinary.uploader
import cloudinary.api

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dd6caczi8',
    'API_KEY': '718852635219182',
    'API_SECRET': 'GGpwQtxxbSiIAHuV0bOVX9mQ6JA',
}

cloudinary.config( 
    cloud_name = CLOUDINARY_STORAGE['CLOUD_NAME'],  
    api_key = CLOUDINARY_STORAGE['API_KEY'],  
    api_secret = CLOUDINARY_STORAGE['API_SECRET']
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
