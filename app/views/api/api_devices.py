from flask import Blueprint, render_template, request, jsonify
from app.functions import db_functions, netmiko_functions
from app.functions.api_functions import api_json

bp = Blueprint("api_devices", __name__, url_prefix="/api/devices")

@bp.route("/")
def api_devices():
    content_type = request.headers.get('Content-Type')

    if request.method == "POST":
        pass

    devices = db_functions.db_get_devices()

    if content_type == "application/json":
        return jsonify(devices)

    return render_template("api_index.html", api_results=api_json(devices))

@bp.route("/<int:id>")
def api_devices_id(id):
    content_type = request.headers.get('Content-Type')

    if request.method == "POST":
        pass

    device = db_functions.db_get_device(id)

    if content_type == "application/json":
        return jsonify(device)

    return render_template("api_index.html", api_results=api_json(device))

@bp.route("/<int:id>/show_version", methods=['GET','POST'])
def api_devices_show_version(id):
    content_type = request.headers.get('Content-Type')

    device = db_functions.db_get_device(id)

    if request.method == "POST":
        session = netmiko_functions.NetmikoAPI(device)
        show_version = db_functions.db_add_device_software_facts(**session.show_version())
        return jsonify(show_version)

    elif request.method == "PATCH":
        session = netmiko_functions.NetmikoAPI(device)
        show_version = db_functions.db_update_device_software_facts(device, **session.show_version())
        return jsonify(show_version)

    device_software_facts = db_functions.db_get_device_software_facts(id)

    if content_type == "application/json":
        return jsonify(device_software_facts)
    
    return render_template("api_index.html", api_results=api_json(device_software_facts))

@bp.route("/<int:id>/show_interfaces", methods=['GET','POST'])
def api_devices_show_interface(id):
    content_type = request.headers.get('Content-Type')

    device = db_functions.db_get_device(id)

    if request.method == "POST":
        session = netmiko_functions.NetmikoAPI(device)
        show_interfaces = db_functions.db_add_device_interface_facts(id, session.show_interfaces())
        return jsonify(show_interfaces)
    elif request.method == "PATCH":
        session = netmiko_functions.NetmikoAPI(device)
        show_interfaces = db_functions.db_update_device_interface_facts(device, session.show_interfaces())
        return jsonify(show_interfaces)

    device_interface_facts = db_functions.db_get_device_interface_facts(id)

    if content_type == "application/json":
        return jsonify(device_interface_facts)
    
    return render_template("api_index.html", api_results=api_json(device_interface_facts))
