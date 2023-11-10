

from pathlib import Path
from decouple import Csv,config
import os
BASE_DIR = Path(__file__).resolve().parent.parent





SECRET_KEY = config('SECRET_KEY')


DEBUG = bool(int(config('DEBUG', 0)))

ALLOWED_HOSTS = []


'''
    DEFINIÇÃO DE APPS MULTI-TENANTS
        - SHARED_APPS
            são todos os apps que servem como configuradores do django e do aplicativo principal (host principal)
        
        - TENANT_APPS
            todos os apps que estaram disponiveis para os tenants(Inquilinos)
            por exemplo para que a authenticação funcione tambem nos tenants, temos que definilos nos no SHARED_APPS e no TENTAN_APPS
'''
   

SHARED_APPS = (
    'django_tenants',
    'TenantClient',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
)

TENANT_APPS = (
    'django.contrib.auth',
    'TenantClient'
)

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]


TENANT_MODEL = "TenantClient.Client"

TENANT_DOMAIN_MODEL = "TenantClient.Domain"

SITE_ID = 1


'''
    MIDDLEWARE
        O middleware (django_tenants.middleware.main.TenantMainMiddleware) e o responsavel por redirecionar a solicitação para o schema correto.
        
'''   


MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


PUBLIC_SCHEMA_URLCONF = 'djangoTenants.urls_public'

ROOT_URLCONF = 'djangoTenants.urls'





TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoTenants.wsgi.application'








 
'''
    DATABASE
        Para que o django possa manipular o postgress para criar os schemas dos inquilinos,
        deve-se usar o django_tenants.postgresql_backend como engine default.
'''   


DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('POSTGRES_HOST'),
        'PORT': config('POSTGRES_PORT')
    }
}


DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)



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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
