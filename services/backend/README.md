# Docker

```docker
docker run --name myPostgresDb -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgresDB -d postgres
```

## Build

```bash
docker build -t dbs-python-example .
```

## Run

```bash
docker run -p 127.0.0.1:8000:8000 --env NAME=Dexter --name dbs-python-example-container dbs-python-example
```

# Unit Test

## Create a .venv

```bash
python3 -m venv .venv
```

## Activate the .venv

```bash
source .venv/bin/activate
```

## Install the requirements

```bash
pip install -r requirements.txt
```
