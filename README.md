<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://gitlab.com/asbor/iu-project-software-engineering">
    <img src="documents/images/logo.png" alt="Logo" width="300">
  </a>

<h3 align="center">HoppyBrew</h3>

  <p align="center">
    This project, part of the Software Engineering course at the Faculty of Informatics, International University of Applied Sciences Bad Honnef - Bonn, is inspired by Brewfather. It aims to develop a web app tailored for home-brewers to efficiently manage brewing processes. Motivated by personal experience as a homebrewer and interest in self-hosting, the creator seeks to provide a self-hosted alternative to subscription-based services like Brewfather. The project will be hosted on a personal server, running within a Docker container, to cater to a specific niche in brewing management.
    <br />
    <a href="https://gitlab.com/asbor/iu-project-software-engineering"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://gitlab.com/asbor/iu-project-software-engineering">View Demo</a>
    ·
    <a href="https://gitlab.com/asbor/iu-project-software-engineering/-/issues/new?issuable_template=bug">Report Bug</a>
    ·
    <a href="https://gitlab.com/asbor/iu-project-software-engineering/-/issues/new?issuable_template=feature">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

---

## About The Project

<img src="documents/images/Brewmaster.webp" width="500" alt="HoppyBrew">

The project, undertaken as part of the Software Engineering course at the Faculty of Informatics, International University of Applied Sciences Bad Honnef - Bonn, seeks to develop a web application tailored for home-brewers. Inspired by the existing project Brewfather, the objective is to create a platform that assists brewers in efficiently managing their brewing processes. The project is motivated by personal experience, with the creator being a homebrewer looking for a self-hosted solution. By leveraging Docker containers, the aim is to provide a self-hosted alternative to subscription-based services like Brewfather, catering to a specific niche within the brewing community.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

The project is built using the following technologies:

| Frontend | Backend | Database | Containerization |
| --- | --- | --- | --- |
| [![Vue.js][Vue.js]][Vue-url] | [![Python][Python.org]][Python-url] | [![PostgreSQL][PostgreSQL.org]][PostgreSQL-url] | [![Docker.com][Docker.com]][Docker-url] |
| | [![sqlalchemy][sqlalchemy]][sqlalchemy-url] | [![SQLite][SQLite]][SQLite-url] | [![Unraid][Unraid]][Unraid-url] |
| | [![FastAPI][FastAPI.org]][FastAPI-url] | [![Redis][Redis]][Redis-url] |  |
| | [![pydantic][pydantic]][pydantic-url] | | |
| | [![uvicorn][uvicorn]][uvicorn-url] | | |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Tools

The project is developed using the following tools:

| IDE | Documentation | Version Control | Operating System |
| --- | --- | --- | --- |
| [![VsCode][VsCode]][VsCode-url] | [![Markdown][Markdown]][Markdown-url] | [![Git-scm][Git-scm]][Git-scm-url] | [![Ubuntu][Ubuntu]][Ubuntu-url] |
| | [![PlantUML][PlantUML]][PlantUML-url] | [![GitHub][GitHub]][GitHub-url] | [![Alpine Linux][Alpine Linux]][Alpine Linux-url] |
| | [![pandoc][pandoc]][pandoc-url] | [![DockerHub][dockerhub.com]][dockerhub-url] | [![Unraid][Unraid]][Unraid-url] |
| | [![gitbook][gitbook]][gitbook-url] | | |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- GETTING STARTED -->
## Getting Started

This project provides multiple ways to get started. You can either clone the repository and run the project locally or use the provided Docker container to run the project in a containerized environment. The following sections provide detailed instructions on how to get started with the project using the following three methods:

1. Local Deployment
2. Docker Deployment
3. Unraid Deployment (coming soon)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Local Deployment

### Prerequisites for Local Deployment

To run the project locally, you need to have the following software installed on your machine:

* Python 3.8 or higher
* Database PostgreSQL

### Installation for Local Deployment

In order to run the application locally, follow the steps below:

Before you start, make sure you have the database set up. You can either use PostgreSQL or SQLite. If you choose to use PostgreSQL, make sure you have it installed on your machine. If you choose to use SQLite, you can skip this step.

Note: The following steps assume you are running locally on a Linux machine. If you are using a different operating system, the steps may vary.

### The database

