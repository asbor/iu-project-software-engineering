# README

This document describes how to get the project up and running. The document is developed based on Ubuntu 24.04 LTS.

## 1. Prerequisites

### 1.1 Install Git

Install the following tools via the terminal:

```bash
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install git
```
Here is the reworked set of instructions to include the necessary steps for installing Docker, Docker Compose, and setting appropriate permissions:

### 1.2 Install Docker and Docker Compose

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

## 2. Clone the project


```bash
git clone https://gitlab.com/asbor1/iu-project-software-engineering.git
```

Yoy will need to enter your **username** and **password** to clone the project via HTTPS. And you will also have to get an invitation to the project.

Once the project is downloaded, you can open it in VS Code or any other IDE of your choice.

```bash
code iu-project-software-engineering
```

## 3. The initial setup of the project

In the initial setup of the project, we will first have to create a virtual environment for the project. The virtual environment is used to isolate the project dependencies from the system dependencies.

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


## 3. Unit testing

To run the unit tests, you can run the following command:

```bash
pytest
```

## 4. Running the backend services using Docker Compose


```bash
docker-compose up
```

## 5. Running the frontend services

```bash
cd services/nuxt3-shadcn/
yarn && yarn dev
```

## 6. Accessing the application

You can access the application by visiting the following URL in your browser:


[http://localhost:3000/](http://localhost:3000/)

