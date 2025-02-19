import sys
import os
import platform
from subprocess import Popen, PIPE, STDOUT, DEVNULL, CalledProcessError
if platform.system() == "Windows":
    from subprocess import DETACHED_PROCESS, CREATE_NEW_PROCESS_GROUP

import click

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='exercise.log', level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)

from . import jupyter as _jupyter
from .config import ANACONDA_CHANNEL, MAINTAINER_EMAIL, REGISTRY_BASE_URL, REQUIRED_GB_FREE_DISK
from .utils import wrap_text
from . import docker as _docker

# TODO: maybe I can use the platforms on gitlab actions to build conda
# environments for different platforms as backup for when docker fails...

# TODO: open download link for exercise notebook in browser after starting container

def update_client(update):
    if not update:
        logger.debug('Update check skipped')
    else:
        click.echo('Updating client...', nl=False)
        # cmd = f"{os.environ['CONDA_EXE']} update -y -c {ANACONDA_CHANNEL} --no-update-deps exercise-client"
        cmd = f"conda update -y -c {ANACONDA_CHANNEL} --no-update-deps exercise-client"
        logger.debug(cmd)
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()
        if stdout:
            [logger.debug(x) for x in stdout.decode().splitlines()]
        if stderr:
            [logger.debug(x) for x in stderr.decode().splitlines()]
        if p.returncode:
            logger.debug(f"Update failed with return code {p.returncode}")

            if stderr and 'PackageNotInstalledError' in stderr.decode():
                msg = f"""
                The package is not installed as a conda package in this environment.
                Please install the package with the following command:
                
                conda install -c {ANACONDA_CHANNEL} exercise-client
                """
                click.echo(msg)
            msg = f"""
            Could not update client. Please try again later.
            If problem persists, please email {MAINTAINER_EMAIL}
            with a screenshot of the error message.
            """
            click.echo(msg)
            sys.exit()
        click.echo('done.')



# @click.option("--verbose",
#                 default=False,
#                 help="Print debugging information")
# @click.option("--fixme",
#                 default=False,
#                 help="Run trouble shooting")
# @click.option("--clone",
#                 default=False,
#                 help="Also clone the repository")
@click.option("--subdir-limit",
                default=0,
                help="Allowed depth of subdir tree")
@click.option('--update/--no-update', default=True,
                help="Override check for package updates")
@click.command()
def jupyter(subdir_limit, update):

    # gb_free = shutil.disk_usage('/').free / 1024**3
    # if gb_free < 10:

    if _docker.check_internet_connection():
        logger.error("Internet connection to Docker Hub ok")
    else:
        click.secho('"No internet connection', fg='red')
        logger.error("No internet connection to Docker Hub")
        sys.exit(1)

    if _docker.check_docker_desktop_running():
        logger.debug("Docker Desktop is running")
    else:
        click.secho('Docker Desktop is not running', fg='red')
        logger.error("Docker Desktop is not running")
        sys.exit(1)

    free_gb = _docker.free_disk_space()
    if free_gb < REQUIRED_GB_FREE_DISK:
        click.secho(f'Not enough disk space. Required: {REQUIRED_GB_FREE_DISK} GB, Available: {free_gb} GB', fg='red')
        logger.error(f"Not enough disk space. Required: {REQUIRED_GB_FREE_DISK} GB, Available: {free_gb} GB")
        sys.exit(1)

    # TODO: check if docker is installed
    # _docker.check_no_other_exercise_container_running()
    # _docker.check_no_other_local_jupyter_running()

    update_client(update)

    _jupyter.launch_exercise()


@click.group()
def docker():
    """Docker commands."""
    pass


@docker.command()
def test():
    """List docker volumes."""
    click.echo(
        'asdfadsfasdf'
    )
    _docker.prune(logger)


@docker.command()
def volumes():
    """List docker volumes."""
    click.echo(_docker.volumes(logger))

@docker.command()
def images():
    """List docker images."""
    click.echo(_docker.images(logger))

@click.argument("url")
@docker.command()
def pull(url):
    """Pull docker image.
    
    URL is the Docker image URL.
    """
    _docker.pull(url)

@docker.command()
def containers():
    """List docker containers."""
    click.echo(_docker.containers(logger))

@click.argument('container')
@docker.command()
def kill(container):
    """Kills a running container.
    
    CONTAINER is the id of the container to kill."""
    _docker.kill(container, logger)

