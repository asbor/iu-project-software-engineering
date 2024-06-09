# Project Setup Guide

Welcome to the Project Setup Guide. This document provides comprehensive instructions for setting up and running the project on Ubuntu 24.04 LTS. Whether you are a new contributor or an experienced developer, this guide will help you get the project up and running quickly and efficiently. 

The guide offers two setup options:
1. **Quick Start**: For users who want to get started immediately using the provided Makefile.
2. **Manual Setup**: For those who prefer detailed, step-by-step instructions to understand and control the setup process.

## README

### Overview

This project includes both backend and frontend components that need to be set up and run in parallel for development and testing purposes. The backend runs with Docker Compose, while the frontend runs as a separate instance in a development environment. This configuration ensures that the frontend can seamlessly communicate with the backend during development.

### Temporary Development Setup

Currently, the backend is managed by Docker Compose, but the frontend is not fully integrated into this setup. This temporary arrangement is due to recent issues preventing the frontend from running correctly within Docker Compose, despite it working previously. As a result, the frontend and backend run separately but are interconnected for testing purposes.

The long-term goal is to have both the frontend and backend managed within a single Docker Compose setup, simplifying the deployment and management process. For now, this temporary solution ensures that development and testing can proceed smoothly.

Follow the instructions in this guide to set up your development environment and get the project running. If you encounter any issues, consult the project documentation or contact the maintainers for support.


## Quick Start

To quickly set up the project, use the provided Makefile. Run the following command in the project root directory:

```bash
make install
```

This command will install all dependencies and start the project. Access the project at [http://localhost:3000/](http://localhost:3000/).

## Manual Setup

Follow these steps to manually set up the project.

### 1. Prerequisites

#### 1.1 Install Git

Update your package list and install Git:

```bash
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install git
```

#### 1.2 Install Docker and Docker Compose

1. Install necessary dependencies:
    ```bash
    sudo apt install -y curl
    ```

2. Install Docker:
    ```bash
    sudo apt install -y docker.io
    ```

3. Download Docker Compose:
    ```bash
    sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    ```

4. Make Docker Compose executable:
    ```bash
    sudo chmod +x /usr/local/bin/docker-compose
    ```

5. Add `/usr/local/bin` to your `PATH`:
    ```bash
    export PATH=$PATH:/usr/local/bin
    ```

6. Verify Docker Compose installation:
    ```bash
    docker-compose --version
    ```

7. (Optional) Make the `PATH` update permanent:
    ```bash
    echo 'export PATH=$PATH:/usr/local/bin' >> ~/.bashrc
    source ~/.bashrc
    ```

8. Add your user to the Docker group:
    ```bash
    sudo usermod -aG docker $USER
    ```

9. Log out and log back in or restart your system to apply the changes.

### 2. Clone the Project

Clone the project repository:

```bash
git clone https://gitlab.com/asbor1/iu-project-software-engineering.git
```

Open the project in your preferred IDE:

```bash
code iu-project-software-engineering
```

### 3. Initial Setup

#### 3.1 Create and Activate a Virtual Environment

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

### 4. Running the Project

#### 4.1 Running Backend Services with Docker Compose

Start the backend services:

```bash
docker-compose up
```

#### 4.2 Running Frontend Services

Navigate to the frontend directory and start the services:

```bash
cd services/nuxt3-shadcn/
yarn && yarn dev
```

### 5. Accessing the Application

Open the following URL in your browser to access the application:

[http://localhost:3000/](http://localhost:3000/)

### 6. Running Unit Tests

To run the unit tests:

```bash
pytest
```

## Conclusion

By following this guide, you can efficiently set up and run the project on Ubuntu 24.04 LTS. The instructions cover both a quick setup using `make install` for simplicity and a detailed manual setup process for greater control and understanding.

The current configuration involves running the backend with Docker Compose and the frontend in a separate development environment. This setup ensures seamless integration between the frontend and backend during development and testing. In future updates, the goal is to fully integrate the frontend into the Docker Compose setup, simplifying deployment and management.

If you encounter any issues or have questions during the setup process, please refer to the project documentation or reach out to the project maintainers. This setup guide aims to streamline your development process and ensure you can quickly get the project up and running. Thank you for contributing to the project, and happy coding!

