import os
import json
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

with open(os.path.join(BASE_DIR, 'secrets.json')) as secrets_file:
    secrets = json.load(secrets_file)


def get_secret(setting, secrets_in=secrets):
    """Get secret setting or fail with ImproperlyConfigured"""
    try:
        return secrets_in[setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {} setting".format(setting))


DJANGO_MODULE_STR = get_secret('DJANGO_MODULE_STR')

if DJANGO_MODULE_STR == 'development':
    from .development import *
else:
    from .production import *
