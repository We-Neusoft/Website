"""
Django settings for empty project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'WE_CLOUD'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['.we.neusoft.edu.cn']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.www',
    'apps.mirror',
    'apps.genuine',
    'apps.file',
    'apps.iptv',
    'apps.open',

    'backdoors.referer',

    'common',

    # 'auth',
    # 'download',
    # 'me',

    #'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'we.middleware.adapter.AdapterMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
)

ROOT_URLCONF = 'we.urls'

WSGI_APPLICATION = 'we.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'WE_CLOUD',
        'NAME': 'WE_CLOUD',
        'USER': 'WE_CLOUD',
    }
}


# Caching
# https://docs.djangoproject.com/en/1.6/topics/cache/

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'memcache:11211',
        'KEY_PREFIX': 'we_dev',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


STATIC_URL = '/static/'

STATIC_ROOT = '/root/we/'

STATICFILES_DIRS = (
    '/root/we/we/static',
)


# Session
# https://docs.djangoproject.com/en/1.6/topics/http/sessions/

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

SESSION_COOKIE_DOMAIN = 'dev.we.neusoft.edu.cn'

SESSION_COOKIE_NAME = 'we'


# 1.3 Style
ADMINS = (
    ('Fulong Sun', 'sunfulong@nou.com.cn'),
)

EMAIL_HOST = 'mail.nou.com.cn'

EMAIL_HOST_USER = 'we@nou.com.cn'

EMAIL_HOST_PASSWORD = 'WE_CLOUD'

SERVER_EMAIL = 'we@nou.com.cn'


EMAIL_SUBJECT_PREFIX = '[We] '


TEMPLATE_DIRS = (
    '/root/we/we/templates',
)


DREAMSPARK_ACCOUNT = 'WE_CLOUD'
DREAMSPARK_KEY = 'WE_CLOUD'
DREAMSPARK_OPEN_REDIRECT_URI = 'http://dev.we.neusoft.edu.cn/genuine/iuv.we'


DATA_ROOT = '/data/www/source/'
FILE_ROOT = '/var/www/file.we.neusoft.edu.cn/htdocs/'

OPEN_CLIENT_ID = 'WE_CLOUD'
OPEN_CLIENT_SECRET = 'WE_CLOUD'

OPEN_SERVER_DOMAIN = 'http://dev.hub.neusoft.edu.cn'
OPEN_SERVER_AUTHORIZE = OPEN_SERVER_DOMAIN + '/oauth/authorize'
OPEN_SERVER_TOKEN = OPEN_SERVER_DOMAIN + '/oauth/token'
OPEN_SERVER_USER_GET_INFO = OPEN_SERVER_DOMAIN + '/user/get_info'
OPEN_SERVER_USER_GET_PRIVACY = OPEN_SERVER_DOMAIN + '/user/get_privacy'
