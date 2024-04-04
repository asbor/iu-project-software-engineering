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
  <a href="https://github.com/asbor/iu-project-software-engineering">
    <img src="images/logo.png" alt="Logo" width="300">
  </a>

<h3 align="center">HoppyBrew</h3>

  <p align="center">
    This project, part of the Software Engineering course at the Faculty of Informatics, International University of Applied Sciences Bad Honnef - Bonn, is inspired by Brewfather. It aims to develop a web app tailored for home-brewers to efficiently manage brewing processes. Motivated by personal experience as a homebrewer and interest in self-hosting, the creator seeks to provide a self-hosted alternative to subscription-based services like Brewfather. The project will be hosted on a personal server, running within a Docker container, to cater to a specific niche in brewing management.
    <br />
    <a href="https://github.com/asbor/iu-project-software-engineering"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/asbor/iu-project-software-engineering">View Demo</a>
    ·
    <a href="https://github.com/asbor/iu-project-software-engineering/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/asbor/iu-project-software-engineering/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
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

<img src="images/Brewmaster.webp" width="500" alt="HoppyBrew">

The project, undertaken as part of the Software Engineering course at the Faculty of Informatics, International University of Applied Sciences Bad Honnef - Bonn, seeks to develop a web application tailored for home-brewers. Inspired by the existing project Brewfather, the objective is to create a platform that assists brewers in efficiently managing their brewing processes. The project is motivated by personal experience, with the creator being a homebrewer looking for a self-hosted solution. By leveraging Docker containers, the aim is to provide a self-hosted alternative to subscription-based services like Brewfather, catering to a specific niche within the brewing community.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

The project is built using the following technologies:

| Frontend | Backend | Database | Containerization |
| --- | --- | --- | --- |
| [![Vue.js][Vue.js]][Vue-url] | [![Python][Python.org]][Python-url] | [![PostgreSQL][PostgreSQL.org]][PostgreSQL-url] | [![Docker.com][Docker.com]][Docker-url] |
| | [![Flask][Flask.pocoo]][Flask-url] | [![SQLite][SQLite]][SQLite-url] | [![Unraid][Unraid]][Unraid-url] |
| | [![FastAPI][FastAPI.org]][FastAPI-url] | [![Redis][Redis]][Redis-url] |  |
| | [![sqlalchemy][sqlalchemy]][sqlalchemy-url] | | |
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

## Structure

The project is structured as follows:

```plaintext
iu-project-software-engineering
├── api `FastAPI Application`
│   ├── __init__.py
│   ├── models `Pydantic Models`
│   │   ├── __init__.py
│   │   ├── beer.py 
│   │   ├── brew.py
│   │   ├── equipment.py
│   │   ├── fermentation.py
│   │   ├── ingredient.py
│   │   ├── recipe.py
│   │   └── user.py
│   ├── routes `API Endpoints`
│   │   ├── __init__.py
│   │   ├── beer.py
│   │   ├── brew.py
│   │   ├── equipment.py
│   │   ├── fermentation.py
│   │   ├── ingredient.py
│   │   ├── recipe.py
│   │   └── user.py
│   └── utils `Utility Functions`
│       ├── __init__.py
│       ├── database.py
│       └── hashing.py
├── app `Flask Application`
│   ├── __init__.py
│   ├── main.py
│   └── settings.py
├── db `Database Migrations`
│   ├── __init__.py
│   ├── base.py
│   ├── models `SQLAlchemy Models`
│   │   ├── __init__.py
│   │   ├── beer.py
│   │   ├── brew.py
│   │   ├── equipment.py
│   │   ├── fermentation.py
│   │   ├── ingredient.py
│   │   ├── recipe.py
│   │   └── user.py
│   └── schemas `Pydantic Schemas`
│       ├── __init__.py
│       ├── beer.py
│       ├── brew.py
│       ├── equipment.py
│       ├── fermentation.py
│       ├── ingredient.py
│       ├── recipe.py
│       └── user.py
├── tests `Unit Tests`
│   ├── __init__.py
│   ├── test_beer.py
│   ├── test_brew.py
│   ├── test_equipment.py
│   ├── test_fermentation.py
│   ├── test_ingredient.py
│   ├── test_recipe.py
│   └── test_user.py
├── docker-compose.yml
├── Dockerfile
├── .env
├── .gitignore
├── LICENSE.txt
├── README.md
├── requirements.txt
└── .gitignore
```


---

## Local Deployment

### Prerequisites for Local Deployment

To run the project locally, you need to have the following software installed on your machine:

* Python 3.8 or higher
* Database (PostgreSQL or SQLite)

### Installation for Local Deployment

In order to run the application locally, follow the steps below:

Before you start, make sure you have the database set up. You can either use PostgreSQL or SQLite. If you choose to use PostgreSQL, make sure you have it installed on your machine. If you choose to use SQLite, you can skip this step.

Note: The following steps assume you are running locally on a Linux machine. If you are using a different operating system, the steps may vary.

#### PostgreSQL

1. Install PostgreSQL on your machine

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

2. Change directory to the project folder

    ```sh
    cd iu-project-software-engineering
    ```

3. Create a virtual environment

    ```sh
    python3 -m venv .venv
    ```

4. Activate the virtual environment

    ```sh
    source .venv/bin/activate
    ```

5. Install the required packages

    ```sh
    pip install -r requirements.txt
    ```

6. Run the project

    ```sh
    uvicorn main:app --reload
    ```

7. Open your browser and navigate to `http://localhost:8000`
8. You should see the project running

At this point, you should have the project running locally on your machine. You can now move on to the next steps to set up the database and start using the application.

To stop the project, press `Ctrl + C` in the terminal.

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
[product-screenshot]: images/screenshot.png
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


