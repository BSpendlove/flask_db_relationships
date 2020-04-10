from netmiko.ssh_dispatcher import CLASS_MAPPER
from netmiko import ConnectHandler
from app.utils.textfsm_extractor import textfsm_extractor

class NetmikoAPI():
    def __init__(self, device):
        ssh_details = {
            "device_type": device.netmiko_driver,
            "ip": device.ip_addr,
            "username": device.user.username,
            "password": device.user.password
        }

        self.ssh_session = ConnectHandler(**ssh_details)

    def enable(self):
        self.ssh_session.enable()

    def send_command(self, *args, **kwargs):
        return self.ssh_session.send_command(**kwargs)

    def show_interfaces(self):
        return textfsm_extractor("cisco_ios_show_interfaces", self.send_command(command_string="show interfaces"))

    def show_version(self):
        return textfsm_extractor("cisco_ios_show_version", self.send_command(command_string="show version"))[0]

def get_device_types():
    return CLASS_MAPPER