@click.option("--verbose/--no-verbose", default=False, help="More detailed output")
@docker.command()
def storage(verbose):
    """Show Docker's disk usage."""

    click.echo(_docker.storage(verbose, logger))


@docker.group()
def remove():
    """Remove Docker elements."""
    pass

@remove.command()
def images():
    _docker.remove_images(logger)



# @click.option("--containers/--no-containers", default=True, help="Prune containers")
# @click.option("--volumes/--no-volumes", default=True, help="Prune volumes")
# @docker.command()
# def prune(containers, volumes):
#     """Prune docker containers and volumes."""
#     if containers and volumes:
#         _docker.prune_all()
#     elif containers:
#         _docker.prune_containers()
#     elif volumes:
#         _docker.prune_volumes()

# @click.option("--force/--no-force", default=False, help="Force removal")
# @click.argument('image')
# @docker.command()
# def remove(image, force):
#     """Remove docker image.
    
#     IMAGE is the id of the image to remove.
#     """

#     _docker.rm_image(image, force)

# @docker.command()
# def cleanup():
#     """Cleanup everything."""

#     for image in _docker.images():
#         if image['Repository'].startswith(REGISTRY_BASE_URL):
#             _docker.rm_image(image['ID'])
#     _docker.prune_containers()
#     _docker.prune_volumes()
#     _docker.prune_all()




@click.group()
def devel():
    pass

@devel.command()
def download():
    pass

@devel.command()
def sync():
    pass

@devel.command()
def status():
    pass

#@click.group(invoke_without_command=True)
@click.group()
def franklin():
    """
    Bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla 
    bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla
    bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla
    bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla.

    \b
    Bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla 

    Bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla 
    bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla
    bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla
    bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla.    
    """

    pass

franklin.add_command(jupyter)
franklin.add_command(docker)
franklin.add_command(devel)


    # container_id = subprocess.check_output('docker ps -q', shell=True).decode().strip()

    # args = f"docker logs --follow {container_id}".split()
    # asyncio.run(run_docker(args))


    # alternative
    #          -t -i
    # args = f"run --attach stdout --attach stderr --rm --mount type=bind,source=/Users/kmt/.ssh,target=/tmp/.ssh --mount type=bind,source=/Users/kmt/.anaconda,target=/root/.anaconda --mount type=bind,source=/Users/kmt/google_drive/projects/mbg-exercise-client,target=/Users/kmt/google_drive/projects/mbg-exercise-client -w /Users/kmt/google_drive/projects/mbg-exercise-client -p 8888:8888 registry.gitlab.au.dk/au81667/mbg-docker-exercises:main".split()

    # args = f"run -d --name kaspertest --rm --mount type=bind,source=/Users/kmt/.ssh,target=/tmp/.ssh --mount type=bind,source=/Users/kmt/.anaconda,target=/root/.anaconda --mount type=bind,source=/Users/kmt/google_drive/projects/mbg-exercise-client,target=/Users/kmt/google_drive/projects/mbg-exercise-client -w /Users/kmt/google_drive/projects/mbg-exercise-client -p 8888:8888 registry.gitlab.au.dk/au81667/mbg-docker-exercises:main  ; docker attach kaspertest".split()

    # args = f"run --pull=always --rm --mount type=bind,source={user_home}/.ssh,target=/tmp/.ssh --mount type=bind,source={user_home}/.anaconda,target=/root/.anaconda --mount type=bind,source={pwd},target={pwd} -w {pwd} -i -t -p 8888:8888 {image_url}:main".split()
    # args = f"run --rm --mount type=bind,source={user_home}/.ssh,target=/tmp/.ssh --mount type=bind,source={user_home}/.anaconda,target=/root/.anaconda --mount type=bind,source={pwd},target={pwd} -w {pwd} -i -t -p 8888:8888 {image_url}:main".split()

    # # args = f"run -t -i --attach stdout --attach stderr --rm --mount type=bind,source=/Users/kmt/.ssh,target=/tmp/.ssh --mount type=bind,source=/Users/kmt/.anaconda,target=/root/.anaconda --mount type=bind,source=/Users/kmt/google_drive/projects/mbg-exercise-client,target=/Users/kmt/google_drive/projects/mbg-exercise-client -w /Users/kmt/google_drive/projects/mbg-exercise-client -p 8888:8888 registry.gitlab.au.dk/au81667/mbg-docker-exercises:main".split()

    # asyncio.run(run_docker(args))

