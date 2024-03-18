# Readme

## Project Overview

This project is part of the Software Engineering course at the Faculty of Informatics, International University of Applied Sciences Bad Honnef - Bonn. It draws inspiration from an existing project called [Brewfather](https://brewfather.app/). The primary objective is to develop a web application tailored for homebrewers, aiding them in efficiently managing their brewing processes.

The motivation behind choosing this project stems from personal experience, as the creator is a homebrewer seeking a self-hosted solution. Having ventured into self-hosting as a hobby, there is a desire to craft a web application specifically designed for managing the brewing process. The intention is to host this application on a personal server, avoiding reliance on subscription-based services such as Brewfather.

While several applications with similar functionalities already exist, this project aims to fulfill a specific niche by providing a self-hosted solution running within a Docker container.

## Structure
The repository is structured as follows:
* `.vscode`: Contains the settings for the Visual Studio Code IDE
* `app`: Contains the code for the application
* `docs`: Contains the documentation for the application
* `tests`: Contains the tests for the application
* `venv`: Contains the virtual environment for the application
* `.gitignore`: Contains the files and folders to be ignored by git
* `Makefile`: Contains the make commands for the application
* `README.md`: Contains the description of the repository
* `requirements.txt`: Contains the required packages for the application
* `setup.py`: Contains the setup for the application

## Installation
To install the application, please follow these steps:
1. Clone the repository
2. Create a virtual environment
3. Activate the virtual environment
4. Install the required packages
5. Run the application
6. Run the tests
7. Deactivate the virtual environment
8. Delete the virtual environment
9. Delete the repository

alternatively, you can use the make commands:
* `make install`: Creates a virtual environment, installs the required packages and runs the application
* `make test`: Runs the tests
* `make clean`: Deletes the virtual environment and the repository
* `make help`: Shows the help for the make commands
* `make all`: Runs all the make commands