1. **Install PostgreSQL on your machine**

    ```sh
    sudo apt update
    sudo apt install postgresql postgresql-contrib
    ```

    The installation process will create a new user called `postgres` with the role `postgres`. It will also create a new system account with the same name. To use PostgreSQL, you need to log in as the `postgres` user.

    The HoppyBrew application will create a new database called `hoppybrew_db` upon startup. You can change the database name in the `.env` file.

    Should you chose to remove the database, you can do so by running the following command:

    ```sh
    sudo -u postgres psql -c "DROP DATABASE hoppybrew_db"
    ```

### The application

1. **Clone the repository**

    ```sh
    git clone
    ```

2. **Navigate to the project directory**

    ```sh
    cd iu-project-software-engineering
    ```

3. **Create a virtual environment**

    ```sh
    python3 -m venv .venv
    ```

4. **Activate the virtual environment**

    ```sh
    source .venv/bin/activate
    ```

5. **Install the required packages**

    ```sh
    pip install -r /docker/requirements.txt
    ```

6. **Run the project**

    ```sh
    uvicorn main:app --reload
    ```

7. **Open your browser and navigate to `http://localhost:8000`**
8. **You should see the project running**

At this point, you should have the project running locally on your machine. You can now move on to the next steps to set up the database and start using the application.

To stop the project, press `Ctrl + C` in the terminal.

## Docker Deployment

### Prerequisites for Docker Deployment

To run the project using Docker, you need to have the following software installed on your machine:

* Docker

### Installation for Docker Deployment

In order to run the application using Docker, follow the steps below:

1. **Run postgres database in a docker container**

    ```sh
    docker run --name hoppybrew-db -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -p 5432:5432 -d postgres
    ```
    Where:
    - `--name hoppybrew-db` specifies the name of the container
    - `-e POSTGRES_PASSWORD=postgres` specifies the password for the database
    - `-e POSTGRES_USER=postgres` specifies the username for the database
    - `-p 5432:5432` specifies the port mapping for the database
    - `-d postgres` specifies the image to use for the container
    - You can change the values for `POSTGRES_PASSWORD`, `POSTGRES_USER`, and `POSTGRES_DB` to suit your needs
    - You can also change the port mapping to a different port if needed

    This command will first pull the PostgreSQL image from Docker Hub and then run the container with the specified options.

2. **Build the Docker image for the application**

    ```sh
    docker build -t hoppybrew_image .
    ```

3. **Run the Docker container**

    ```sh
    docker run -d -p 127.0.0.1:8000:8000\
        --env NAME=HoppyBrew\
        --env DATABASE_HOST=host.docker.internal\
        --env DATABASE_PORT=5455\
        --env DATABASE_NAME=hoppybrew_db\
        --env DATABASE_USER=postgres\
        --env DATABASE_PASSWORD=postgres\
        --name hoppybrew_container hoppybrew_image
    ```

    Where:
    - `--name hoppybrew_container hoppybrew_image` specifies the name of the container and the image to use for the container
    - `-d` specifies that the container should run in detached mode
    - `-p -p 127.0.0.1:8000:8000` specifies the port mapping for the container
    - `--env NAME=HoppyBrew` specifies the name of the application
    - `--env DATABASE_HOST=host.docker.internal` specifies the host for the database container
    - `--env DATABASE_PORT=5455` specifies the port for the database container
    - `--env DATABASE_NAME=hoppybrew_db` specifies the name of the database
    - `--env DATABASE_USER=postgres` specifies the username for the database
    - `--env DATABASE_PASSWORD=postgres` specifies the password for the database

