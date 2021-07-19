# devops-netology
devops-10 student

HW-3.3. Операционные системы, лекция 1

п.1
strace -o /home/vagrant/strace.out /bin/bash -c 'cd /tmp'
less /home/vagrant/strace.out

chdir("/tmp")                           = 0

п.2
/usr/share/misc/magic.mgc

п.3
vagrant@vagrant:~/big_file$ rm file.bigsize

vagrant@vagrant:~/big_file$ ps aux | grep less
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
vagrant     4183  0.0  0.2   8436  2628 pts/3    T    14:42   0:00 less +F big_file/file.bigsize
vagrant     4196  0.0  0.0   8900   676 pts/0    S+   14:43   0:00 grep --color=auto less

vagrant@vagrant:~/big_file$ lsof | grep deleted
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
less      4183                       vagrant    3r      REG              253,0 2
147483648     131092 /home/vagrant/big_file/file.bigsize (deleted)

vagrant@vagrant:~/big_file$ ls -l /proc/4183/fd | grep bigsize
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
lr-x------ 1 vagrant vagrant 64 Jul 15 14:43 3 -> /home/vagrant/big_file/file.bigsize (deleted)

vagrant@vagrant:~/big_file$ df -h
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Filesystem                  Size  Used Avail Use% Mounted on
udev                        447M     0  447M   0% /dev
tmpfs                        99M  664K   98M   1% /run
/dev/mapper/vgvagrant-root   62G  3.6G   55G   7% /
tmpfs                       491M     0  491M   0% /dev/shm
tmpfs                       5.0M     0  5.0M   0% /run/lock
tmpfs                       491M     0  491M   0% /sys/fs/cgroup
/dev/sda1                   511M  4.0K  511M   1% /boot/efi
tmpfs                        99M     0   99M   0% /run/user/1000

vagrant@vagrant:~/big_file$ truncate -s 0 /proc/4183/fd/3
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
vagrant@vagrant:~/big_file$ df -h
Filesystem                  Size  Used Avail Use% Mounted on
udev                        447M     0  447M   0% /dev
tmpfs                        99M  664K   98M   1% /run
/dev/mapper/vgvagrant-root   62G  1.6G   57G   3% /
tmpfs                       491M     0  491M   0% /dev/shm
tmpfs                       5.0M     0  5.0M   0% /run/lock
tmpfs                       491M     0  491M   0% /sys/fs/cgroup
/dev/sda1                   511M  4.0K  511M   1% /boot/efi
tmpfs                        99M     0   99M   0% /run/user/1000

п.4
Зомби процес не занимает память, но блокируют записи в таблице процессов, размер которой ограничен для каждого пользователя и системы в целом.

п.5
sudo strace -r -o ./strace.out /usr/sbin/opensnoop-bpfcc -d 1
less strace.out | grep "openat" | grep " = 3"  > strace.open.out
head -n 10 strace.open.out

     0.000254 openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
     0.000106 openat(AT_FDCWD, "/lib/aarch64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
     0.000104 openat(AT_FDCWD, "/lib/aarch64-linux-gnu/libpthread.so.0", O_RDONLY|O_CLOEXEC) = 3
     0.000149 openat(AT_FDCWD, "/lib/aarch64-linux-gnu/libdl.so.2", O_RDONLY|O_CLOEXEC) = 3
     0.000131 openat(AT_FDCWD, "/lib/aarch64-linux-gnu/libutil.so.1", O_RDONLY|O_CLOEXEC) = 3
     0.000136 openat(AT_FDCWD, "/lib/aarch64-linux-gnu/libm.so.6", O_RDONLY|O_CLOEXEC) = 3
     0.000142 openat(AT_FDCWD, "/lib/aarch64-linux-gnu/libexpat.so.1", O_RDONLY|O_CLOEXEC) = 3
     0.000037 openat(AT_FDCWD, "/lib/aarch64-linux-gnu/libz.so.1", O_RDONLY|O_CLOEXEC) = 3
     0.000056 openat(AT_FDCWD, "/usr/lib/locale/locale-archive", O_RDONLY|O_CLOEXEC) = 3
     0.000096 openat(AT_FDCWD, "/usr/lib/aarch64-linux-gnu/gconv/gconv-modules.cache", O_RDONLY) = 3

less strace.open.out | wc -l
953

п.6
uname({sysname="Linux", nodename="vagrant", ...}) = 0

также информацию можно посмотреть в соответствующем файле /proc/sys/kernel/{ostype, hostname, osrelease, version, domainname}
например,
cat /proc/sys/kernel/osrelease
5.4.0-66-genericn


п.7
Если первая команда завершилась с ошибкой, то при испльзовании ';' будет запущена вторая команда.
Если первая команда завершилась с ошибкой, то при испльзовании '&&' вторая команда не будет запущена.

Установка значения -e устанавливает поведение выполнения нескольких последовательных команд как немедленный выход если команда завершилась с ненулевым статусом. В этом случае использование ';' и '&&' приведет к одинаковому поведению.

п.8
-e = немедленный выход если команда завершилась с ненулевым кодом
-u = если передается переменная с неустановленным значением, выдается ошибка
-x = выводит команды и их аргументы во время их выполнения
-o pipefail = конвейер возвращает статус, отличный от нулевого для последней команды с таким статусом, либо ноль, если все команды выполнились с нулевым статусом.

Эти аргументы полезны при испльзовании в сценариях, т.к. набор обеспечивает визуализацию стадии выполнения скрипта (-х), прерывает дальнейшее выполнение, если предыдущая команда завершилась с ошибкой (-e), выполняет проверку на наличие значения в переменных.

п.9
vagrant@vagrant:~$ ps -ax -o stat | grep -c 'S'
66
vagrant@vagrant:~$ ps -ax -o stat | grep -c 'I'
47
vagrant@vagrant:~$ ps -ax -o stat | grep -c 'R'
1
vagrant@vagrant:~$ ps -ax -o stat | grep -c 'Z'
1
vagrant@vagrant:~$ ps -ax -o stat | grep -c 'T'
2

Т.о. наибольшее количество процессов находится в статусе S* (interruptible sleep), т.е. в ожидании завершения
