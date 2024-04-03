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

This requirements.txt file should only contain the packages required for the application to run. If you are developing the application, you should create a separate requirements file for development packages. This will help to keep the dependencies clean and organized. You can create a development requirements file by running the following command:

```bash
pip freeze > requirements-dev.txt
```

1. Run the application

```bash
uvicorn main:app --reload
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
POSTGRES_PORT=5455
POSTGRES_NAME=HoppyBrew_DB
```

Once the environment variables are set, you need to make sure that you use the correct debugger, which is `Python Debugger: Debug using launch.json` in the debugger dropdown.

## 2.1 Installation and run using Docker

### 2.1.1 Prerequisites

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
git clone https://github.com/asbor/iu-project-software-engineering.git
```

This repository comes with further instructions on steps which are to taken.

build the docker image

```docker
docker build -t docker-hoppy-brew-app-image .
```

have a look at which images you have, you can use the following command to list your images in the terminal, or alternatively have a look in the Docker IDE

```docker
docker images
```

In case you wish to `remove` the image again, you can use the following command

```docker
docker rmi docker-hoppy-brew-app
```

ps: the `docker-hoppy-brew-app` is the name of the image, which you can find in the list of images.

```docker
docker ps
```

Stop the container

```docker
docker stop docker-hoppy-brew-app-container
```

Remove the container

```docker
docker rm docker-hoppy-brew-app-container
```

Run a new container with the following environment variables

Environment variable    | Description               | Example
---                     | ---                       | ---
POSTGRES_HOST           | IP of database server     | 127.0.0.1
POSTGRES_PORT           | Port of database          | 5455
POSTGRES_NAME           | Name of the database      | HoppyBrew_DB
POSTGRES_USER           | Database user             | postgres
POSTGRES_PASSWORD       | Password                  | postgres


Run the application

> **NOTE !**
> 
> It turnes out that it was quite dificult to be able to establish a connection between the API and the database, and the issue was for some reason caused by the `POSTGRES_HOST` parameter. Supposetly under normal circumstances, the POSTGRES_HOST would function fine by using the IP-Address `172.17.0.1`. but for some reason this was not possible, which is why we needed to enter `host.docker.internal`.

```docker
docker run -d -p 127.0.0.1:8000:8000 --env NAME=Dexter --name docker-hoppy-brew-app-container docker-hoppy-brew-app-image
```

```docker
docker run -d -p 127.0.0.1:8000:8000\
    --env NAME=Dexter\
    --env POSTGRES_HOST=host.docker.internal\
    --env POSTGRES_PORT=5455\
    --env POSTGRES_NAME=HoppyBrew_DB\
    --env POSTGRES_USER=postgres\
    --env POSTGRES_PASSWORD=postgres\
    --name docker-hoppy-brew-app-container docker-hoppy-brew-app-image
```

> *`host.docker.internal` exists only in **Windows WSL** because **Docker Desktop for Windows** runs Docker daemon inside the special **WSL VM Docker-Desktop**. It has its own `localhost` and its own `WSL2 interface` to communicate with Windows. **This VM has no static IP**. The IP is generated every time when VM is created and passed via host.docker.internal in the generated /etc/hosts to every distro. Although there is no bridge or real v-switch all ports opened on eth0 of VM internal network are mapped on the host Local network, BUT NOT ON THE ETH0 OF THE HOST. There is no real bridge and port mapping - nothing to configure. Inside WSL VM its Localhost is the same as the localhost of the Linux machine. 2 processes inside WSL VM can communicate via localhost. Cross-distro IPC must use host.docker.internal. It is possible to create bridge inside WSL VM -Docker does it.*
>
> Source: https://stackoverflow.com/questions/48546124/what-is-linux-equivalent-of-host-docker-internal#:~:text=on%20this%20post.-,host.,interface%20to%20communicate%20with%20Windows.

see also: https://blog.devgenius.io/connect-locally-hosted-postgresql-from-docker-daffea720af1

### 2.2.3 Access the application

Open a web browser and navigate to `http://127.0.0.1:8000/` or `http://0.0.0.0:8000/` or `http://localhost:8000/`. This will open the application, and you can start using it. It should be noted that this works while running ubuntu, and im not sure if it will work on windows.

### 2.2.4 Swagger UI

In case you wish to access the documentation, you can do so by navigating to the following URL: `http://localhost:8000/docs`. This will open the Swagger UI, which is a tool that allows you to interact with the API. You can test the endpoints and see the responses.

### 2.2.5 Redoc documentation

Also, you can access the redoc documentation by navigating to the following URL: `http://localhost:8000/redoc`. This will open the redoc documentation, which is another tool that allows you to interact with the API. You can test the endpoints and see the responses.

### 2.2.4 Create a new docker container for the PostgreSQL server

we can also create a new docker container for the PostgreSQL server and interconnect the containers. This can be done by running the following command:

```docker
docker run --name HoppyBrew_DB \
    -p 5455:5432 \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_PASSWORD=postgres \
    -e POSTGRES_DB=postgres \
    -d postgres:latest
```

This will create a new docker container with the name `HoppyBrew_DB` and expose the port `5455` to the host machine. The environment variables `POSTGRES_USER`, `POSTGRES_PASSWORD`, and `POSTGRES_DB` are set to `postgres`, `postgres`, and `postgres` respectively. The container is based on the `postgres:latest` image.

## 3.1 Publish the docker image to Docker Hub

### 3.1.1 Prerequisites

You need to have a Docker Hub account. If you don't have one, you can create one at https://hub.docker.com/. You also need to have Docker installed on your machine. Once you have Docker installed, you can log in to your Docker Hub account by running the following command:

```docker
docker login
```

### 3.1.2 Tag the docker image

To publish the docker image `docker-hoppy-brew-app-container` to Docker Hub, you need to tag the image with your Docker Hub username. You can do this by running the following command:

- Usage:  docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]

```docker
docker tag docker-hoppy-brew-app-image asbjornbordoy/docker-hoppy-brew-app-image
```

This will tag the image `docker-hoppy-brew-app-image` with the username `asbjornbordoy` and the image name `docker-hoppy-brew-app-image`. You can verify that the image has been tagged correctly by running the following command:

```docker
docker images
```

You should see the tagged image in the list of images. If you have tagged the image incorrectly, you can remove the tag by running the following command:

```docker
docker rmi asbor/docker-hoppy-brew-app-image
```

once you have tagged the image correctly, you can push the image to Docker Hub by running the following command:

```docker
docker push asbjornbordoy/docker-hoppy-brew-app-image
```

This will push the image to Docker Hub. You can verify that the image has been pushed successfully by logging in to your Docker Hub account and navigating to the repository.

