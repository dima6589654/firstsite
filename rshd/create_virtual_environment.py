import os
import sys
import subprocess


def create_virtual_environment(env_name):
    if sys.platform.startswith('win'):
        subprocess.run(['python', '-m', 'venv', env_name], check=True, shell=True)
    else:
        subprocess.run(['python3', '-m', 'venv', env_name], check=True, shell=True)


# Пример использования:
create_virtual_environment('venv')
