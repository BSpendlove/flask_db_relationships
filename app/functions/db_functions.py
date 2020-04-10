from app import db
from app.models import (
    User,
    Device,
    DeviceInterfaceFacts,
    DeviceSoftwareFacts
)
from flask import jsonify

def db_add_user(*args, **kwargs):
    user = User(*args, **kwargs)
    db.session.add(user)
    db.session.commit()
    return user

def db_add_device(*args, **kwargs):
    device = Device(*args, **kwargs)
    db.session.add(device)
    db.session.commit()
    return device

"""
def db_add_device_interface_facts(device_id, interface_list):
    return_list = []

    for interface in interface_list:
        interface["device"] = device_id
        for key, value in interface.items():
            if isinstance(value, list):
                interface[key] = str(value)

        device_interface_facts = DeviceInterfaceFacts(**interface)
        return_list.append(device_interface_facts)
        db.session.add(device_interface_facts)

    db.session.commit()
    return return_list

def db_add_device_software_facts(**kwargs):
    for key, value in kwargs.items():
        if isinstance(value, list):
            kwargs[key] = str(value)

    device_software_facts = DeviceSoftwareFacts(**kwargs)
    db.session.add(device_software_facts)
    db.session.commit()
    return device_software_facts

"""

def db_delete_device(id):
    device = db_get_device(id)
    db.session.delete(device)
    db.session.commit()
    return device

def db_delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return user

def db_get_device(id):
    query = Device.query.get(id)
    return query

def db_get_device_interface_facts(id):
    query = DeviceInterfaceFacts.query.filter(DeviceInterfaceFacts.device==id).all()
    return query

def db_get_device_software_facts(id):
    query = DeviceSoftwareFacts.query.get(id)
    return query

def db_get_devices():
    query =  Device.query.all()
    return query

def db_get_devices_software_facts():
    query = DeviceSoftwareFacts.all()
    return query

def db_get_user(id):
    query = User.query.get(id)
    return query

def db_get_users():
    query = User.query.all()
    return query

"""
def db_update_device_interface_facts(device, interface_list):
    for interface in interface_list:
        for key,value in interface.items():
            setattr(device.interface_facts, key, str(value)) #TextFSM Template may return lists so we need to convert it to string
    db.session.commit()
    return device.interface_facts

def db_update_device_software_facts(device, **kwargs):
    for key, value in kwargs.items():
        setattr(device.software_facts, key, str(value)) #TextFSM Template may return lists so we need to convert it to string
    db.session.commit()
    return device.software_facts
"""