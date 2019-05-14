import os
basedir = os.path.abspath(os.path.dirname(__file__))

MAINTENANCE = False
FLASK_ADMIN_SWATCH = 'cerulean'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACE_MODIFICATIONS = False
WTF_CSRF_ENABLED = True
SECRET_KEY = 'boojei'
