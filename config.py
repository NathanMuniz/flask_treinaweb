DEBUG = True
USERNAME = 'root'
PASSWORD = 'root'
SEVER = 'localhost'
DB = 'flask_fundamentos'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SEVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True