#!/usr/bin/python3
"""creates and distributes an archive to your web servers"""
from fabric.api import put, run, env, local
from datetime import datetime
import os

env.hosts = ['18.206.208.113', '18.206.232.93']
env.user = "ubuntu"


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        archive_name = os.path.basename(archive_path)
        archive_base = os.path.splitext(archive_name)[0]
        path = "/data/web_static/releases/"

        run('mkdir -p {}{}/'.format(path, archive_base))
        run('tar -xzf /tmp/{} -C {}{}/'
            .format(archive_name, path, archive_base))
        run('rm /tmp/{}'.format(archive_name))
        run('mv {0}{1}/web_static/* {0}{1}/'
            .format(path, archive_base))
        run('rm -rf {}{}/web_static'.format(path, archive_base))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, archive_base))
        run('chmod -R 755 /data/')
        print("New version deployed!")
        return True
    except FileNotFoundError:
        return False


def do_pack():
    """Creates a .tgz archive from the contents of the web_static folder."""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        if not os.path.exists("versions"):
            local("mkdir versions")
        archive_p = 'versions/web_static_{}.tgz'.format(time)
        local("tar -czvf {} web_static".format(archive_p))
        return archive_p
    except FileNotFoundError:
        return None


def deploy():
    """ DEPLOYS """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)