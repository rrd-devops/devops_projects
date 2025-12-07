
#Goal 
Run PostgreSQL container with a named volume, create table and data, delete container, start new container with same volume, verify data persistent.

Create a docker volume
```bash
docker volume create pgdata_assign2
