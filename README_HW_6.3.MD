### devops-10 student

### HW-6.3. MySQL

---

1.<br>

```
docker run -d --name my_sql \
	    -e MYSQL_ROOT_PASSWORD=secret \
	    -v $HOME/netology/hw6.3/mysql_data:/var/lib/mysql \
	    mysql:8
```

```
docker exec -it my_sql /bin/bash
```
```
root@3eb3d64c7443:/# mysql -u root -p test_db
Enter password: 
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 30
Server version: 8.0.26 MySQL Community Server - GPL
```
```
mysql> \s
--------------
mysql  Ver 8.0.26 for Linux on x86_64 (MySQL Community Server - GPL)

Connection id:		31
Current database:	test_db
Current user:		root@localhost
SSL:			Not in use
Current pager:		stdout
Using outfile:		''
Using delimiter:	;
Server version:		8.0.26 MySQL Community Server - GPL
Protocol version:	10
Connection:		Localhost via UNIX socket
Server characterset:	utf8mb4
Db     characterset:	utf8mb4
Client characterset:	latin1
Conn.  characterset:	latin1
UNIX socket:		/var/run/mysqld/mysqld.sock
Binary data as:		Hexadecimal
Uptime:			33 min 50 sec

Threads: 5  Questions: 160  Slow queries: 0  Opens: 242  Flush tables: 3  Open tables: 161  Queries per second avg: 0.078
--------------
```
Server version:		8.0.26 MySQL Community Server - GPL </br>

```
mysql> source /var/lib/mysql/test_dump.sql
Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.04 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

Query OK, 0 rows affected (0.00 sec)
```

```
mysql> SHOW TABLE STATUS;
+--------+--------+---------+------------+------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+---------------------+------------+--------------------+----------+----------------+---------+
| Name   | Engine | Version | Row_format | Rows | Avg_row_length | Data_length | Max_data_length | Index_length | Data_free | Auto_increment | Create_time         | Update_time         | Check_time | Collation          | Checksum | Create_options | Comment |
+--------+--------+---------+------------+------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+---------------------+------------+--------------------+----------+----------------+---------+
| orders | InnoDB |      10 | Dynamic    |    5 |           3276 |       16384 |               0 |            0 |         0 |              6 | 2021-10-11 23:02:59 | 2021-10-11 23:02:59 | NULL       | utf8mb4_0900_ai_ci |     NULL |                |         |
+--------+--------+---------+------------+------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+---------------------+------------+--------------------+----------+----------------+---------+
1 row in set (0.00 sec)
```

```
mysql> use test_db;
Database changed
mysql> select * from orders where price>300;
+----+----------------+-------+
| id | title          | price |
+----+----------------+-------+
|  2 | My little pony |   500 |
+----+----------------+-------+
1 row in set (0.00 sec)
```

2.<br>

```
mysql> create user 'test' IDENTIFIED with mysql_native_password by 'test-pass' 
    -> WITH MAX_QUERIES_PER_HOUR 100
    -> password expire interval 180 day 
    -> FAILED_LOGIN_ATTEMPTS 3  
    -> ATTRIBUTE '{"fname": "James", "lname": "Pretty"}';
Query OK, 0 rows affected (0.02 sec)

```
```
mysql> grant select on test_db.* to test;
Query OK, 0 rows affected (0.00 sec)
```
```
mysql> SELECT * FROM INFORMATION_SCHEMA.USER_ATTRIBUTES WHERE `USER` LIKE 'test';
+------+------+---------------------------------------+
| USER | HOST | ATTRIBUTE                             |
+------+------+---------------------------------------+
| test | %    | {"fname": "James", "lname": "Pretty"} |
+------+------+---------------------------------------+
1 row in set (0.00 sec)
```

3.</br>

