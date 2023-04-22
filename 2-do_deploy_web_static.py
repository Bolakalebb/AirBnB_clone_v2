#!/usr/bin/python3
"""distributes an archive to your web servers,
using the function do_deploy"""

from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['54.158.180.235', '54.237.0.75']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/my_privkey'

def do_pack():
    """
    Creates a compressed archive of the web_static folder.
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    local('sudo mkdir -p versions')
    path = './versions/web_static_{}'.format(now)
    local('sudo tar -czvf {}.tgz web_static'.format(path))
    name = '{}.tgz'.format(path)
    if name:
        return name
    else:
        return None


def do_deploy(archive_path):
    """Deploy the boxing package tgz file
    """
    try:
        archive = archive_path.split('/')[-1]
        path = '/data/web_static/releases/' + archive.strip('.tgz')
        current = '/data/web_static/current'
        put(archive_path, '/tmp')
        run('mkdir -p {}/'.format(path))
        run('tar -xzf /tmp/{} -C {}'.format(archive, path))
        run('rm /tmp/{}'.format(archive))
        run('mv {}/web_static/* {}'.format(path, path))
        run('rm -rf {}/web_static'.format(path))
        run('rm -rf {}'.format(current))
        run('ln -s {} {}'.format(path, current))
        print('New version deployed!')
        return True
    except:
        return False
