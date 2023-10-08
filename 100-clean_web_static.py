#!/usr/bin/python3
""" Function that deletes out-of-date archives """
from fabric.api import *


env.hosts = ["100.25.35.201", "34.227.91.172"]
env.user = "ubuntu"


def do_clean(number=0):
    """
    cleans out-of-date archives
    """

    number = int(number)

    if number == 0:
        numbers = 1
    else:
        numbers = number

    local('cd versions ; ls -t | head -n -{} | xargs rm -rf'.format(numbers))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | head -n -{} | xargs rm -rf'.format(path, numbers))