```
mysql> SET profiling=1;
Query OK, 0 rows affected, 1 warning (0.00 sec)

mysql> SHOW PROFILE;
+----------------+----------+
| Status         | Duration |
+----------------+----------+
| starting       | 0.000078 |
| Opening tables | 0.000029 |
| query end      | 0.000007 |
| closing tables | 0.000004 |
| freeing items  | 0.000010 |
| cleaning up    | 0.000022 |
+----------------+----------+

mysql> SELECT TABLE_NAME, ENGINE
    ->   FROM information_schema.TABLES
    ->  WHERE TABLE_SCHEMA = 'test_db' AND ENGINE IS NOT NULL;
+------------+--------+
| TABLE_NAME | ENGINE |
+------------+--------+
| orders     | InnoDB |
+------------+--------+
1 row in set (0.00 sec)

mysql> ALTER TABLE orders ENGINE = MyISAM;
Query OK, 5 rows affected (0.04 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> SELECT TABLE_NAME, ENGINE   FROM information_schema.TABLES  WHERE TABLE_SCHEMA = 'test_db' AND ENGINE IS NOT NULL;
+------------+--------+
| TABLE_NAME | ENGINE |
+------------+--------+
| orders     | MyISAM |
+------------+--------+
1 row in set (0.00 sec)


mysql> SET profiling=1;
Query OK, 0 rows affected, 1 warning (0.00 sec)

mysql> SELECT * FROM orders WHERE price>100;
+----+-----------------------+-------+
| id | title                 | price |
+----+-----------------------+-------+
|  2 | My little pony        |   500 |
|  3 | Adventure mysql times |   301 |
|  4 | Server gravity falls  |   300 |
|  5 | Log gossips           |   123 |
+----+-----------------------+-------+
4 rows in set (0.00 sec)

mysql> UPDATE orders SET price=301 WHERE id=3;
Query OK, 0 rows affected (0.00 sec)
Rows matched: 1  Changed: 0  Warnings: 0

mysql> SHOW PROFILE;
+--------------------------------+----------+
| Status                         | Duration |
+--------------------------------+----------+
| starting                       | 0.000076 |
| Executing hook on transaction  | 0.000003 |
| starting                       | 0.000032 |
| checking permissions           | 0.000007 |
| Opening tables                 | 0.000036 |
| init                           | 0.000005 |
| System lock                    | 0.000037 |
| updating                       | 0.000028 |
| end                            | 0.000003 |
| query end                      | 0.000004 |
| closing tables                 | 0.000006 |
| freeing items                  | 0.000012 |
| cleaning up                    | 0.000010 |
+--------------------------------+----------+
13 rows in set, 1 warning (0.00 sec)

mysql> ALTER TABLE orders ENGINE = InnoDB;
Query OK, 5 rows affected (0.04 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM orders WHERE price>100;
+----+-----------------------+-------+
| id | title                 | price |
+----+-----------------------+-------+
|  2 | My little pony        |   500 |
|  3 | Adventure mysql times |   301 |
|  4 | Server gravity falls  |   300 |
|  5 | Log gossips           |   123 |
+----+-----------------------+-------+
4 rows in set (0.00 sec)

mysql> UPDATE orders SET price=300 WHERE id=3;
Query OK, 1 row affected (0.02 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SHOW PROFILE;
+--------------------------------+----------+
| Status                         | Duration |
+--------------------------------+----------+
| starting                       | 0.000089 |
| Executing hook on transaction  | 0.000004 |
| starting                       | 0.000009 |
| checking permissions           | 0.000006 |
| Opening tables                 | 0.000046 |
| init                           | 0.000008 |
| System lock                    | 0.000092 |
| updating                       | 0.000151 |
| end                            | 0.000006 |
| query end                      | 0.000004 |
| waiting for handler commit     | 0.016003 |
| closing tables                 | 0.000030 |
| freeing items                  | 0.000023 |
| cleaning up                    | 0.000012 |
+--------------------------------+----------+
14 rows in set, 1 warning (0.00 sec)
```

4.</br>

```
# Copyright (c) 2017, Oracle and/or its affiliates. All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA

#
# The MySQL  Server configuration file.
#
# For explanations see
# http://dev.mysql.com/doc/mysql/en/server-system-variables.html

[mysqld]
pid-file        = /var/run/mysqld/mysqld.pid
socket          = /var/run/mysqld/mysqld.sock
datadir         = /var/lib/mysql
secure-file-priv= NULL

# Custom config should go here
!includedir /etc/mysql/conf.d/

#Размер буффера кеширования данных и индексов
innodb_buffer_pool_size=3Gb

#Размер файла-лога операций
innodb_log_file_size=100Mb

#Размер буффера, в который помещаются транзакции в незакомиченном состоянии
innodb_log_buffer_size=1Mb

#Tаблицы хранятся по разным файлам
innodb_file_per_table=ON

#Логика сброса данных на диск
innodb_flush_method=O_DSYNC

#Скорость IO важнее сохранности данных
innodb_flush_log_at_trx_commit=2
```
