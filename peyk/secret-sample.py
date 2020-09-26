import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wmwad(-fhdzc9_ce%(+h=-5r*7(m8^lpks%+3#a&t-zu^z$id$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}