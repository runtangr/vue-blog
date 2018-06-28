import os

HERE = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:test@localhost/test?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = False


try:
    from local_set import * 
except ImportError:
    pass

