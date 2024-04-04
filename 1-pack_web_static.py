#!/usr/bin/python3
""" Generates an archive (.tgz) from the contents of the web_static folder """
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Creates a .tgz archive from the contents of the web_static folder."""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        if not os.path.exists("versions"):
            local("mkdir versions")
        archive_p = 'versions/web_static_{}.tgz'.format(time)
        local("tar -czvf {} web_static".format(archive_p))
        return archive_p
    except:
        return None