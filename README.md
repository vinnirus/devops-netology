# devops-netology
##cdevops-10 student

##cHW-3.8. Компьютерные сети, лекция 3

**************
Использовал виртуализацию parallels c ВМ ubuntu 20.04 для arm64
**************

1.
  parallels@ubuntu-linux-20-04-desktop:~$ telnet route-views.routeviews.org
  Trying 128.223.51.103...
  Connected to route-views.routeviews.org.
  Escape character is '^]'.
  C
  **********************************************************************

                      RouteViews BGP Route Viewer
                      route-views.routeviews.org

   route views data is archived on http://archive.routeviews.org

   This hardware is part of a grant by the NSF.
   Please contact help@routeviews.org if you have questions, or
   if you wish to contribute your view.

   This router has views of full routing tables from several ASes.
   The list of peers is located at http://www.routeviews.org/peers
   in route-views.oregon-ix.net.txt

   NOTE: The hardware was upgraded in August 2014.  If you are seeing
   the error message, "no default Kerberos realm", you may want to
   in Mac OS X add "default unset autologin" to your ~/.telnetrc

   To login, use the username "rviews".

   **********************************************************************

  User Access Verification

  Username: rviews

  route-views>sh ip route 128.69.187.233

  Routing entry for 128.68.0.0/14, supernet
    Known via "bgp 6447", distance 20, metric 0
    Tag 3303, type external
    Last update from 217.192.89.50 3w2d ago
    Routing Descriptor Blocks:
    * 217.192.89.50, from 217.192.89.50, 3w2d ago
        Route metric is 0, traffic share count is 1
        AS Hops 3
        Route tag 3303
        MPLS label: none
        
  route-views>sh bgp 128.69.187.233

  BGP routing table entry for 128.68.0.0/14, version 181278844
  Paths: (25 available, best #11, table default)
    Not advertised to any peer
    Refresh Epoch 1
    20912 3257 3356 3216 3216 3216 8402
      212.66.96.126 from 212.66.96.126 (212.66.96.126)
        Origin IGP, localpref 100, valid, external
        Community: 3257:8070 3257:30515 3257:50001 3257:53900 3257:53902 20912:65004
        path 7FE1253652C8 RPKI State not found
        rx pathid: 0, tx pathid: 0
    Refresh Epoch 1
    3267 2603 3216 8402
      194.85.40.15 from 194.85.40.15 (185.141.126.1)
        Origin IGP, metric 0, localpref 100, valid, external
        path 7FE18C983988 RPKI State not found
        rx pathid: 0, tx pathid: 0
    Refresh Epoch 1
    3333 12859 3216 8402
      193.0.0.56 from 193.0.0.56 (193.0.0.56)
        Origin IGP, localpref 100, valid, external
       Community: 3216:1000 3216:1004 3216:2001 8402:900 8402:904 8402:905 12859:1000 12859:1100
        path 7FE13E26DAC0 RPKI State not found
        rx pathid: 0, tx pathid: 0
    Refresh Epoch 1
    3561 3910 3356 3216 3216 3216 8402
      206.24.210.80 from 206.24.210.80 (206.24.210.80)
        Origin IGP, localpref 100, valid, external
        path 7FE118F9F5E8 RPKI State not found
        rx pathid: 0, tx pathid: 0
    Refresh Epoch 1
    7018 3356 3216 3216 3216 8402
      12.0.1.63 from 12.0.1.63 (12.0.1.63)
        Origin IGP, localpref 100, valid, external
        Community: 7018:5000 7018:37232
        path 7FE0D7827888 RPKI State not found
        rx pathid: 0, tx pathid: 0
    Refresh Epoch 1
    6939 3216 8402
      64.71.137.241 from 64.71.137.241 (216.218.252.164)
        Origin IGP, localpref 100, valid, external
        path 7FE1071D8358 RPKI State not found
        rx pathid: 0, tx pathid: 0
    Refresh Epoch 1
    3549 3356 3216 3216 3216 8402
      208.51.134.254 from 208.51.134.254 (67.16.168.191)
        Origin IGP, metric 0, localpref 100, valid, external
        Community: 3216:1000 3216:1004 3216:2001 3356:2 3356:22 3356:100 3356:123 3356:503 3356:903 3356:2067 3549:2581 3549:30840 8402:900 8402:904 8402:905
        path 7FE148788AC8 RPKI State not found
        rx pathid: 0, tx pathid: 0
    Refresh Epoch 1
    3356 3216 3216 3216 8402
      4.68.4.46 from 4.68.4.46 (4.69.184.201)
        Origin IGP, metric 0, localpref 100, valid, external
        Community: 3216:1000 3216:1004 3216:2001 3356:2 3356:22 3356:100 3356:123 3356:503 3356:903 3356:2067 8402:900 8402:904 8402:905
        path 7FE0C7080D98 RPKI State not found
        rx pathid: 0, tx pathid: 0
    Refresh Epoch 1
    701 3356 3216 3216 3216 8402
      137.39.3.55 from 137.39.3.55 (137.39.3.55)
        Origin IGP, localpref 100, valid, external
        path 7FE15B3A16C8 RPKI State not found
        rx pathid: 0, tx pathid: 0
    Refresh Epoch 1
    53767 14315 6453 6453 3356 3216 3216 3216 8402
      162.251.163.2 from 162.251.163.2 (162.251.162.3)
        Origin IGP, localpref 100, valid, external
        Community: 14315:5000 53767:5000
        path 7FE17191CC08 RPKI State not found
        rx pathid: 0, tx pathid: 0
    Refresh Epoch 2
    3303 3216 8402

  parallels@ubuntu-linux-20-04-desktop:~$ sudo ip route add 172.16.10.0/24 dev dummy0
  parallels@ubuntu-linux-20-04-desktop:~$ ip route show

default via 10.211.55.1 dev eth0 proto dhcp src 10.211.55.5 metric 100 
10.211.55.0/24 dev eth0 proto kernel scope link src 10.211.55.5 
10.211.55.1 dev eth0 proto dhcp scope link src 10.211.55.5 metric 100 
172.16.10.0/24 dev dummy0 scope link 


2.
  parallels@ubuntu-linux-20-04-desktop:/etc/network$ sudo ip link add name dummy0 type dummy
  parallels@ubuntu-linux-20-04-desktop:/etc/network$ sudo ip link set dummy0 up

  parallels@ubuntu-linux-20-04-desktop:/etc/network$ ip link show
  1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
      link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
  2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
      link/ether 00:1c:42:bb:c7:a6 brd ff:ff:ff:ff:ff:ff
  3: dummy0: <BROADCAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
      link/ether 96:84:b2:c2:2b:7f brd ff:ff:ff:ff:ff:ff

  parallels@ubuntu-linux-20-04-desktop:~$ sudo ip route add 172.16.10.0/24 dev dummy0

  parallels@ubuntu-linux-20-04-desktop:~$ ip route show

  default via 10.211.55.1 dev eth0 proto dhcp src 10.211.55.5 metric 100 
  10.211.55.0/24 dev eth0 proto kernel scope link src 10.211.55.5 
  10.211.55.1 dev eth0 proto dhcp scope link src 10.211.55.5 metric 100 
  172.16.10.0/24 dev dummy0 scope link 

3.
  parallels@ubuntu-linux-20-04-desktop:~$ sudo netstat -tpln

  Active Internet connections (only servers)
  Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
  tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      486/systemd-resolve 
  tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN      18661/cupsd         
  tcp6       0      0 ::1:631                 :::*                    LISTEN      18661/cupsd 

systemd-resolve: 
>служба systemd, выполняющая разрешение сетевых имён для локальных приложений 

cupsd: 
>служба общей системы печати, которая управляет заданиями печати и обеспечивает сетевую печать

4.
  parallels@ubuntu-linux-20-04-desktop:~$ sudo netstat -upln
   
  Active Internet connections (only servers)
  Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
  udp        0      0 0.0.0.0:5353            0.0.0.0:*                           531/avahi-daemon: r 
  udp        0      0 0.0.0.0:631             0.0.0.0:*                           18662/cups-browsed  
  udp        0      0 0.0.0.0:59205           0.0.0.0:*                           531/avahi-daemon: r 
  udp        0      0 127.0.0.53:53           0.0.0.0:*                           486/systemd-resolve 
  udp        0      0 10.211.55.5:68          0.0.0.0:*                           291/systemd-network 
  udp6       0      0 :::5353                 :::*                                531/avahi-daemon: r 
  udp6       0      0 fe80::21c:42ff:febb:546 :::*                                291/systemd-network 
  udp6       0      0 :::45989                :::*                                531/avahi-daemon: r

avahi-daemon:
>служба, обеспечивающая обнаружение сервисов в локальной сети

systemd-network:
>служба, управляющая сетевыми настройками

5.
http://joxi.ru/Vm6E9jkFRKVEGr
