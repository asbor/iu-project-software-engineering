# To build and run the container using this Dockerfile:

https://stackoverflow.com/questions/25540711/docker-postgres-pgadmin-local-connection


## Build PGAdmin4 Docker Image

```bash
docker run \
  -p 5050:80 \
  -e "PGADMIN_DEFAULT_EMAIL=name@example.com" \
  -e "PGADMIN_DEFAULT_PASSWORD=admin" \
  -d dpage/pgadmin4
```

## Connection string for PgAdmin
Enter PgAdmin on localhost:80. Then add a server with:
```bash
name: container-postgresdb
host: host.docker.internal
database: postgres
user: postgres
password: admin
```