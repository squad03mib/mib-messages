import os

timezone = 'UTC'

broker_url_default = 'redis://127.0.0.1:6379'
broker_url = os.getenv('BROKER_URL', broker_url_default)
