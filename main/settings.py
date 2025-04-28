from pathlib import Path
from datetime import timedelta
import os
# from decouple import config


# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# Core settings
SECRET_KEY = 'django-insecure-b2x2y^vs%3h84pn36jzh!cwpn9(s!%of70$z2&x08fo1atc1u!'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'shadow71.com', 'www.shadow71.com']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    # Third-party apps
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth', 
    'dj_rest_auth.registration',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    # Local apps
    'catalg',
    'accounts',
]

ACCOUNT_ADAPTER = 'accounts.adapters.CustomAccountAdapter'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'main.urls'

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

# WSGI_APPLICATION = 'main.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'  # URL prefix for static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Where collected static files go
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Where your static files are stored
]

# Add WhiteNoise storage (optional but recommended for compression)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication
AUTH_USER_MODEL = 'accounts.CustomUserModel'

# AllAuth settings
SITE_ID = 1
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none' 


# Rest Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication'
    ),
}

# JWT settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=36500),  
    'REFRESH_TOKEN_LIFETIME': timedelta(hours=2), 
}

# Rest Auth settings
REST_AUTH = {
    'USE_JWT': True,
    'REST_USE_JWT' : True,
    'JWT_AUTH_COOKIE': 'access',
    'JWT_AUTH_REFRESH_COOKIE': 'refresh',
    'JWT_AUTH_HTTPONLY': True,
    'SESSION_LOGIN': False,
    'OLD_PASSWORD_FIELD_ENABLED': True,
}

# CORS settings
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1',
    'http://localhost',
    'http://localhost:3000',
    'https://shadow71.com',
    'https://bindu-britto.com',
    # 'https://official.bindu-britto.com/'
]

CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1',
    'http://localhost',
    'http://localhost:3000'
    # 'https://shadow71.com',
    # 'https://bindu-britto.com',
    # 'https://official.bindu-britto.com/',
]

CSRF_COOKIE_SECURE = False  # Set to True in production (HTTPS only)
CSRF_COOKIE_HTTPONLY = False  # Allow JavaScript to access the CSRF token
CSRF_COOKIE_SAMESITE = 'Lax'  # Set to 'Strict' or 'None' as needed

CORS_ALLOW_CREDENTIALS = True

CORS_URLS_REGEX = r'^/.*$'  # Allow CORS for all URLs

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Replace with your SMTP server
EMAIL_HOST_USER =  'afzalhossen2019@gmail.com'
EMAIL_HOST_PASSWORD = "jvkvlgmmpaaepumv" 
EMAIL_PORT = 587
EMAIL_USE_TLS = True

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'accounts.serializers.CustomRegisterSerializer',
}


REST_AUTH_SERIALIZERS = {
    'PASSWORD_RESET_SERIALIZER': 'dj_rest_auth.serializers.PasswordResetSerializer',
}