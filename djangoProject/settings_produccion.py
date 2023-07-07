import dj_database_url
import os

from djangoProject.settings import *

# SECRET KEY
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag')

# DEBUG
DEBUG = False if os.environ.get('DJANGO_DEBUG') == 'False' else True

# DATABASE
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# MIDDLEWARE Whitenoise
# obteniendo index de SecurityMiddleware
indexSecurityMiddleware = [i for i, e in enumerate(MIDDLEWARE) if e == 'django.middleware.security.SecurityMiddleware'][
    0]
# Insertando Whitenoise Middleware una posicion despues de SecurityMiddleware
MIDDLEWARE.insert(indexSecurityMiddleware + 1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# File Compressor
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ALLOWED HOSTS
ALLOWED_HOSTS = ['*']

# CORS
CORS_ORIGIN_ALLOW_ALL = True
