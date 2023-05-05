#!/usr/bin/python3
"""
    Script that Clean up the archive files on the server
"""
from fabric.api import run, env, local
import os

env.user = "ubuntu"
env.hosts = ["100.26.120.84", "18.207.1.176"]
env.path_filename = "~/.ssh/id_rsa"


def do_clean(number=0):
    """ clean archive files on the server """

    number = int(number)
    if os.path.exists("versions/"):
        if number == 0 or number == 1:
            local("ls -1tr versions/*.tgz | head -n -1 | xargs rm -rf")
        else:
            local("ls -1tr versions/*.tgz | head -n -{} | xargs rm -rf".format(
                number))

    path = "/data/web_static/releases/*/"
    try:
        if number == 0 or number == 1:
            run("sudo ls -1tr {} | head -n -1 | xargs rm -rf".format(path))
        else:
            run("sudo ls -1tr {} | head -n -{} | xargs rm -rf".format(
                path, number))
        return True

    except Exception as e:
        return False
