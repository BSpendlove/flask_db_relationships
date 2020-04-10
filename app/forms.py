from flask_wtf import FlaskForm
from app.models import db, User
from app.functions import db_functions, netmiko_functions
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

"""
supported_netmiko_devices = [
    ("cisco_ios", "Cisco IOS"),
    ("cisco_asa", "Cisco ASA"),
    ("huawei", "Huawei"),
    ("huawei_smartax", "Huawei SmartAX")]
"""

class UserAddForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Add')

class DeviceAddForm(FlaskForm):
    ip_addr = StringField('IP Address', validators=[DataRequired()])
    friendly_name = StringField('Friendly Name')
    netmiko_driver = SelectField(
        'Netmiko Driver',
        #choices=[netmiko_functions.get_device_types()]
        choices=[(x,x) for x,y in netmiko_functions.get_device_types().items()]
    )
    device_user = QuerySelectField(
        'User',
        get_label='username',
        query_factory=db_functions.db_get_users,
        allow_blank=False
    )
    submit = SubmitField('Add')