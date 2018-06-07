import os

HERE = os.path.abspath(os.path.dirname(__file__))
DEBUG = False
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:test@mysql:3306/test?charset=utf8mb4'  # noqa
SQLALCHEMY_TRACK_MODIFICATIONS = False

