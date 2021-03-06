from path import path


BASE_DIR = path(__file__).parent.parent.abspath()

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = dict(
    default=dict(
        ENGINE='django.db.backends.sqlite3',
        NAME='example.db',
        USER='',
        PASSWORD='',
        HOST='',
        PORT='',
    )
)

INSTALLED_APPS = [
    # Project app
    'django_file_form_example',

    # Generic apps
    'django_file_form',
    'django_file_form.ajaxuploader',
    'django_bootstrap3_form',
    'django_pony_forms',

    # Django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
]

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

STATIC_URL = '/static/'
ROOT_URLCONF = 'testproject.urls'

STATIC_ROOT = BASE_DIR.joinpath('static')

MEDIA_ROOT = BASE_DIR.joinpath('media')
MEDIA_ROOT.mkdir_p()
MEDIA_ROOT.joinpath('example').mkdir_p()
MEDIA_ROOT.joinpath('temp_uploads').mkdir_p()

USE_TZ = True
