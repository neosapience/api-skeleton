import os


def read_secret_key():
    app_secret = os.environ.get('APP_SECRET_KEY')
    if not app_secret:
        with open(os.environ.get('SECRET_KEY_FILE'), 'rt') as f:
            app_secret = f.read()
    if not app_secret:
        raise RuntimeError('cannot read SECRET_KEY_FILE or APP_SECRET_KEY')
    return app_secret


class Config(object):
    SECRET_KEY = read_secret_key()
    MONGO_HOST = os.environ.get('MONGO_HOST', 'mongo')
    MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'appname')
    MONGO_USER = os.environ.get('MONGO_USERNAME', '')
    MONGO_PASS = os.environ.get('MONGO_PASSWORD', '')
    MONGO_RSNAME = os.environ.get('MONGO_RSNAME', '')

    mongo_uri_params = []
    if not MONGO_USER:
        MONGO_URI = f'mongodb://{MONGO_HOST}/{MONGO_DBNAME}'
    else:
        mongo_uri_params.append('authSource=admin')
        MONGO_URI = f'mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}/{MONGO_DBNAME}'

    if MONGO_RSNAME:
        mongo_uri_params.append(f'replicaSet={MONGO_RSNAME}')

    MONGO_URI += '?' + '&'.join(mongo_uri_params)
    _redis_url = 'redis://:{}@{}:6379/0'.format(
        os.environ.get('REDIS_PASSWORD', ''),
        os.environ.get('REDIS_HOST', 'redis'))

    BROKER_URL = _redis_url
    CELERY_RESULT_BACKEND = _redis_url
    CELERY_TIMEZONE = 'Asia/Seoul'


class ConfigDebug(Config):
    SECRET_KEY = 'develop secret key'
    DEBUG = True

