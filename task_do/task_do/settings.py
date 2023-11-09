# -*- coding: utf-8 -*-
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-*qucb$c2x-lb=u%u$@lzi3#0mjon4be==$ax0joqfr^9v*-mj!'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'django_redis',
    'captcha',
    'bblist',
    'easy_thumbnails',
    'debug_toolbar',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'task_do.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'bblist.context_processors.user_groups',
            ],
        },
    },
]

WSGI_APPLICATION = 'task_do.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Asia/Almaty'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

THUMBNAIL_ALIASES = {
    '': {
        'small': {'size': (100, 100), 'crop': True},
        'medium': {'size': (300, 200)},
    },
}

CRITICAL = 50
INFO = 25
MY_CUSTOM_LEVEL = 30

MESSAGE_TAGS = {
    CRITICAL: 'critical',
    INFO: 'info',
    MY_CUSTOM_LEVEL: 'my-custom-level',
}

LOGGING_DIR = Path(BASE_DIR) / 'logs'
LOGGING_DIR.mkdir(parents=True, exist_ok=True)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file_debug': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOGGING_DIR / 'debug.log',
        },
        'file_info': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': LOGGING_DIR / 'info.log',
        },
        'file_custom': {
            'level': MY_CUSTOM_LEVEL,
            'class': 'logging.FileHandler',
            'filename': LOGGING_DIR / 'custom.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file_debug', 'file_info'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'custom_logger': {
            'handlers': ['file_custom'],
            'level': MY_CUSTOM_LEVEL,
            'propagate': True,
        },
    },
}

LOGOUT_REDIRECT_URL = 'task_list'
LOGIN_REDIRECT_URL = 'task_list'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',  # Укажите адрес и порт вашего Redis-сервера
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

if DEBUG:
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    INTERNAL_IPS = ['127.0.0.1', 'localhost']
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG,
}
CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:5500',
    'http://localhost:5500',
]
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
