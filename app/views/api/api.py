from flask import Blueprint, render_template, request
from app.functions import db_functions
from app.functions.api_functions import api_json

bp = Blueprint("api", __name__, url_prefix="/api")

@bp.route("/")
def api_home():
    return render_template("api_index.html")

@bp.route("/test")
def api_test():
    return render_template("api_index.html", api_results=api_json({"Test": True}))