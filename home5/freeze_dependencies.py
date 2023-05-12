import subprocess


def freeze_dependencies():
    subprocess.run(['pip', 'freeze', '>', 'requirements.txt'], check=True, shell=True)


# Пример использования:
freeze_dependencies()