#docker run --attach stdout --attach stderr --name kaspertest --rm --mount type=bind,source=/Users/kmt/.ssh,target=/tmp/.ssh --mount type=bind,source=/Users/kmt/.anaconda,target=/root/.anaconda --mount type=bind,source=/Users/kmt/google_drive/projects/mbg-exercise-client,target=/Users/kmt/google_drive/projects/mbg-exercise-client -w /Users/kmt/google_drive/projects/mbg-exercise-client -p 8888:8888 registry.gitlab.au.dk/au81667/mbg-docker-exercises:main

#docker run -d --name kaspertest --rm --mount type=bind,source=/Users/kmt/.ssh,target=/tmp/.ssh --mount type=bind,source=/Users/kmt/.anaconda,target=/root/.anaconda --mount type=bind,source=/Users/kmt/google_drive/projects/mbg-exercise-client,target=/Users/kmt/google_drive/projects/mbg-exercise-client -w /Users/kmt/google_drive/projects/mbg-exercise-client -p 8888:8888 registry.gitlab.au.dk/au81667/mbg-docker-exercises:main ; docker attach kaspertes

# docker run -d --name topdemo alpine top -b

# docker attach topdemo

#docker run -d --name tester --rm --mount type=bind,source=/Users/kmt/.ssh,target=/tmp/.ssh --mount type=bind,source=/Users/kmt/.anaconda,target=/root/.anaconda --mount type=bind,source=/Users/kmt/google_drive/projects/mbg-exercise-client,target=/Users/kmt/google_drive/projects/mbg-exercise-client -w /Users/kmt/google_drive/projects/mbg-exercise-client -p 8888:8888 registry.gitlab.au.dk/au81667/mbg-docker-exercises:main -b

# docker run -d --name kaspertest --rm --mount type=bind,source=/Users/kmt/.ssh,target=/tmp/.ssh --mount type=bind,source=/Users/kmt/.anaconda,target=/root/.anaconda --mount type=bind,source=/Users/kmt/google_drive/projects/mbg-exercise-client,target=/Users/kmt/google_drive/projects/mbg-exercise-client -w /Users/kmt/google_drive/projects/mbg-exercise-client -p 8888:8888 registry.gitlab.au.dk/au81667/mbg-docker-exercises:main -b -t ; docker attach kaspertest

#     check_docker_running()

#     registry_listing = get_registry_listing()

# client.images.pull('kaspermunch/sap')

#     course_mapping = get_course_mapping()

#     course = get_user_input(course_mapping)

#     week_mapping = get_week_mapping()

#     check_no_other_exercise_container_running()

#     check_no_other_local_jupyter_running()

#     # https://docker-py.readthedocs.io/en/stable/
#     client = docker.from_env()
#     client.images.pull('nginx')
#     container = client.containers.run("bfirsh/reticulate-splines", detach=True)
#     for line in container.logs(stream=True):
#         print(line.strip())
#     container.stop()

#     launch_docker(course, week_mapping)

#     report_disk_space()

#     purge_docker_images_and_containers()


# #!/usr/bin/env python3

# import docker, getpass

# client = docker.from_env()

# my_pw = getpass.getpass(prompt='Password: ')

# sec_name = 'TestSec'
# noise = client.secrets.create(name=sec_name,  
#                               data=str.encode(my_pw))
# secret_id = client.secrets.list(filters={'name': sec_name})[0].id

# secRef = docker.types.SecretReference(secret_id, sec_name)

# print(type(secRef))

# client.services.create('alpine:latest',
#                        name='TestSvc',
#                        hostname='test_host',
#                        secrets=[secRef],
#                        command='sleep 999',)






# >>> import platform
# >>> platform.system()
# 'Darwin'
# >>> platform.processor()
# 'i386'
# >>> platform.platform()
# 'Darwin-10.8.0-i386-64bit'
# >>> platform.machine()
# 'i386'
# >>> platform.version()
# 'Darwin Kernel Version 10.8.0: Tue Jun  7 16:33:36 PDT 2011; root:xnu-1504.15.3~1/RELEASE_I386'
# >>> platform.uname()
# ('Darwin', 'Hostname.local', '10.8.0', 'Darwin Kernel Version 10.8.0: Tue Jun  7 16:33:36 PDT 2011; root:xnu-1504.15.3~1/RELEASE_I386', 'i386', 'i386')




