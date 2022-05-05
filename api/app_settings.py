import os
from distutils.util import strtobool


class Config(object):
    SECRET_KEY = os.environ.get('APP_SECRET_KEY')

    MONGO_HOST = os.environ.get('MONGO_HOST', 'mongo')
    MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'light')
    MONGO_USER = os.environ.get('MONGO_USER', '')
    MONGO_PASS = os.environ.get('MONGO_PASS', '')
    MONGO_RSNAME = os.environ.get('MONGO_RSNAME', '')
    
    use_mgo_atlas = MONGO_HOST.startswith('mongodb+srv://')
    mongo_uri_params = []
    if not MONGO_USER:
        MONGO_URI = f'mongodb://{MONGO_HOST}/{MONGO_DBNAME}'
    elif use_mgo_atlas:
        mongo_uri_params += ['retryWrites=true', 'w=majority']
        MONGO_HOST = MONGO_HOST[14:]
        MONGO_URI = f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}/{MONGO_DBNAME}"
    else:
        mongo_uri_params.append('authSource=admin')
        MONGO_URI = f'mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}/{MONGO_DBNAME}'

    if not use_mgo_atlas and MONGO_RSNAME:
        mongo_uri_params.append(f'replicaSet={MONGO_RSNAME}')

    MONGO_URI += '?' + '&'.join(mongo_uri_params)

    REDIS_URL = 'redis://:{}@{}:6379/0'.format(
        os.environ.get('REDIS_PASSWORD', ''),
        os.environ.get('REDIS_HOST', 'redis'))

    _redis_url = 'redis://:{}@{}:6379/0'.format(
        os.environ.get('REDIS_PASSWORD', ''),
        os.environ.get('REDIS_HOST', 'redis'))

    BROKER_URL = _redis_url

    CELERY_RESULT_BACKEND = _redis_url
    CELERY_TIMEZONE = 'Asia/Seoul'
    CELERY_ALWAYS_EAGER = strtobool(os.environ.get('CELERY_ALWAYS_EAGER', 'false'))
    CELERY_ENABLE_UTC = False


class ConfigDebug(Config):
    SECRET_KEY = 'develop secret key'
    DEBUG = True

