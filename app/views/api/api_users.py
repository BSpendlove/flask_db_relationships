from flask import Blueprint, render_template, request, jsonify
from app.functions import db_functions
from app.functions.api_functions import api_json

bp = Blueprint("api_users", __name__, url_prefix="/api/users")

@bp.route("/")
def api_users():
    content_type = request.headers.get('Content-Type')

    if request.method == "POST":
        pass

    users = db_functions.db_get_users()

    if content_type == "application/json":
        return jsonify(users)

    return render_template("api_index.html", api_results=api_json(users))

@bp.route("/<int:id>")
def api_users_id(id):
    content_type = request.headers.get('Content-Type')

    if request.method == "POST":
        pass

    user = db_functions.db_get_user(id)

    if content_type == "application/json":
        return jsonify(user)

    return render_template("api_index.html", api_results=api_json(user))