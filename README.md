# devops-netology
devops-10 student

HW-3.1. Работа в терминале, лекция 1

п.4:
PS C:\projects\vagrant> vagrant status
Current machine states:

default                   running (virtualbox)

The VM is running. To stop this VM, you can run `vagrant halt` to
shut it down forcefully, or you can run `vagrant suspend` to simply
suspend the virtual machine. In either case, to restart it again,
simply run `vagrant up`.

п.5:
Vagrant settings = VirtualBox default settings:
RAM = 1024 Mb
CPU = 2
Video = 4 Mb
HDD = 64 Gb

п.8:
Длина журнала задается переменной HISTSIZE. Номер строки  1178.
echo $HISTSIZE
1000

Директива ignoreboth объединяет директивы ignorespace и ignoredups. Т.е. в журнал не попадут команды, которые начинаются с пробела или повторяют предыдущую команду.

п.9
{ list; } - список команд, разделенных точкой с запятой;
a{d,c,b}e = ade, ace, abe - перечисление возможных значений для механизма создания произвольных строк;

п.10
vagrant@vagrant:~$ touch file{1..300000}
-bash: /usr/bin/touch: Argument list too long
vagrant@vagrant:~$ touch file{1..100000}
vagrant@vagrant:~$ ls | wc -l
100000

п.11
Конструкция [[ -d /tmp ]] возвращает 0 или 1, в зависимости от того, существует ли файл /tmp и является ли он директорией/

п.12
vagrant@vagrant:/usr/bin$ export PATH="/tmp/netology/:/usr/local/bin/:/bin/:$PATH"
vagrant@vagrant:/usr/bin$ type -a bash
bash is /tmp/netology/bash
bash is /usr/local/bin/bash
bash is /bin/bash
bash is /usr/bin/bash
bash is /bin/bash
vagrant@vagrant:/usr/bin$

п.13
at - выполняет команды в указанное время
batch - выполняет команды когда средняя загрузка падает ниже заданного значения.
