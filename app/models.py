from app import db
from dataclasses import dataclass
from sqlalchemy.inspection import inspect

@dataclass
class User(db.Model):
    """ User Model """
    id: int
    username: str
    password: str

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), index=True, unique=True)
    password = db.Column(db.String(20), index=True)
    devices = db.relationship('Device', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.username)

    def __hash__(self):
        return hash(self.id)

@dataclass
class Device(db.Model):
    """ Device Model """
    id: int
    ip_addr: str
    friendly_name: str
    netmiko_driver: str
    device_user: int

    id = db.Column(db.Integer, primary_key=True)
    ip_addr = db.Column(db.String(64), index=True, unique=True)
    friendly_name = db.Column(db.String(64))
    netmiko_driver = db.Column(db.String(64))
    device_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    software_facts = db.relationship('DeviceSoftwareFacts', backref='device_software', uselist=False)
    interface_facts = db.relationship('DeviceInterfaceFacts', backref='device_interfaces')

    def __repr__(self):
        return '<Device %r>' % (self.ip_addr)

    def __hash__(self):
        return hash(self.id)

@dataclass
class DeviceSoftwareFacts(db.Model):
    """ Device Software Facts Model """
    id: int
    version: str
    rommon: str
    hostname: str
    uptime: str
    reload_reason: str
    running_image: str
    hardware: str
    serial: str
    config_register: str
    mac: str
    device: int

    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.String())
    rommon = db.Column(db.String())
    hostname = db.Column(db.String())
    uptime = db.Column(db.String())
    reload_reason = db.Column(db.String())
    running_image = db.Column(db.String())
    hardware = db.Column(db.String())
    serial = db.Column(db.String())
    config_register = db.Column(db.String())
    mac = db.Column(db.String())
    device = db.Column(db.Integer, db.ForeignKey('device.id'))

    def __repr__(self):
        return '<DeviceSoftwareFacts %r>' % (self.id)
        
    def __hash__(self):
        return hash(self.id)

@dataclass
class DeviceInterfaceFacts(db.Model):
    """ Device Software Facts Model """
    id: int
    interface: str
    link_status: str
    protocol_status: str
    hardware_type: str
    address: str
    bia: str
    description: str
    ip_address: str
    mtu: str
    duplex: str
    speed: str
    bandwidth: str
    delay: str
    encapsulation: str
    last_input: str
    last_output: str
    last_output_hang: str
    queue_strategy: str
    input_rate: str
    output_rate: str
    input_packets: str
    output_packets: str
    input_errors: str
    output_errors: str
    device: int

    id = db.Column(db.Integer, primary_key=True)
    interface = db.Column(db.String())
    link_status = db.Column(db.String())
    protocol_status = db.Column(db.String())
    hardware_type = db.Column(db.String())
    address = db.Column(db.String())
    bia = db.Column(db.String())
    description = db.Column(db.String())
    ip_address = db.Column(db.String())
    mtu = db.Column(db.String())
    duplex = db.Column(db.String())
    speed = db.Column(db.String())
    bandwidth = db.Column(db.String())
    delay = db.Column(db.String())
    encapsulation = db.Column(db.String())
    last_input = db.Column(db.String())
    last_output = db.Column(db.String())
    last_output_hang = db.Column(db.String())
    queue_strategy = db.Column(db.String())
    input_rate = db.Column(db.String())
    output_rate = db.Column(db.String())
    input_packets = db.Column(db.String())
    output_packets = db.Column(db.String())
    input_errors = db.Column(db.String())
    output_errors = db.Column(db.String())
    device = db.Column(db.Integer, db.ForeignKey('device.id'))

    def __repr__(self):
        return '<DeviceInterfaceFacts %r>' % (self.id)

    def __hash__(self):
        return hash(self.id)