from fabric import colors
from fabric.api import task
from fabric.api import env
from fabric.api import run
from fabric.api import cd
from fabric.api import prefix


env.hosts = ['45.55.252.44']
env.user = 'vt'
env.key_filename = '/home/sardor/.ssh/id_rsa.pub'


ROOT = '/home/vt/'
CODE_ROOT = '%s/vt' % ROOT
LOCAL_SETTINGS = '%s/vt/config/production.py' % CODE_ROOT
GUNICORN = '/usr/local/bin/gunicorn'


@task
def git_pull():
    with cd(CODE_ROOT):
        run('git pull origin develop')


@task
def install_requirements():
    print(colors.cyan('Installing requirements...', bold=True))
    with cd(CODE_ROOT):
        run('pip install -U -r requirements.txt')
        run('pip install -e .')


@task
def deploy():
    """Deploy code to production"""
    print(colors.cyan('Deploying...', bold=True))
    with cd(CODE_ROOT):
        run('git pull origin develop')
        clear_cache()
        run('find . -name "*.pyc" -delete')
        restart()


@task
def clear_cache():
    with cd(CODE_ROOT):
        run('redis-cli -n 1 flushdb')


@task
def restart():
    with cd(CODE_ROOT):
        run('supervisorctl -c deploy/supervisord.conf restart vt')
