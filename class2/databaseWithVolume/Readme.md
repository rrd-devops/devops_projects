
# Goal 
Run PostgreSQL container with a named volume, create table and data, delete container, start new container with same volume, verify data persistent.

Create a docker volume
```bash
docker volume create pgdata_assign2
```
```markdown
Start the Postgres container and mount the pgdata_assign2 inside as /var/lib/postgresql/data
```

```bash
docker run -d \
--name pg-assign2 \
-e POSTGRES_PASSWORD=secretpw \
-e POSTGRES_USER=bootcamp \
-e POSTGRES_DB=bootcampdb \
-v pgdata_assign2:/var/lib/postgresql/data \
-p 5432:5432 \
postgres:15
```
Add the movie names to the database
```bash
docker exec -it pg-assign2 psql -U bootcamp -d bootcampdb -c "CREATE TABLE movies (id SERIAL PRIMARY KEY, title TEXT, year INT);"
# insert data
docker exec -it pg-assign2 psql -U bootcamp -d bootcampdb -c "INSERT INTO movies (title, year) VALUES ('The Matrix',1999),('Inception',2010);"
# verify
docker exec -it pg-assign2 psql -U bootcamp -d bootcampdb -c "SELECT *
```
stop and delete the container
```bash
docker stop pg-assign2
docker rm pg-assign2
```
Start a new container and start with a different port
```bash
docker run -d \
--name pg-assign2-new \
-e POSTGRES_PASSWORD=secretpw \
-e POSTGRES_USER=bootcamp \
-e POSTGRES_DB=bootcampdb \
-v pgdata_assign2:/var/lib/postgresql/data \
-p 5433:5432 \
postgres:15
```
Check if the movie names are still available in the data base created with volume
```bash
docker exec -it pg-assign2-new psql -U bootcamp -d bootcampdb -c "SELECT * FROM movies;"
```
```markdown
 id |   title    | year 
----+------------+------
  1 | The Matrix | 1999
  2 | Inception  | 2010
(2 rows)
```
