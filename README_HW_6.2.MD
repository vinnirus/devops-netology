### devops-10 student

### HW-6.2. SQL

---

1.<br>

```
sudo mkdir /pgdata
sudo mkdir /pgdata
docker run -d --name=pg -p 5432:5432 \
					-e POSTGRES_PASSWORD=secret \
					-e PGDATA=/pgdata \
					-v /pgdata:/pgdata \ 
					-v /pgbkp:/pgbkp \
					postgres:12
```

2.<br>

```
docker exec -it pg /bin/bash
root@a5877e48e2b7:/# su - postgres
postgres@a5877e48e2b7:~$ psql -a
```
```
postgres=# create database test_db;
CREATE DATABASE
postgres=# \c test_db 
You are now connected to database "test_db" as user "postgres".
test_db=# create table orders(id int primary key, name varchar, price real);
CREATE TABLE
test_db=# create table clients(id int primary key, surname varchar, country varchar, cl_order int references orders(id));
CREATE TABLE
test_db=# create index clnts_cntr_idx on clients(country);
CREATE INDEX
test_db=# create user test_admin_user;
CREATE ROLE
test_db=# grant all on orders, clients to test_admin_user;
GRANT
test_db=# grant select,update,insert,delete on orders,clients to test_simple_user;
GRANT
```
```
test_db=# select datname from pg_database;
  datname  
-----------
 postgres
 template1
 template0
 test_db
(4 rows)
```
```
test_db=# \d orders
                    Table "public.orders"
 Column |       Type        | Collation | Nullable | Default 
--------+-------------------+-----------+----------+---------
 id     | integer           |           | not null | 
 name   | character varying |           |          | 
 price  | real              |           |          | 
Indexes:
    "orders_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "clients" CONSTRAINT "clients_cl_order_fkey" FOREIGN KEY (cl_order) REFERENCES orders(id)
```
```
test_db=# \d clients
                    Table "public.clients"
  Column  |       Type        | Collation | Nullable | Default 
----------+-------------------+-----------+----------+---------
 id       | integer           |           | not null | 
 surname  | character varying |           |          | 
 country  | character varying |           |          | 
 cl_order | integer           |           |          | 
Indexes:
    "clients_pkey" PRIMARY KEY, btree (id)
    "clnts_cntr_idx" btree (country)
Foreign-key constraints:
    "clients_cl_order_fkey" FOREIGN KEY (cl_order) REFERENCES orders(id)
```
```
test_db=# SELECT grantee, table_catalog, table_schema, table_name, privilege_type FROM information_schema.table_privileges WHERE grantee like 'test_admin_user';
     grantee     | table_catalog | table_schema | table_name | privilege_type 
-----------------+---------------+--------------+------------+----------------
 test_admin_user | test_db       | public       | orders     | INSERT
 test_admin_user | test_db       | public       | orders     | SELECT
 test_admin_user | test_db       | public       | orders     | UPDATE
 test_admin_user | test_db       | public       | orders     | DELETE
 test_admin_user | test_db       | public       | orders     | TRUNCATE
 test_admin_user | test_db       | public       | orders     | REFERENCES
 test_admin_user | test_db       | public       | orders     | TRIGGER
 test_admin_user | test_db       | public       | clients    | INSERT
 test_admin_user | test_db       | public       | clients    | SELECT
 test_admin_user | test_db       | public       | clients    | UPDATE
 test_admin_user | test_db       | public       | clients    | DELETE
 test_admin_user | test_db       | public       | clients    | TRUNCATE
 test_admin_user | test_db       | public       | clients    | REFERENCES
 test_admin_user | test_db       | public       | clients    | TRIGGER
(14 rows)

test_db=# SELECT grantee, table_catalog, table_schema, table_name, privilege_type FROM information_schema.table_privileges WHERE grantee like 'test_simple_user';
     grantee      | table_catalog | table_schema | table_name | privilege_type 
------------------+---------------+--------------+------------+----------------
 test_simple_user | test_db       | public       | orders     | INSERT
 test_simple_user | test_db       | public       | orders     | SELECT
 test_simple_user | test_db       | public       | orders     | UPDATE
 test_simple_user | test_db       | public       | orders     | DELETE
 test_simple_user | test_db       | public       | clients    | INSERT
 test_simple_user | test_db       | public       | clients    | SELECT
 test_simple_user | test_db       | public       | clients    | UPDATE
 test_simple_user | test_db       | public       | clients    | DELETE
(8 rows)
```

3.<br>

