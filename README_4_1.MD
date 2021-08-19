## devops-10 student

## HW-4.1. Командная оболочка Bash: практические навыки

---
### Использовал виртуализацию ***parallels*** c ВМ ubuntu 20.04 для arm64

1.

```
c=a+b
d=1+2
e=3
```

Такое поведение вызвано особенностями работы с арифметическими операциями, а именно при вычислении значения переменной d bash извлечет из памяти значения переменных *a* и *b*, и запишет в переменную d строку *"1+2"*, в случае с переменной *e* имеет место арифметическая подстановка, при которой bash сначала вычислит значение в скобках, а затем присвоит его переменной *e*. Запись `$(($a + $b))` эквивалентна записи `$((a+b))`, предпочтительным является второй вариант,т.к.  он более читаем. Переменная c вернет строку `a+b`.

2.
В примере допущена синтаксическая ошибка в виде отсутствующей закрывающей скобки.
Кроме того, оператор `((` является аналогом оператора `let` и используется в арифметических операциях, для корректной работы скрипта следует использовать квадратные скобки `[[` или оператор `test`:

```
while [ 1==1 ]
do
    curl -s -k https://localhost:443
    if [ $? != 0 ]
    then
        date >> curl.log
        sleep 1
    fi
done
```
Примечание - в моем случае скрипт одинаково правильно работал как с `((` так и с `[[`, а именно - писал в файл только в случае недоступности *apache2*

3.

```
parallels@ubuntu-linux-20-04-desktop:~$ vim check_health.sh 

#!/bin/bash
for ip in $@
do
    for i in {1..5}
    do
        echo "iteration $i for $ip" >> /home/parallels/log
        nc -zv $ip 80  >>  /home/parallels/log 2>&1
    done
done


parallels@ubuntu-linux-20-04-desktop:~$ chmod 700 check_health.sh

parallels@ubuntu-linux-20-04-desktop:~$ ./check_health.sh 192.168.0.1 173.194.222.113 87.250.250.242

parallels@ubuntu-linux-20-04-desktop:~$ cat log

iteration 1 for 192.168.0.1
nc: connect to 192.168.0.1 port 80 (tcp) failed: Connection refused
iteration 2 for 192.168.0.1
nc: connect to 192.168.0.1 port 80 (tcp) failed: Connection refused
iteration 3 for 192.168.0.1
nc: connect to 192.168.0.1 port 80 (tcp) failed: Connection refused
iteration 4 for 192.168.0.1
nc: connect to 192.168.0.1 port 80 (tcp) failed: Connection refused
iteration 5 for 192.168.0.1
nc: connect to 192.168.0.1 port 80 (tcp) failed: Connection refused
iteration 1 for 173.194.222.113
Connection to 173.194.222.113 80 port [tcp/http] succeeded!
iteration 2 for 173.194.222.113
Connection to 173.194.222.113 80 port [tcp/http] succeeded!
iteration 3 for 173.194.222.113
Connection to 173.194.222.113 80 port [tcp/http] succeeded!
iteration 4 for 173.194.222.113
Connection to 173.194.222.113 80 port [tcp/http] succeeded!
iteration 5 for 173.194.222.113
Connection to 173.194.222.113 80 port [tcp/http] succeeded!
iteration 1 for 87.250.250.242
Connection to 87.250.250.242 80 port [tcp/http] succeeded!
iteration 2 for 87.250.250.242
Connection to 87.250.250.242 80 port [tcp/http] succeeded!
iteration 3 for 87.250.250.242
Connection to 87.250.250.242 80 port [tcp/http] succeeded!
iteration 4 for 87.250.250.242
Connection to 87.250.250.242 80 port [tcp/http] succeeded!
iteration 5 for 87.250.250.242
Connection to 87.250.250.242 80 port [tcp/http] succeeded!

```
4.

```
parallels@ubuntu-linux-20-04-desktop:~$ vim ./check_status_repeat.sh
#!/bin/bash
while :
do
  for ip in $@
  do
    nc -vz $ip 80
    if [ $? -eq 1 ] ;then
      echo $(date) has problem in $ip >> /home/parallels/error
      exit 6
    fi
  done
done

parallels@ubuntu-linux-20-04-desktop:~$ ./test.sh 173.194.222.113 87.250.250.242 192.168.1.0

Connection to 173.194.222.113 80 port [tcp/http] succeeded!
Connection to 87.250.250.242 80 port [tcp/http] succeeded!
nc: connect to 192.168.1.0 port 80 (tcp) failed: Connection refused

parallels@ubuntu-linux-20-04-desktop:~$ cat error

Fri 13 Aug 2021 01:41:09 PM MSK has problem in 192.168.1.0
```
