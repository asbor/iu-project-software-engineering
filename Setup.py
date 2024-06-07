# This script will automatically prepare the project for the user.
#    1) Create a virtual environment
#    2) Install all the required packages
#    3) Trigger the pytest to run all the test cases
#

# Create a virtual environment
import os
import sys
import subprocess


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


def install_required_packages():
    '''
    This function will install all the required packages in the virtual environment
    '''

    print("Installing required packages")
    try:
        subprocess.check_call(
            [sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
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
        subprocess.check_call([sys.executable, '-m', 'pytest'])
    except subprocess.CalledProcessError as e:
        print("Error while running tests")
        print(e)
        sys.exit(1)


def run_docker_compose():
    '''
    This function will run the docker-compose file
    This will start the backend server
    '''

    print("Running docker-compose")
    try:
        subprocess.check_call(
            ['docker-compose', 'up', '--build', '-d'])
    except subprocess.CalledProcessError as e:
        print("Error while running docker-compose")
        print(e)
        sys.exit(1)


def run_frontend():
    '''
    This function will run the frontend server
    '''

    # navigate to services/nuxt3-shadcn and run yarn && yarn dev
    os.chdir('services/nuxt3-shadcn')
    try:
        subprocess.check_call(
            ['yarn'])
    except subprocess.CalledProcessError as e:
        print("Error while running yarn")
        print(e)
        sys.exit(1)


def main():
    create_virtual_environment()
    install_required_packages()
    run_tests()
    run_docker_compose()
    run_frontend()


if __name__ == "__main__":
    main()
