from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

Bootstrap(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.views.api import api, api_users, api_devices
from app.views import devices as devices_routes
from app.views import users as users_routes

from app import models

@app.route("/")
def index():
    return render_template("index.html")

app.register_blueprint(api.bp)
app.register_blueprint(api_users.bp)
app.register_blueprint(api_devices.bp)
app.register_blueprint(devices_routes.bp)
app.register_blueprint(users_routes.bp)
