import os
# import requests
from pathlib import Path


# def is_ec2_linux():
#     """Detect if we're running on an EC2 Linux Instance
#     See http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/identify_ec2_instances.html
#     """
#     if os.path.isfile("/sys/hypervisor/uuid"):
#         with open("/sys/hypervisor/uuid") as f:
#             uuid = f.read()
#             return uuid.startswith("ec2")
#     return False

# def get_token():
#     """See the authorization token to live for 6 hours (maximun)"""
#     headers = {
#         'X-aws-ec2-metadata-token-ttl-seconds': '21600',
#     }
#     response = requests.put('http://169.254.169.254/latest/api/token', headers=headers)
#     return response.text

# def get_linux_ec2_private_ip():
#     """Get the private IP Address of the machine if running on a ec2 Linux server
#         See https://docs.aws.amazon.com/AWSEC2/ltest/UserGuide/instancedata-data-retrieval.html
#     """
#     if not is_ec2_linux():
#         return None
#     try:
#         token = get_token()
#         headers = {
#             'X-aws-ec2-metadata-token': f"{token}",
#         }
#         response = requests.get('http://169.254.169.254/latest/meta-data/local-ipv4', headers=headers)
#         return response.text
#     except:
#         return None
#     finally:
#         if response:
#             response.close()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'nationwidemovers.ap-southeast-2.elasticbeanstalk.com',
    'www.nationwidemovers.com.au',
    'nationwidemovers.com.au',
]
# private_ip = get_linux_ec2_private_ip()
# if private_ip:
#     ALLOWED_HOSTS.append(private_ip)


# Application definition

INSTALLED_APPS = [
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local
    'clients',
    'services',
    'inventory',
    'vehicles',
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

ROOT_URLCONF = 'NRProject.urls'

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

WSGI_APPLICATION = 'NRProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

if 'RDS_DB_NAME' in os.environ:
  DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.postgresql',
      'NAME': os.environ['RDS_DB_NAME'],
      'USER': os.environ['RDS_USERNAME'],
      'PASSWORD': os.environ['RDS_PASSWORD'],
      'HOST': os.environ['RDS_HOSTNAME'],
      'PORT': os.environ['RDS_PORT']
    },
}
else:
  DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '5432'
      },
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']

# Email conf
EMAIL_HOST = os.environ['NWM_EMAIL_HOST']
EMAIL_PORT = os.environ['NWM_EMAIL_PORT']
EMAIL_HOST_USER = os.environ['NWM_EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['NWM_EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

# Security
# SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
# SECURE_HSTS_SECONDS = 1800
# SECURE_HSTS_PRELOAD = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
