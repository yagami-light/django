"""
Django settings for djangoboard project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.core.urlresolvers import reverse_lazy
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '56^fqo!8fstlk!+tgyp-c4_x0wq$g6(o6ppiqo33ip9$eppz2q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'accounts',
    'boards',
    'captcha',
    'registration',
    'django_google_maps',
    'oauth2_provider',
        
    'social_django', 
     'debug_toolbar',
     'django_otp',
         'django_otp.plugins.otp_static',
             'django_otp.plugins.otp_totp',
                 'two_factor',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
     'social_django.middleware.SocialAuthExceptionMiddleware',
         'debug_toolbar.middleware.DebugToolbarMiddleware',
         'django.contrib.auth.middleware.AuthenticationMiddleware',
             'django_otp.middleware.OTPMiddleware'
]

ROOT_URLCONF = 'djangoboard.urls'


AUTHENTICATION_BACKENDS = (
            'social_core.backends.github.GithubOAuth2',
                'social_core.backends.twitter.TwitterOAuth',
                    'social_core.backends.facebook.FacebookOAuth2',
                    'social_core.backends.google.GoogleOAuth2',
                        'django.contrib.auth.backends.ModelBackend',
                        )

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',


                'social_django.context_processors.backends',  # <--
                                'social_django.context_processors.login_redirect',
            ],
        },
    },
]
RECAPTCHA_PUBLIC_KEY='6Lfn0jsUAAAAABoDrjvHv_LxvqvZWjUesyTYx30_'
RECAPTCHA_PRIVATE_KEY='6Lfn0jsUAAAAAADxFTcVm9uzLngaFjFwJh5jEXyT'
WSGI_APPLICATION = 'djangoboard.wsgi.application'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.yahoo.com'
EMAIL_HOST_USER = 'myname@yahoo.com'
EMAIL_HOST_PASSWORD = 'mypassword'
EMAIL_PORT = 587
ACCOUNT_ACTIVATION_DAYS=2
GOOGLE_MAPS_API_KEY='AIzaSyDNnOQ_4IsxjlyR4mYuRkl6H3WOUNuJ_eg'
SOCIAL_AUTH_FACEBOOK_KEY='544177532592299'
SOCIAL_AUTH_FACEBOOK_SECRET='78c910fcb5ca049f0c258d973f0304ee'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY='68940993973-34vg0uufitic6rd3sgj5m53udreipvh2.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET='YKszjRXAhD4vC1DlYgnwOE1D'
GOOGLE_ANALYTICS_MODEL = True
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
NOCAPTCHA = True
#LOGOUT_REDIRECT_URL = 'home'
#LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'two_factor:login'
LOGIN_REDIRECT_URL = 'two_factor:profile'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
