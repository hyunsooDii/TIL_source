"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.0.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 현재 디렉토리를 패키지 안에서 찾는 명령어 BASE_DIR에 저장

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p)tb=jytn11_l1(_odsclj--&oj9m+xu0vp^_)g#y2ve&kp-f6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.0.18','127.0.0.1','localhost'] # 웹서버의 호스트 - 어떤 웹서버한테만 지원할거냐 리스트를 비워두면 모두다


# Application definition

# INSTALLED_APPS = 기능을 추가할 때 쓰는 List

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth', # 로그인 로그아웃, PW변경 등 제공
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'taggit.apps.TaggitAppConfig',
    'taggit_templatetags2',

    'widget_tweaks',
    'tinymce',

    'bookmark.apps.BookmarkConfig',
    'blog.apps.BlogConfig',
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

ROOT_URLCONF = 'mysite.urls' # URL 패턴을 어떻게 운영할거냐, 계층화(Tree 구조)시켜서 운영함
# __init__ 파일이 있는 폴더  = package , mysite는 패키지, 그 밑에 있는 파일들은 모듈 
# mysite.urls mysite 패키지에 있는 urls 모듈

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES =  { # 제일 중요함 DB랑 user를 먼저 생성 후 써야됨
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': 'django_ex_db', # 데이터베이스 명
'HOST': 'localhost', # 서버 IP
'PORT': '3306', # 포트번호
'USER': 'webuser', # 사용자 ID
'PASSWORD': '1234' # 비밀번호
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # 현재 프로젝트 안에 media

TAGGIT_CASE_INSENSITIVE = True
TAGGIT_LIMIT = 50

LOGOUT_REDIRECT_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'