# 1. Activate a MBGexercises environment  
# 2. Check for package updates of mbg-exercise-client package at the mbgexercises anaconda channel
# 3. Update package if necessary and reimport package after update to use new version  
# 4. Read registry listing using API requests library (see above)  
# 5. Read yml file mapping English to Danish course names (see above)
# 6. Take user input through to pick course
# 7. Read yml file mapping exercises to week numbers (see above)
# 8. Check that docker is installed
# 9. Check that docker is running  
# 10. Check that no other exercise container is running  
# 11. Check that no other local jupyter is using a port  
# 12. Launch docker run as a process in a separate thread (like in slurm-jupyter)  
# 13. Read URL from the output and launch the browser like in  (like in slurm-jupyter)  
# 14. Make sure the script cannot be shut down with keyboard interrupt or kill without cleaning up  
# 15. Report how much disk space images and containers currently use  
# 16. Ask to purge docker images and containers \[Y\]/n and do so  
# 17. Exit




# from collections import defaultdict
# from bullet import Bullet, colors, VerticalPrompt, SlidePrompt, ScrollBar, emojis

# options = dict(
#     indent = 0,
#     shift = 0,
#     align = 2, 
#     margin = 1,
#     # bullet = "★",
#     pointer = "★",
#     pad_right = 10,
#     height = 10,    
#     # bullet_color=colors.bright(colors.foreground["default"]),
#     word_color=colors.bright(colors.foreground["default"]),
#     word_on_switch=colors.bright(colors.foreground["green"]),
#     background_color=colors.background["default"],
#     background_on_switch=colors.background["default"],
#     return_index=False
# )

# image_name_list = [
#     'Biomolekylær_struktur_og_funktion-uge1-v1',
#     'Biomolekylær_struktur_og_funktion-uge2-v1',
#     'Bioinformatik_og_programmering-uge_1-v1',
#     'Bioinformatik_og_programmering-uge_2-v1',
# ]

# image_tree = defaultdict(lambda: defaultdict(lambda: defaultdict(str)))
# for image_name in image_name_list:
#     c, w, v = image_name.split('-')
#     image_tree[c.replace('_', ' ')][w.replace('_', ' ')][v.replace('_', ' ')] = image_name

# # cli = ScrollBar(
# #     "How are you feeling today? ", 
# #     choices = list(image_tree.keys()) + ['asdf']*15,
# #     height = 15,
# #     **options
# # )
# # result = cli.launch()
# # print(result)

# cli = ScrollBar(prompt = "\n Select course: ", choices = list(image_tree.keys())*15, **options)
# course = cli.launch()
# cli = ScrollBar(prompt = "\n Select exercise: ", choices = list(image_tree[course].keys()), **options)
# week = cli.launch()
# cli = ScrollBar(prompt = "\n Select version: ", choices = list(image_tree[course][week].keys()), **options)
# version = cli.launch()
# selected_image = image_tree[course][week][version]


# # cli = SlidePrompt([
# #     Bullet(prompt = "\nSelect course: ", choices = list(image_tree.keys()), **options),
# #     Bullet(prompt = "\nSelect week: ", choices = list(image_tree[course].keys()), **options),
# #     Bullet(prompt = "\nSelect version: ", choices = list(image_tree[course][week].keys()), **options)
# # ])
# # course, week, version = cli.launch()
# # selected_image = image_tree[course][week][version]




# # course_menu = Bullet(
# #         prompt = "\nSelect course: ",
# #         choices = ["Biomolekylær struktur og funktion", "Bioinformatik og programmering", "orange", "watermelon", "strawberry"], 
# #         indent = 3,
# #         shift = 0,
# #         align = 3, 
# #         margin = 1,
# #         bullet = "★",
# #         # bullet_color=colors.bright(colors.foreground["cyan"]),
# #         # word_color=colors.bright(colors.foreground["yellow"]),
# #         # word_on_switch=colors.bright(colors.foreground["yellow"]),
# #         # background_color=colors.background["black"],
# #         # background_on_switch=colors.background["black"],
# #         pad_right = 10
# #     )
# # week_menu = Bullet(
# #         prompt = "\nSelect week: ",
# #         choices = ["week1", "week2"], 
# #         indent = 3,
# #         shift = 0,
# #         align = 3, 
# #         margin = 1,
# #         bullet = "★",
# #         # bullet_color=colors.bright(colors.foreground["cyan"]),
# #         # word_color=colors.bright(colors.foreground["yellow"]),
# #         # word_on_switch=colors.bright(colors.foreground["yellow"]),
# #         # background_color=colors.background["black"],
# #         # background_on_switch=colors.background["black"],
# #         pad_right = 10
# #     )


