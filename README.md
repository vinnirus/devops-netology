# devops-netology
devops-10 student

HW-3.2. Работа в терминале, лекция 2

п.1:
parallels@ubuntu-linux-20-04-desktop:~$ type cd
cd is a shell builtin

Команда man cd говорит, что внешняя реализация cd допустима, но представляет собой сценарий с тем же именем, что и используемая в сценарии команда.

п.2
grep -c <some_string> <some_file>

п.3
/sbin/init

parallels@ubuntu-linux-20-04-desktop:~$ ps aux | grep " 1 "
root           1  0.1  0.5 101876 10428 ?        Ss   23:01   0:01 /sbin/init

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
-----------------------------------------------------------------------------------

п.7:
Командой bash 5>&1 мы определили еще один дескриптор с номером 5 (дескрипторы с 3 по 9 являются undefined и позволяют программе самой определять их поведение) затем перенаправили его поток в stdout.
Далее мы записали строку netology в файловый дескриптор с номером 5, который выводит свой поток в stdout.

п.8
-------------------------------------------------------------------------------------

п.9
Результатом выполнения команды станет вывод переменных окружения для текущего пользователя, что является эквивалентом вызову команды env.

п.10
/proc/[pid]/cmdline - неизменяемый файл, который содержит полную командную строку для процесса при условии, что этот процесс не является зомби-процессом.ъ
/proc/[pid]/exe - файл является символической ссылкой, указывающей на актуальный путь для выполняющейся команды.

п.11
Выполняю работу на macbook m1, который не поддерживает sse инструкции, поэтому привожу пример для RHEL6.4 для x86:
cat /proc/cpuinfo | grep sse
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts mmx fxsr sse sse2 ss ht syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts xtopology tsc_reliable nonstop_tsc aperfmperf unfair_spinlock pni pclmulqdq ssse3 cx16 sse4_1 sse4_2 popcnt aes xsave avx hypervisor lahf_lm ida arat epb pln pts dts

Старшая версия sse = sse4_2



п.10
