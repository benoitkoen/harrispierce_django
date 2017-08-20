from os import environ


class Config:
    db_user = environ.get('DB_USER', 'postgres')
    db_name = environ.get('DB_NAME', 'postgres')
    db_host = environ.get('DB_HOST', '')
    db_password = environ.get('DB_USER', '')
    db_port = environ.get('DB_PORT', '')

    secret_key = environ.get('SECRET_KEY', 'fake_secret_key')