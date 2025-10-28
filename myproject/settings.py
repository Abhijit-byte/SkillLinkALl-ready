"""
Django settings for myproject project.
"""

from pathlib import Path
import os
import dj_database_url

# -------------------------------------------------------------------
# 📂 PATHS
# -------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent


# -------------------------------------------------------------------
# 🔐 SECURITY SETTINGS
# -------------------------------------------------------------------

SECRET_KEY = os.environ.get(
    'SECRET_KEY', 'django-insecure-+x#+u=y-$=gny9o6m!!@_9grwnj^cz$#3h9kmh)uk=8!-!owk+'
)

# Detect if running on Railway
RAILWAY_ENV = os.environ.get('RAILWAY_ENVIRONMENT', None)

if RAILWAY_ENV:
    DEBUG = False
    ALLOWED_HOSTS = ['railway.app', '.up.railway.app']
else:
    DEBUG = True
    ALLOWED_HOSTS = []


# -------------------------------------------------------------------
# 🧩 INSTALLED APPS
# -------------------------------------------------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'rest_framework',
    'corsheaders',

    # Local apps
    'myapp',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}


# -------------------------------------------------------------------
# ⚙️ MIDDLEWARE
# -------------------------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',        # Allow frontend access
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# -------------------------------------------------------------------
# 📁 URLS / WSGI
# -------------------------------------------------------------------

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'myproject.wsgi.application'


# -------------------------------------------------------------------
# 🗄️ DATABASE CONFIG
# -------------------------------------------------------------------

# Your Railway PostgreSQL database URL
DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://postgres:PGqnDugiHkCSYyWEBLlPSLpZwvurvfVm@postgres.railway.internal:5432/railway"
)

DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600)
}


# -------------------------------------------------------------------
# 🔐 PASSWORD VALIDATION
# -------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# -------------------------------------------------------------------
# 🌍 INTERNATIONALIZATION
# -------------------------------------------------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# -------------------------------------------------------------------
# 🖼️ STATIC FILES
# -------------------------------------------------------------------

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# -------------------------------------------------------------------
# 🔑 DEFAULT PRIMARY KEY FIELD TYPE
# -------------------------------------------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# -------------------------------------------------------------------
# 🌐 CORS (Frontend access)
# -------------------------------------------------------------------

CORS_ALLOW_ALL_ORIGINS = True
