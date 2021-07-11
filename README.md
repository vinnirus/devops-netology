# devops-netology
devops-10 student

HW-3.2. Работа в терминале, лекция 2

п.1:
parallels@ubuntu-linux-20-04-desktop:~$ type cd
cd is a shell builtin
cd является командой, встроенной в оболочку.
Команда man cd говорит, что внешняя реализация cd допустима, но представляет собой сценарий с тем же именем, что и используемая в сценарии команда.

п.2
grep -c <some_string> <some_file>

п.3
systemd

parallels@ubuntu-linux-20-04-desktop:~$ pstree -p
systemd(1)─┬─ModemManager(40662)─┬─{ModemManager}(40665)
           │                     └─{ModemManager}(40669)
           ├─NetworkManager(223482)─┬─{NetworkManager}(223517)
           │                        └─{NetworkManager}(223518)


п.4
root@ubuntu-linux-20-04-desktop:~# ls /wrong_dir 2>/dev/pts/1

п.5:
less input.file
first line
second line
3 line

sort < input.file > output.file

less output.file
3 line
first line
second line

п.6
Перенаправить данные из pty в tty возможно, но наблюдать вывод не получится.
*Т.к. перенаправление происходит на другое устройство вывода, для того, чтобы наблюдать вывод в реальном времени, необходимо переключиться на это устройство.

п.7:
Командой bash 5>&1 мы определили еще один дескриптор с номером 5 (дескрипторы с 3 по 9 являются undefined и позволяют программе самой определять их поведение) затем перенаправили его поток в stdout.
Далее мы записали строку netology в файловый дескриптор с номером 5, который выводит свой поток в stdout.

п.8
vagrant@vagrant:~$ ls /proc/$$/fd
0  1  2  255
vagrant@vagrant:~$ bash 5>&1
vagrant@vagrant:~$ bash 2>&1
vagrant@vagrant:~$ bash 2>&5
vagrant@vagrant:~$ ls /proc/$$/fd
0  1  2  255  5
vagrant@vagrant:~$ ls wrong_dir | less

п.9
Результатом выполнения команды станет вывод переменных окружения для текущего пользователя, что является эквивалентом вызову команды env.

п.10
/proc/[pid]/cmdline - неизменяемый файл, который содержит полную командную строку для процесса при условии, что этот процесс не является зомби-процессом.ъ
/proc/[pid]/exe - файл является символической ссылкой, указывающей на актуальный путь для выполняющейся команды.

п.11
Выполняю работу на macbook m1, который не поддерживает sse инструкции, поэтому привожу пример для RHEL6.4 для x86_64:
cat /proc/cpuinfo | grep sse
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts mmx fxsr sse sse2 ss ht syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts xtopology tsc_reliable nonstop_tsc aperfmperf unfair_spinlock pni pclmulqdq ssse3 cx16 sse4_1 sse4_2 popcnt aes xsave avx hypervisor lahf_lm ida arat epb pln pts dts

Старшая версия sse = sse4_2

п.12
По умолчанию, когда я запускаю команду на удаленной машине, используя ssh, процесс TTY не инициируется для удаленной сессии. Это позволяет передавать двоичные данные без необходимости использовать териминал. Для того, чтобы изменить это поведение необходимо просто подключиться к удаленной сессии по протоколу ssh и авторизоваться в системе:
ssh vagrant@127.0.0.1

п.13
1. vagrant@vagrant:~$ tail -f bash.man.txt
2. vagrant@vagrant:~$ screen -S 'session for reptyr'
3. vagrant@vagrant:~$ ps aux | grep tail
vagrant     1491  0.0  0.0   8112   596 pts/3    S+   15:12   0:00 tail -f bash.man.txt
vagrant     1496  0.0  0.0   8900   672 pts/4    S+   15:13   0:00 grep --color=auto tail
4. vagrant@vagrant:~$ reptyr -s 1491
5. ctrl+A, D - для выхода из screen
6. vagrant@vagrant:~$ ps aux | grep tail
vagrant     1491  0.0  0.1   8112  1912 pts/2    Ss+  15:12   0:00 tail -f bash.man.txt
vagrant     1525  0.0  0.0      0     0 pts/3    Z    15:21   0:00 [tail] <defunct>
vagrant     1534  0.0  0.0   8900   664 pts/0    S+   15:23   0:00 grep --color=auto tail
7. vagrant@vagrant:~$ kill 1525
  
п.14
Программа tee копирует данные из stdin в stdout. В случае с командой sudo echo string > /root/new_file перенаправление происходит под текущим пользователем, а в случае c командой echo string | sudo tee /root/new_file сразу происходит запуск программы tee с правами суперпользователя и которой на вход передается вывод echo string.
