import os
import sys
import subprocess


def remove_virtual_environment():
    '''
    This function will remove the virtual environment
    '''
    print("Removing virtual environment")
    try:
        subprocess.check_call(['rm', '-rf', 'venv'])
    except subprocess.CalledProcessError as e:
        print("Error while removing virtual environment")
        print(e)
        sys.exit(1)


def create_virtual_environment():
    '''
    This function will create a virtual environment in the project directory
    '''
    print("Creating virtual environment")
    try:
        subprocess.check_call([sys.executable, '-m', 'venv', 'venv'])
    except subprocess.CalledProcessError as e:
        print("Error while creating virtual environment")
        print(e)
        sys.exit(1)


def ensure_pip_installed():
    '''
    This function will ensure pip is installed
    '''
    print("Ensuring pip is installed")
    try:
        subprocess.check_call(['venv/bin/python', '-m', 'pip', '--version'])
    except subprocess.CalledProcessError:
        print("pip not found. Please install pip using the package manager:")
        print("sudo apt install python3-pip")
        sys.exit(1)


def install_required_packages():
    '''
    This function will install all the required packages in the virtual environment
    '''
    print("Installing required packages")
    try:
        subprocess.check_call(
            ['venv/bin/python', '-m', 'pip', 'install', '-r', 'requirements.txt'])
    except subprocess.CalledProcessError as e:
        print("Error while installing required packages")
        print(e)
        sys.exit(1)


def run_tests():
    '''
    This function will run all the test cases
    '''
    print("Running tests")
    try:
        subprocess.check_call(['venv/bin/python', '-m', 'pytest'])
    except subprocess.CalledProcessError as e:
        print("Error while running tests")
        print(e)
        sys.exit(1)


def docker_compose_down():
    '''
    This function will stop the docker-compose file
    '''
    print("Stopping docker-compose")
    try:
        subprocess.check_call(['docker-compose', 'down'])
    except subprocess.CalledProcessError as e:
        print("Error while stopping docker-compose")
        print(e)
        sys.exit(1)


def docker_compose_up():
    '''
    This function will run the docker-compose file
    This will start the backend server
    '''
    print("Running docker-compose")
    try:
        subprocess.check_call(['docker-compose', 'up', '--build', '-d'])
    except subprocess.CalledProcessError as e:
        print("Error while running docker-compose")
        print(e)
        sys.exit(1)


def main():
    remove_virtual_environment()
    create_virtual_environment()
    ensure_pip_installed()
    install_required_packages()
    run_tests()
    docker_compose_down()
    docker_compose_up()


if __name__ == "__main__":
    main()
