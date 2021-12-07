import os

timezone = 'UTC'

broker_url_default = 'redis://localhost:6379'
broker_url = os.getenv('BROKER_URL', broker_url_default)
result_backend_default = broker_url
result_backend = os.getenv('RESULT_BACKEND', result_backend_default)
