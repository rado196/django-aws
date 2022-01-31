from dotenv import load_dotenv as load_dotEnvConfigs
from os import environ, path

path_root = path.dirname(path.realpath(__file__))
path_env = path.join(path_root, '.env')

load_dotEnvConfigs(path_env)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': environ.get('DB_DATABASE'),
        'USER': environ.get('DB_USERNAME'),
        'PASSWORD': environ.get('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
