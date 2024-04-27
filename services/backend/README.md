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
