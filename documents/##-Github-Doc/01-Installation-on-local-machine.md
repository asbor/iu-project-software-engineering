## 1.1 Installation and run on local machine

These instructions will are based on Linux and MacOS. The application can be run on Windows as well, but the commands may differ slightly.

### 1.1.1 Prerequisites

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
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=localhost
DATABASE_PORT=5455
DATABASE_NAME=hoppybrew_db
```

Once the environment variables are set, you need to make sure that you use the correct debugger, which is `Python Debugger: Debug using launch.json` in the debugger dropdown.
