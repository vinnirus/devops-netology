# devops-netology
devops-10 student

HW-3.7. Компьютерные сети, лекция 2

**************
Использовал виртуализацию parallels c ВМ ubuntu 20.04 для arm64
**************

п.1
parallels@ubuntu-linux-20-04-desktop:~$ ip link show

1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 00:1c:42:bb:c7:a6 brd ff:ff:ff:ff:ff:ff
    
parallels@ubuntu-linux-20-04-desktop:~$ nmcli device status

DEVICE  TYPE      STATE      CONNECTION 
eth0    ethernet  unmanaged  --         
lo      loopback  unmanaged  -- 

parallels@ubuntu-linux-20-04-desktop:~$ netstat -i

Kernel Interface table
Iface      MTU    RX-OK RX-ERR RX-DRP RX-OVR    TX-OK TX-ERR TX-DRP TX-OVR Flg
eth0      1500     1479      0      0 0          1456      0      0      0 BMRU
lo       65536      437      0      0 0           437      0      0      0 LRU

п.2
Neighbor Discovery Protocol (NDP) — протокол из набора протоколов TCP/IP, используемый совместно с IPv6. Заменяет применяемые в IPv4 протоколы ARP, ICMP. Вместо использующихся в протоколе ARP широковещательных пакетов канального уровня используются групповые сообщения (multicast) не на канальном, а на сетевом уровне, что должно значительно снизить широковещательный трафик. Усовершенствованы функции протокола ICMP, облегчая работу разных подсетей в одном физическом сегменте. Включен механизм распознавания неисправных маршрутизаторов, что позволяет повысить устойчивость к сбоям оборудования. В дополнение к имевшимся ранее двум типам адресации — Unicast и Multicast (доставке уникальному получателю или группе получателей) — добавлен третий — Anycast, при котором осуществляется доставка любому получателю из группы.

Пакет называется libndp-tools
Команды npdtool, ndpmon

п.3
