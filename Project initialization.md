# README

This document describes how to get the project up and running. The document is develloped based on Ubuntu 24.04 LTS.

## Prerequisites

### Install Git

Install the following tools via the terminal:

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git
```
Here is the reworked set of instructions to include the necessary steps for installing Docker, Docker Compose, and setting appropriate permissions:

### Install Docker and Docker Compose

1. **Install necessary dependencies**:
    ```sh
    sudo apt install -y curl
    ```

2. **Install Docker**:
    ```sh
    sudo apt install -y docker.io
    ```

3. **Download Docker Compose binary**:
    ```sh
    sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    ```

4. **Make the Docker Compose binary executable**:
    ```sh
    sudo chmod +x /usr/local/bin/docker-compose
    ```

5. **Ensure `/usr/local/bin` is in your `PATH`**:
    ```sh
    export PATH=$PATH:/usr/local/bin
    ```

6. **Verify the Docker Compose installation**:
    ```sh
    docker-compose --version
    ```

7. **Make the `PATH` update permanent** (optional):
    ```sh
    echo 'export PATH=$PATH:/usr/local/bin' >> ~/.bashrc
    source ~/.bashrc
    ```

8. **Add your user to the Docker group**:
    ```sh
    sudo usermod -aG docker $USER
    ```

9. **Log out and log back in** to apply the group changes, or restart your system.

10. **Verify that your user is added to the Docker group**:
    ```sh
    groups $USER
    ```

11. **Run Docker Compose**:
    ```sh
    docker-compose up
    ```

Following these steps should ensure that Docker and Docker Compose are installed correctly and that you have the necessary permissions to run Docker commands.

### Git clone the project

```bash
git clone https://gitlab.com/asbor1/iu-project-software-engineering.git
```

Yoy will need to enter your username and password to clone the project via HTTPS. And you will also have to get an invitation to the project.

Once the project is downloaded, you can open it in VS Code or any other IDE of your choice.

```bash
code iu-project-software-engineering
```

### Unit testing

To run the unit tests, you will need to install the pytest package. Install the package via the terminal:

```bash
sudo apt install python3-pytest
```



## Running the project locally

To run the project locally, we will appearently first have to install the Python3-venv package. This package is not installed by default in Ubuntu 24.04 LTS. The package is required to create a virtual environment for the project.

Install the package via the terminal:
Create a virtual environment for the project:

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

The requirements are:

```bash
alembic
beautifulsoup4
fastapi
psycopg2-binary
pydantic
SQLAlchemy
SQLAlchemy-Utils
uvicorn
pandas
selenium
```


