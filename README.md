# 1. Introduction & Project Overview

This project is part of the Software Engineering course at the Faculty of Informatics, International University of Applied Sciences Bad Honnef - Bonn. It draws inspiration from an existing project called [Brewfather](https://brewfather.app/). The primary objective is to develop a web application tailored for home-brewers, aiding them in efficiently managing their brewing processes.

The motivation behind choosing this project stems from personal experience, as the creator is a homebrewer seeking a self-hosted solution. Having ventured into self-hosting as a hobby, there is a desire to craft a web application specifically designed for managing the brewing process. The intention is to host this application on a personal server, avoiding reliance on subscription-based services such as Brewfather.

While several applications with similar functionalities already exist, this project aims to fulfill a specific niche by providing a self-hosted solution running within a Docker container.

## 1.1 Installation and run on local machine

These instructions will are based on Linux and MacOS. The application can be run on Windows as well, but the commands may differ slightly.

## 1.2 Prerequisites

* Install Python 3.8 or higher

### 1.2.1 Prepare the virtual environment

1. Clone the repository

```bash
git clone https://github.com/asbor/iu-project-software-engineering.git
```

1. Change into the project directory

```bash
cd iu-project-software-engineering
```

1. Create a virtual environment

```bash
python3 -m venv .venv
```

1. Activate the virtual environment

```bash
source .venv/bin/activate
```

1. Install the required packages

```bash
pip install -r requirements.txt
```

**Note:**

This requirements.txt file should only contain the packages required for the application to run.

1. Run the application

```bash
uvicorn app.main:app --reload
```

1. Open a web browser and navigate to `http://127.0.0.1:8000/`

2. To stop the application, press `Ctrl + C`

**NOTE!:** You need to make sure that the environment variables are set correctly in your local environment. There are multiple approaches to setting environment variables, such as using a `.env` file or in VSCode, you can set them in the `launch.json` file.

#### Setting environment variables

To set the environment in VSCode, you can add the following configuration to the `launch.json` file:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env" // Use the .env file
        }
    ]
}
```

Then, create a `.env` file in the root directory of the project and add the following environment variables:

```bash
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5434
POSTGRES_NAME=HoppyBrew_DB
```

Once the environment variables are set, you need to make sure that you use the correct debugger, which is `Python Debugger: Debug using launch.json` in the debugger dropdown.

## 2.1 Installation and run using Docker

## 2.2 Prerequisites

* Install Python 3.8 or higher
* Install Docker

### 2.2.1 Install Docker

To install Docker on Ubuntu, follow the instructions on the official Docker website: https://docs.docker.com/engine/install/ubuntu/

### 2.2.2 Build the docker-image and Create docker-container based on example repository

Confirm that you have docker installed

```docker
docker -v
```


navigate to the project folder, and clone the GitHub example repository

```git
git clone  
```

This repository comes with further instructions on steps which are to taken.

build the docker image

```docker
docker build -t dockerfile . 
```

have a look at which images you have, you can use the following command to list your images in the terminal, or alternatively have a look in the Docker IDE

```docker
docker images
```

Run a new container with the following environment variables

Environment variable    | Description               | Example
---                     | ---                       | ---
DATABASE_HOST           | IP of database server     | 127.0.0.1
DATABASE_PORT           | Port of database          | 5432
DATABASE_NAME           | Name of the database      | dbs
DATABASE_USER           | Database user             | xstudent
DATABASE_PASSWORD       | Password                  | SuperSecret

Run the application

> **NOTE !**
> 
> It turnes out that it was quite dificult to be able to establish a connection between the API and the database, and the issue was for some reason caused by the `DATABASE_HOST` parameter. Supposetly under normal circumstances, the DATABASE_HOST would function fine by using the IP-Address `172.17.0.1`. but for some reason this was not possible, which is why we needed to enter `host.docker.internal`.

```docker
docker run -d -p 127.0.0.1:8000:8000 --env NAME=Dexter --env DATABASE_HOST=host.docker.internal --env DATABASE_PORT=5432 --env DATABASE_NAME=postgres --env DATABASE_USER=postgres --env DATABASE_PASSWORD=postgres --name dbs-python dbs-python-example
postgres
```

> *`host.docker.internal` exists only in **Windows WSL** because **Docker Desktop for Windows** runs Docker daemon inside the special **WSL VM Docker-Desktop**. It has its own `localhost` and its own `WSL2 interface` to communicate with Windows. **This VM has no static IP**. The IP is generated every time when VM is created and passed via host.docker.internal in the generated /etc/hosts to every distro. Although there is no bridge or real v-switch all ports opened on eth0 of VM internal network are mapped on the host Local network, BUT NOT ON THE ETH0 OF THE HOST. There is no real bridge and port mapping - nothing to configure. Inside WSL VM its Localhost is the same as the localhost of the Linux machine. 2 processes inside WSL VM can communicate via localhost. Cross-distro IPC must use host.docker.internal. It is possible to create bridge inside WSL VM -Docker does it.*
>
> Source: https://stackoverflow.com/questions/48546124/what-is-linux-equivalent-of-host-docker-internal#:~:text=on%20this%20post.-,host.,interface%20to%20communicate%20with%20Windows.

see also: https://blog.devgenius.io/connect-locally-hosted-postgresql-from-docker-daffea720af1

to see which containers we have we can

```docker
    docker ps
```

we can also create a new docker container for the PostgreSQL server and interconnect the contaioners. 

```docker
docker run --name myPostgresDb -p 5455:5432 -e POSTGRES_USER=postgresUser -e POSTGRES_PASSWORD=postgresPW -e POSTGRES_DB=postgresDB -d postgres
```





### Running the tests








It then creates a non-root user "**dbs**", sets the working directory to `/home/dbs`, copies the local files into the container, installs Python dependencies listed in `requirements.txt`, exposes port 8000, and finally runs a command to start the application using Uvicorn, a fast ASGI server, to serve the `dbs_assignment` application with auto-reload enabled on all network interfaces.

**The Alpine Linux Docker Container**: The container is based on Alpine Linux, a lightweight Linux distribution. The container is designed to be as small as possible, making it ideal for running applications in resource-constrained environments. The container is built using the Dockerfile in the root directory of the repository.

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