# # cli = VerticalPrompt([course_menu, week_menu], spacing = 0)

# # result = cli.launch()
# # print("You chose:", result)

# # # result = cli.launch()
# # # print(result)

# adapters
# api_version
# attach
# attach_socket
# auth
# base_url
# build
# cert
# close
# commit
# connect_container_to_network
# containers
# cookies
# copy
# create_container
# create_container_config
# create_container_from_config
# create_endpoint_config
# create_host_config
# create_network
# create_networking_config
# create_service
# create_swarm_spec
# create_volume
# delete
# diff
# disconnect_container_from_network
# events
# exec_create
# exec_inspect
# exec_resize
# exec_start
# export
# from_env
# get
# get_adapter
# get_archive
# get_image
# get_redirect_target
# head
# headers
# history
# hooks
# images
# import_image
# import_image_from_data
# import_image_from_file
# import_image_from_image
# import_image_from_stream
# import_image_from_url
# info
# init_swarm
# insert
# inspect_container
# inspect_image
# inspect_network
# inspect_node
# inspect_service
# inspect_swarm
# inspect_task
# inspect_volume
# join_swarm
# kill
# leave_swarm
# load_image
# login
# logs
# max_redirects
# merge_environment_settings
# mount
# networks
# nodes
# options
# params
# patch
# pause
# ping
# port
# post
# prepare_request
# proxies
# pull
# push
# put
# put_archive
# rebuild_auth
# rebuild_method
# rebuild_proxies
# remove_container
# remove_image
# remove_network
# remove_service
# remove_volume
# rename
# request
# resize
# resolve_redirects
# restart
# search
# send
# services
# should_strip_auth
# start
# stats
# stop
# stream
# tag
# tasks
# timeout
# top
# trust_env
# unpause
# update_container
# update_service
# update_swarm
# verify
# version
# volumes
# wait





    # # client = docker.Client(base_url='https://registry.hub.docker.com:443')
    # client = docker.Client(
    #     base_url='tcp://gitlab.au.dk:443',
    #     # base_url='tcp://gitlab.au.dk:443/api/v4/projects/au81667%2Fmbg-docker-exercises/registry/repositories',
    #     # credstore_env={'PRIVATE-TOKEN': 'glpat-tiYpz3zJ95qzVXnyN8--'}
    #     )
    # print(client.images())
    # print(client.search('au81667/mbg-docker-exercises'))
    # client.search('kaspermunch/sap')

#     # client = docker.Client(base_url='https://registry.hub.docker.com:443')
#     client = docker.Client(base_url='https://registry.gitlab.au.dk:443')

# #    client.images(name='kaspermunch/sap')
#     client.search('au81667/mbg-docker-exercises')

#    docker pull registry.gitlab.au.dk/au81667/mbg-docker-exercises:main




    # headers = {'PRIVATE-TOKEN': 'glpat-tiYpz3zJ95qzVXnyN8--'}
    # client.get('au81667/mbg-docker-exercises', **headers)



#registry.gitlab.au.dk/au81667/mbg-docker-exercises

    # print(dir(docker.constants))

#    print(client.pull('mbg-docker-exercises'))#, auth_config={'PRIVATE-TOKEN': 'glpat-tiYpz3zJ95qzVXnyN8--'}))
    # print(*dir(client), sep='\n')

    # noise = docker.secrets()#.create_secret(name='PRIVATE-TOKEN',  
    #                          #  data=str.encode('glpat-tiYpz3zJ95qzVXnyN8--'))

    # import  getpass
    # client = docker.from_env()
    # my_pw = getpass.getpass(prompt='Password: ')
    # sec_name = 'TestSec'
    # noise = docker.secrets.create(name=sec_name,  
    #                             data=str.encode(my_pw))
    # secret_id = docker.secrets.list(filters={'name': sec_name})[0].id

    # secRef = docker.types.SecretReference(secret_id, sec_name)

    # print(type(secRef))

    # client.services.create('alpine:latest',
    #                     name='TestSvc',
    #                     hostname='test_host',
    #                     secrets=[secRef],
    #                     command='sleep 999',)



