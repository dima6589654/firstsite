import os


def create_django_project(project_name):
    os.system(f'django-admin startproject {project_name}')

create_django_project('my_django_project')