4. **Open your browser and navigate to [http://localhost:8000](http://localhost:8000)**
5. **You should see the project running**

At this point, you should have the project running in a Docker container on your machine. You can now move on to the next steps to set up the database and start using the application.

## Setting the environment variables as default values in the Dockerfile

Instead of passing the environment variables as command-line arguments when running the Docker container, you can set the default values in the Dockerfile. This way, you don't have to specify the environment variables every time you run the container.

As it turns out, you can not directly set the environment variables in the Dockerfile. This is because the environment variables are set at runtime, not at build time. However you create some arguments in the Dockerfile and then pass the arguments to the environment variables at runtime. Here's how you can do it:

![An overview of ARG and ENV availability.](https://vsupalov.com/images/docker-env-vars/docker_environment_build_args.png)

> Note: in the image, there is a rectangle around Dockerfile. This is a bit confusing. It should be around the “build image” step only. But that would be harder to read…

```Dockerfile
# Arguments for the environment variables
ARG NAME=HoppyBrew
ARG DATABASE_HOST=host.docker.internal
ARG DATABASE_PORT=5455
ARG DATABASE_USER=postgres
ARG DATABASE_PASSWORD=postgres

# Environment variables
ENV NAME $NAME
ENV DATABASE_HOST $DATABASE_HOST
ENV DATABASE_PORT $DATABASE_PORT
ENV DATABASE_USER $DATABASE_USER
ENV DATABASE_PASSWORD $DATABASE_PASSWORD
```

Now you can run the Docker container without specifying all the environment variables:

```sh
docker run -d -p 127.0.0.1:8000:8000 --name hoppybrew_container hoppybrew_image
```

The benefit with this approach is when you pull the image from Docker, the environment variables are already set with the default values. This is particularly useful when you pull the image to a unraid server, because Unraid is then able to generate a template for the container with the default values.

## Docker compose

To run the project using Docker Compose, follow the steps below:

1. **Create a `docker-compose.yml` file**

    ```yml
    version: '3.8'

    services:
      # This will create a PostgreSQL database service based on the official PostgreSQL image. If the image is not available locally, Docker will pull it from Docker Hub.
      hoppybrew-db:
        image: postgres
        environment:
          POSTGRES_PASSWORD: postgres
          POSTGRES_USER: postgres
          POSTGRES_DB: hoppybrew_db
        ports:
          - "5455:5432"

      # This will create an application service based on the Dockerfile in the current directory.
      hoppybrew-app:
        build: .
        environment:
          NAME: HoppyBrew
          DATABASE_HOST: hoppybrew-db
          DATABASE_PORT: 5455
          DATABASE_NAME: hoppybrew_db
          DATABASE_USER: postgres
          DATABASE_PASSWORD: postgres
        ports:
          - "8000:8000"
    ```
    Where:
    - `hoppybrew-db` is the name of the database service
    - `hoppybrew-app` is the name of the application service
    - `image: postgres` specifies the image to use for the database service
    - `build: .` specifies the build context for the application service
    - `environment` specifies the environment variables for the services
    - `ports` specifies the port mapping for the services
    - You can change the values for `POSTGRES_PASSWORD`, `POSTGRES_USER`, and `POSTGRES_DB` to suit your needs
    - You can also change the port mapping to a different port if needed
    - You can add additional services to the `docker-compose.yml` file as needed

2. **Run the Docker Compose stack**

    ```sh
    docker-compose up
    ```
    This command will first build the Docker image for the application and then run the Docker Compose stack with the specified services.


## FAQ

### ERROR: [Errno 98] Address already in use

This error occurs when the port you are trying to use is already in use by another process. To fix this error, you can either stop the process using the port or change the port number in the command.

### How do I change the port number?

To change the port number, you can add the `--port` flag followed by the port number you want to use. For example, to run the project on port 5000, you can use the following command:

```sh
uvicorn main:app --reload --port 5000
```

### How do i connect PGAdmin to the PostgreSQL database?

To connect PGAdmin to the PostgreSQL database, follow the steps below:

1. Open PGAdmin and click on the `Add New Server` button
2. Enter the connection details:
    - Hostname/Address: `localhost`
    - Port: `5432`
    - Maintenance Database: `hoppybrew`
    - Username: `username`
    - Password: `password`
3. Click `Save` to save the connection details
4. You should now see the new server listed in the left sidebar

### How do i distinguish between the local and docker postgres database?

To distinguish between the local and docker PostgreSQL databases, you can use different port numbers for the two databases. For example, you can use port 5432 for the local database and port 5455 for the docker database. This way, you can connect to the correct database based on the port number.

### What are the most frequently used Docker commands?

Here are some of the most frequently used Docker commands:

- `docker ps` - List all running containers
- `docker ps -a` - List all containers (running and stopped)
- `docker images` - List all images
- `docker build -t <image_name> .` - Build a Docker image
- `docker run -d -p <host_port>:<container_port> <image_name>` - Run a Docker container in detached mode
- `docker stop <container_id>` - Stop a running container
- `docker rm <container_id>` - Remove a stopped container
- `docker rmi <image_id>` - Remove an image
- `docker exec -it <container_id> /bin/bash` - Start a shell in a running container
- `docker logs <container_id>` - View the logs of a container
- `docker-compose up` - Start a Docker Compose stack
- `docker-compose down` - Stop a Docker Compose stack
- `docker-compose logs` - View the logs of a Docker Compose stack
- `docker-compose ps` - List all services in a Docker Compose stack
- `docker-compose exec <service_name> /bin/bash` - Start a shell in a service container






<p align="right">(<a href="#readme-top">back to top</a>)</p>




### Docker Deployment

#### Prerequisites for Docker Deployment

To run the project using Docker, you need to have the following software installed on your machine:

* Docker



### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/asbor/iu-project-software-engineering.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/asbor/iu-project-software-engineering/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/asbor/iu-project-software-engineering](https://github.com/asbor/iu-project-software-engineering)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/asbor/iu-project-software-engineering.svg?style=for-the-badge
[contributors-url]: https://github.com/asbor/iu-project-software-engineering/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/asbor/iu-project-software-engineering.svg?style=for-the-badge
[forks-url]: https://github.com/asbor/iu-project-software-engineering/network/members
[stars-shield]: https://img.shields.io/github/stars/asbor/iu-project-software-engineering.svg?style=for-the-badge
[stars-url]: https://github.com/asbor/iu-project-software-engineering/stargazers
[issues-shield]: https://img.shields.io/github/issues/asbor/iu-project-software-engineering.svg?style=for-the-badge
[issues-url]: https://github.com/asbor/iu-project-software-engineering/issues
[license-shield]: https://img.shields.io/github/license/asbor/iu-project-software-engineering.svg?style=for-the-badge
[license-url]: https://github.com/asbor/iu-project-software-engineering/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: www.linkedin.com/in/asbjørn-bordoy-89b0462a
[product-screenshot]: documents/images/screenshot.png
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Python-url]: https://www.python.org/
[Python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Flask.pocoo]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/2.0.x/
[Docker.com]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
[PostgreSQL.org]: https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white
[PostgreSQL-url]: https://www.postgresql.org/
[FastAPI.org]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
[FastAPI-url]: https://fastapi.tiangolo.com/
[Unraid]: https://img.shields.io/badge/Unraid-3776AB?style=for-the-badge&logo=unraid&logoColor=white
[Unraid-url]: https://unraid.net/
[sqlalchemy]: https://img.shields.io/badge/sqlalchemy-316192?style=for-the-badge&logo=sqlalchemy&logoColor=white
[sqlalchemy-url]: https://www.sqlalchemy.org/
[pydantic]: https://img.shields.io/badge/pydantic-005571?style=for-the-badge&logo=pydantic
[pydantic-url]: https://pydantic-docs.helpmanual.io/
[GitHub]: https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white
[GitHub-url]: https://github.com/asbor/iu-project-software-engineering
[Markdown]: https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white
[Markdown-url]: https://www.markdownguide.org/
[PlantUML]: https://img.shields.io/badge/PlantUML-000000?style=for-the-badge&logo=plantuml&logoColor=white
[PlantUML-url]: https://plantuml.com/
[pandoc]: https://img.shields.io/badge/pandoc-000000?style=for-the-badge&logo=pandoc&logoColor=white
[pandoc-url]: https://pandoc.org/
[dockerhub.com]: https://img.shields.io/badge/DockerHub-2496ED?style=for-the-badge&logo=docker&logoColor=white
[dockerhub-url]: https://hub.docker.com/
[gitbook]: https://img.shields.io/badge/GitBook-7B36ED?style=for-the-badge&logo=gitbook&logoColor=white
[gitbook-url]: https://www.gitbook.com/
[Alpine Linux]: https://img.shields.io/badge/Alpine_Linux-0D597F?style=for-the-badge&logo=alpinelinux&logoColor=white
[Alpine Linux-url]: https://alpinelinux.org/
[Ubuntu]: https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white
[Ubuntu-url]: https://ubuntu.com/
[uvicorn]: https://img.shields.io/badge/uvicorn-316192?style=for-the-badge&logo=uvicorn&logoColor=white
[uvicorn-url]: https://www.uvicorn.org/
[Git-scm]: https://img.shields.io/badge/Git-181717?style=for-the-badge&logo=git&logoColor=F05032
[Git-scm-url]: https://git-scm.com/
[VsCode]: https://img.shields.io/badge/Visual_Studio_Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white
[VsCode-url]: https://code.visualstudio.com/
[SQLite]: https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white
[SQLite-url]: https://www.sqlite.org/
[Redis]: https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white
[Redis-url]: https://redis.io/


