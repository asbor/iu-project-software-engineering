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
DATABASE_HOST           | IP of database server     | 127.0.0.1
DATABASE_PORT           | Port of database          | 5455
DATABASE_NAME           | Name of the database      | hoppybrew_db
DATABASE_USER           | Database user             | postgres
DATABASE_PASSWORD       | Password                  | postgres


Run the application

> **NOTE !**
> 
> It turnes out that it was quite dificult to be able to establish a connection between the API and the database, and the issue was for some reason caused by the `DATABASE_HOST` parameter. Supposetly under normal circumstances, the DATABASE_HOST would function fine by using the IP-Address `172.17.0.1`. but for some reason this was not possible, which is why we needed to enter `host.docker.internal`.

```docker
docker run -d -p 127.0.0.1:8000:8000 --env NAME=Dexter --name docker-hoppy-brew-app-container docker-hoppy-brew-app-image
```

```docker
docker run -d -p 127.0.0.1:8000:8000\
    --env NAME=Dexter\
    --env DATABASE_HOST=host.docker.internal\
    --env DATABASE_PORT=5455\
    --env DATABASE_NAME=hoppybrew_db\
    --env DATABASE_USER=postgres\
    --env DATABASE_PASSWORD=postgres\
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
docker run --name hoppybrew_db_Cont \
    -p 5455:5432 \
    -e DATABASE_USER=brewer \
    -e DATABASE_PASSWORD=password \
    -e DATABASE_DB=hoppybrew_db \
    -d postgres:latest
```

This will create a new docker container with the name `hoppybrew_db` and expose the port `5455` to the host machine. The environment variables `DATABASE_USER`, `DATABASE_PASSWORD`, and `DATABASE_DB` are set to `postgres`, `postgres`, and `postgres` respectively. The container is based on the `postgres:latest` image.
