#!/usr/bin/python3
""" that deletes out-of-date archives, using the function do_clean """
from fabric.api import *


env.hosts = ['18.206.208.113', '18.206.232.93']
env.user = "ubuntu"


def do_clean(number=0):
    """ that deletes out-of-date archives, using the function do_clean """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