```
test_db=# select count(1) from orders;
 count 
-------
     5
(1 row)

test_db=# select count(1) from clients;
 count 
-------
     5
(1 row)

```

4.</br> 

```
test_db=# update clients set cl_order = 3 where surname = 'Ivanov Ivan Ivanovich';
UPDATE 1

test_db=# update clients set cl_order = 4 where surname = 'Petrov Petr Petrovich';
UPDATE 1

test_db=# update clients set cl_order = 5 where surname = 'Iogan Sebastian Bax';
UPDATE 1

test_db=# select * from clients where cl_order is not null;
 id |        surname        | country | cl_order 
----+-----------------------+---------+----------
  1 | Ivanov Ivan Ivanovich | USA     |        3
  2 | Petrov Petr Petrovich | Canada  |        4
  3 | Iogan Sebastian Bax   | Japan   |        5
(3 rows)
```

5.</br>

```
test_db=# explain select * from clients where cl_order is not null;
                        QUERY PLAN                         
-----------------------------------------------------------
 Seq Scan on clients  (cost=0.00..18.10 rows=806 width=72)
   Filter: (cl_order IS NOT NULL)
(2 rows)

test_db=# explain analyze select * from clients where cl_order is not null;
                                             QUERY PLAN                                              
-----------------------------------------------------------------------------------------------------
 Seq Scan on clients  (cost=0.00..18.10 rows=806 width=72) (actual time=0.107..0.110 rows=3 loops=1)
   Filter: (cl_order IS NOT NULL)
   Rows Removed by Filter: 2
 Planning Time: 1.081 ms
 Execution Time: 0.356 ms
(5 rows)

```
Команда *explain* показывает план запроса, который строит планировщик запросов СУБД перед его выполнением. В данном примере мы видим, что СУБД будет последовательно читать все строки, т.к. на колонку *cl_order* не создан индекс.

6.</br>

```
postgres@40be47b8d4ac:~$ pg_dump test_db > /pgbkp/test_db.bkp
postgres@40be47b8d4ac:~$ ls /pgbkp/
test_db.bkp
postgres@40be47b8d4ac:~$ exit
logout
root@40be47b8d4ac:/# exit
exit
parallels@ubuntu-linux-20-04-desktop:/pgdata$ docker stop pg
pg

parallels@ubuntu-linux-20-04-desktop:/pgdata$ sudo -i
root@ubuntu-linux-20-04-desktop:~# ls -la /pgbkp
total 12
drwxrwxrwx  2 root             root             4096 Oct  7 00:58 .
drwxr-xr-x 22 root             root             4096 Oct  5 00:31 ..
-rw-r--r--  1 systemd-coredump systemd-coredump 2731 Oct  7 00:58 test_db.bkp
root@ubuntu-linux-20-04-desktop:~# exit
logout

parallels@ubuntu-linux-20-04-desktop:/pgdata$ docker run -d --name pg2 \
																											-e POSTGRES_PASSWORD=secret \
																											-e POSTGRES_USER=postgres \
																											-e PGDATA=/pgdata \
																											-p 6543:5432 \
																											-v /pgdata:/pgdata \
																											-v /pgbkp:/pgbkp \
																											postgres:12
																											
6870b2b67091271d34b5a026e1fd61f20145cfbbe623a9c479b51195c50bd74e

parallels@ubuntu-linux-20-04-desktop:/pgdata$ docker exec -it pg2 /bin/bash

postgres@570dab79694b:~$ psql -c 'create database test_db'
CREATE DATABASE
postgres@570dab79694b:~$ psql -d test_db -f /pgbkp/test_db.bkp 
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
CREATE TABLE
ALTER TABLE
COPY 5
COPY 5
ALTER TABLE
ALTER TABLE
CREATE INDEX
ALTER TABLE
psql:/pgbkp/test_db.bkp:111: ERROR:  role "test_simple_user" does not exist
psql:/pgbkp/test_db.bkp:112: ERROR:  role "test_admin_user" does not exist
psql:/pgbkp/test_db.bkp:119: ERROR:  role "test_simple_user" does not exist
psql:/pgbkp/test_db.bkp:120: ERROR:  role "test_admin_user" does not exist

postgres@570dab79694b:~$ psql
psql (12.8 (Debian 12.8-1.pgdg110+1))
Type "help" for help.

postgres=# \c test_db
You are now connected to database "test_db" as user "postgres".
test_db=# select count(1) from clients ;
 count 
-------
     5
(1 row)
```
