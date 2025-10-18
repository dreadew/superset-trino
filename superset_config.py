# Superset configuration file
import os

SECRET_KEY = os.getenv('SUPERSET_SECRET_KEY', 'change-this-to-a-long-random-string')

SQLALCHEMY_DATABASE_URI = os.getenv(
    'SUPERSET_DATABASE_URI',
    'postgresql+psycopg2://superset:superset@postgres:5432/superset'
)

REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)

# Cache configuration
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_HOST': REDIS_HOST,
    'CACHE_REDIS_PORT': REDIS_PORT,
}

DATA_CACHE_CONFIG = CACHE_CONFIG

RATELIMIT_STORAGE_URI = f'redis://{REDIS_HOST}:{REDIS_PORT}/1'

class CeleryConfig:
    broker_url = f'redis://{REDIS_HOST}:{REDIS_PORT}/0'
    result_backend = f'redis://{REDIS_HOST}:{REDIS_PORT}/0'

CELERY_CONFIG = CeleryConfig

FEATURE_FLAGS = {
    'ALERT_REPORTS': True,
    'DASHBOARD_NATIVE_FILTERS': True,
    'DASHBOARD_CROSS_FILTERS': True,
    'DASHBOARD_RBAC': True,
    'EMBEDDABLE_CHARTS': True,
    'ENABLE_TEMPLATE_PROCESSING': True,
}

SUPERSET_WEBSERVER_TIMEOUT = 300

UPLOAD_FOLDER = '/app/superset_home/uploads/'
ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'xls'}

SUPERSET_WEBSERVER_TIMEOUT = 300
SQLLAB_TIMEOUT = 300
SQLLAB_ASYNC_TIME_LIMIT_SEC = 300

ENABLE_SCHEDULED_EMAIL_REPORTS = True

SQLALCHEMY_POOL_SIZE = 5
SQLALCHEMY_POOL_TIMEOUT = 300
SQLALCHEMY_MAX_OVERFLOW = 10
SQLALCHEMY_POOL_PRE_PING = True

HIVE_POLL_INTERVAL = 5
