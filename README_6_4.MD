### devops-10 student

### HW-6.4. PostgreSQL

---

1.<br>

```
parallels@ubuntu-linux-20-04-desktop:~$ docker run -d --name=pg_13 -p 4432:5432 -e POSTGRES_PASSWORD=secret -e PGDATA=/pgdata -v /pgdata13:/pgdata -v /pgbkp13:/pgbkp postgres:13
91ffd76e6e8f53091c88233a65b43088f326f4011e8e8be0173a3d42741d1e41
parallels@ubuntu-linux-20-04-desktop:~$ docker ps
CONTAINER ID   IMAGE         COMMAND                  CREATED         STATUS         PORTS                                       NAMES
91ffd76e6e8f   postgres:13   "docker-entrypoint.s…"   7 seconds ago   Up 6 seconds   0.0.0.0:4432->5432/tcp, :::4432->5432/tcp   pg_13

parallels@ubuntu-linux-20-04-desktop:~$ docker exec -it pg_13 /bin/bash

root@91ffd76e6e8f:/# su - postgres

postgres@91ffd76e6e8f:~$ psql 

psql (13.4 (Debian 13.4-4.pgdg110+1))
Type "help" for help.
```
```
postgres=# \?
...
postgres=# \l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges
   
-----------+----------+----------+------------+------------+--------------------
---
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres        
  +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres        
  +
           |          |          |            |            | postgres=CTc/postgres
(3 rows)

postgres=# \connect postgres
You are now connected to database "postgres" as user "postgres".

postgres=# \d
Did not find any relations.

postgres-# \d table
Did not find any relation named "table".

postgres-# \q
postgres@91ffd76e6e8f:~$
```
2.<br>

```
postgres=# CREATE DATABASE test_database;
CREATE DATABASE
```
```
postgres@91ffd76e6e8f:/pgbkp$ pg_restore -C -d test_database /pgbkp/test_dump.sql 
pg_restore: error: input file appears to be a text format dump. Please use psql.
```
```
postgres@91ffd76e6e8f:/pgbkp$ psql -d test_database -f test_dump.sql 
SET
SET
SET
SET
SET
 set_config 
------------
 
(1 row)

SET
SET
SET
SET
SET
SET
CREATE TABLE
ALTER TABLE
CREATE SEQUENCE
ALTER TABLE
ALTER SEQUENCE
ALTER TABLE
COPY 8
 setval 
--------
      8
(1 row)

ALTER TABLE
postgres@91ffd76e6e8f:/pgbkp$
```
```
test_database=# analyze VERBOSE orders;
INFO:  analyzing "public.orders"
INFO:  "orders": scanned 1 of 1 pages, containing 8 live rows and 0 dead rows; 8 rows in sample, 8 estimated total rows
ANALYZE
```
```
test_database=# select attname, avg_width from pg_stats where tablename='orders' order by avg_width desc limit 1;
 attname | avg_width 
---------+-----------
 title   |        16
(1 row)
```
3.<br>

```
begin;
create table orders_1 (
		check (price > 499)
		) inherits (orders);
create table orders_2 (
		check (price <= 499)
		) inherits (orders);
commit;
```
Да, мы могли бы изначально спроектировать таблицу, использую декларативное секционирование таблицы. В этом случае мы должны создать таблицу *orders* как секционированную, используя ключевое слово *PARTITION*:

```
CREATE TABLE public.orders (
	id serial4 NOT NULL,
	title varchar(80) NOT NULL,
	price int4 NULL DEFAULT 0,
	CONSTRAINT orders_pkey PRIMARY KEY (id)
) PARTITION BY RANGE (price);
```
 Затем нам необходимо создать секции, учитывающие разбиение по цене:

 ```
 CREATE TABLE orders_2 PARTITION OF orders
    FOR VALUES FROM (1) TO (500);
    
 CREATE TABLE orders_1 PARTITION OF orders
    FOR VALUES FROM (500);
 ```
4.</br> 

```
postgres@91ffd76e6e8f:~$ pg_dump test_database > 20211020_test_database.backup

postgres@91ffd76e6e8f:~$ ls
20211020_test_database.backup
```
[Ссылка на бекап](https://github.com/vinnirus/devops-netology/blob/main/20211020_test_database.backup)
