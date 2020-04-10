# flask_db_relationships
Example of DB Relationships and Flask

I haven't included a requirements.txt for specific reasons... This repo is an addition to a blog and the 1 task I've set for the average network engineer getting into python/automation is to learn how to pull a repository and use pip install to get familiar with the git and pip CLI.

### You can create the databases by using:
```console
$flask db init
$flask db migrate
$flask db upgrade
```

The base idea of this program is to pull Cisco IOS information (Interfaces and Show version in this example), store them into a database and have a very basic frontend GUI and backend API with a little bit of Javascript/AJAX.

## The whole database relationship goes like this:

1) There must be a user created

2) When creating a Device, a relationship can be configured to assign a Device to a specific user (to use that users credentials to log into SSH via netmiko) via a One to Many relationship (a device can only have 1 user, but a user can be responsible for many devices).

3) When you pull interface and version information for the device, this is then linked (one-to-one relationship) to the specific device (id).

I've tried to make the code quite clear so the average person can work out logically what happens and how...