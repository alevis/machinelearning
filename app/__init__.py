from flask import Flask
from flask_admin import Admin
from flask_bower import Bower
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
Bower(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

admin = Admin(app,name="Kanime",template_mode='bootstrap3')

import views, models
