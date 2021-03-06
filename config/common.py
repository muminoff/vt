import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'bao&&m9(6iiv_*73yl0@j+y_0j^-4c@z&7jw(m6r#pp+20^ipc'
ALLOWED_HOSTS = ['*']

BASE_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
    'core',
)

THIRD_PARTY_APPS = (
    'rest_framework',
    'pipeline',
)

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    # 'pipeline.middleware.MinifyHTMLMiddleware',
)

ROOT_URLCONF = 'vt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'deploy.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vt',
        'USER': 'vt',
        'PASSWORD': 'vt',
    }
}


LANGUAGE_CODE = 'en-us' 
TIME_ZONE = 'UTC' 
USE_I18N = True 
USE_L10N = True 
USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'staticfiles')
STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
        )

STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'pipeline.finders.PipelineFinder',
        )

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'vt.context_processors.navbar',
            ],
        },
    },
]

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.jsmin.JSMinCompressor'
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
PIPELINE_VERSIONING = 'pipeline.versioning.hash.MD5Versioning'
PIPELINE_ENABLED = True
PIPELINE_AUTO = True
PIPELINE_VERSION = True

PIPELINE_CSS = {
        'bootstrap': {
            'source_filenames': (
                'css/bootstrap.css',
                ),
            'output_filename': 'css/bootstrap.min.css',
            },
        'bootstrap-tweaks': {
            'source_filenames': (
                'css/bootstrap-tweaks.css',
                ),
            'output_filename': 'css/bootstrap-tweaks.min.css',
            },
        'prettify': {
            'source_filenames': (
                'css/prettify.css',
                ),
            'output_filename': 'css/prettify.min.css',
            },
        'default': {
            'source_filenames': (
                'css/default.css',
                ),
            'output_filename': 'css/default.min.css',
            },
    }

PIPELINE_JS = {
        'jquery': {
            'source_filenames': (
                'js/jquery.js',
            ),
            'output_filename': 'js/jquery.min.js',
        },
        'bootstrap': {
            'source_filenames': (
                'js/bootstrap.js',
            ),
            'output_filename': 'js/bootstrap.min.js',
        },
        'prettify': {
            'source_filenames': (
                'js/prettify.js',
            ),
            'output_filename': 'js/prettify.min.js',
        },
        'default': {
            'source_filenames': (
                'js/default.js',
            ),
            'output_filename': 'js/default.min.js',
        },
    }

REST_FRAMEWORK = {
    'PAGINATE_BY': 100,
    'PAGINATE_BY_PARAM': 'page_size',
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_xml.renderers.XMLRenderer',
        'rest_framework_yaml.renderers.YAMLRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FormParser',
        'rest_framework_yaml.parsers.YAMLParser',
        'rest_framework_xml.parsers.XMLParser',
    )
}
