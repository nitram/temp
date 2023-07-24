from .base import *

DEBUG = False

ALLOWED_HOSTS = ["18.222.116.197"]

try:
    from .local import *
except ImportError:
    pass
