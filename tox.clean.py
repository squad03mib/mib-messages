import os

try:
    os.remove('swagger_server/:memory')
except Exception:
    pass