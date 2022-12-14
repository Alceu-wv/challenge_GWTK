"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
import sys
from pathlib import Path

import stringcase
from asbool import asbool
from stela import settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_NAME = stringcase.titlecase(settings["project.name"])
ENV = settings["ENV"]
SERVICE_TYPE = settings["project.service_type"]
SHOW_DJANGO_PAGES = settings["project.show_django_pages"]


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = settings["project.secret_key"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "debug_toolbar",
    "django_celery_beat",
    "django_celery_results",
    "drf_spectacular",
    "rest_framework",
    "main_app.apps.MainAppConfig",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

RUNNING_TESTS = "pytest" in sys.modules or "test" in sys.argv
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "postgres" if RUNNING_TESTS else settings["db.name"],
        "USER": "postgres" if RUNNING_TESTS else settings["db.user"],
        "PASSWORD": "postgres" if RUNNING_TESTS else settings["db.password"],
        "HOST": "db" if RUNNING_TESTS else settings["db.host"],
        "PORT": "5432" if RUNNING_TESTS else settings["db.port"],
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Celery
CELERY_RESULT_BACKEND = "django-db"
CELERY_BROKER_URL = "redis://redis:6379"
CELERY_RESULT_BACKEND = "redis://redis:6379"

if settings["project.broker_type"] == "sqs":
    CELERY_BROKER_TRANSPORT_OPTIONS = {
        "region": settings["project.aws_region"],
        "polling_interval": 3,
        "visibility_timeout": 3600,
        "queue_name_prefix": f"main-app-{ENV}-",
    }


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

# CORS
CORS_ALLOW_ALL_ORIGINS = asbool(settings["project.allow_all_origins"])
CORS_ALLOW_HEADERS = ("content-type", "authorization", "accept", "origin", "user-agent")

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DEBUG = asbool(settings["project.debug"])

ALLOWED_HOSTS = settings["project.allowed_hosts"]
