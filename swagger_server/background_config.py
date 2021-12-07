import os

broker_url = 'redis://localhost:6379'
result_backend = broker_url
timezone = 'UTC'

flask_env = os.getenv('FLASK_ENV', 'None')
if flask_env == 'production':
    broker_url = os.getenv('BROKER_URL', 'None')
    result_backend = os.getenv('RESULT_BACKEND', 'None')