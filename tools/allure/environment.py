from config import settings
import platform
import sys


def create_allure_environment_file():
    items = [f"{key}={value}" for key, value in settings.model_dump(exclude={"test_user"}).items()]
    items.append(f'os_info={platform.system()}, {platform.release()}')
    items.append(f'python_version={sys.version}')
    properties = '\n'.join(items)

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)