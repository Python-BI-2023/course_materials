# СУБД. SQL

## Поднимаем постгрес в докере

Для поднятия

```shell
docker run --rm --name demo_db -d -p 5432:5432 \
  -e POSTGRES_DB=demo \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=admin \
  postgres:14
```

Для работы в консольке

```shell
docker exec -it demo_db psql -U admin --dbname demo
```

Остановить бд

```shell
docker stop demo_db
```