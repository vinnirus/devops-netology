devops-10 student

HW-3.9. Элементы безопасности информационных систем

Использовал виртуализацию parallels c ВМ ubuntu 20.04 для arm64 и ВМ с KaliLinux для arm64, чтобы проверить подключение по ssh-ключу

1. и 2.
http://joxi.ru/L21qXg3czDkRB2

3.
parallels@ubuntu-linux-20-04-desktop:~$ sudo apt-get install apache2

parallels@ubuntu-linux-20-04-desktop:~$ service apache2 status

● apache2.service - The Apache HTTP Server
     Loaded: loaded (/lib/systemd/system/apache2.service; enabled; vendor preset: enabled)
     Active: active (running) since Thu 2021-08-12 14:06:11 MSK; 59min ago
       Docs: https://httpd.apache.org/docs/2.4/
   Main PID: 107446 (apache2)
      Tasks: 55 (limit: 2268)
     Memory: 5.5M
     CGroup: /system.slice/apache2.service
             ├─107446 /usr/sbin/apache2 -k start
             ├─107448 /usr/sbin/apache2 -k start
             └─107449 /usr/sbin/apache2 -k start

parallels@ubuntu-linux-20-04-desktop:~$ mkdir ~/ss
parallels@ubuntu-linux-20-04-desktop:~$ sudo openssl req -x509 -newkey rsa:2048 -days 365 -keyout /home/parallels/ssl/apache2_ssl.key -out /home/parallels/ssl/apache2_ssl.crt

parallels@ubuntu-linux-20-04-desktop:~/ssl$ sudo a2enmod ssl

Considering dependency setenvif for ssl:
Module setenvif already enabled
Considering dependency mime for ssl:
Module mime already enabled
Considering dependency socache_shmcb for ssl:
Enabling module socache_shmcb.
Enabling module ssl.
See /usr/share/doc/apache2/README.Debian.gz on how to configure SSL and create self-signed certificates.
To activate the new configuration, you need to run:
  systemctl restart apache2

parallels@ubuntu-linux-20-04-desktop:~/ssl$ sudo a2ensite default-ssl

Enabling site default-ssl.
To activate the new configuration, you need to run:
  systemctl reload apache2

parallels@ubuntu-linux-20-04-desktop:~$ sudo vim /etc/apache2/sites-enabled/default-ssl.conf 
После строки SSLEngine on добавляем строки:

SSLProtocol all -SSLv2

SSLCertificateFile      /home/parallels/ssl/apache2_ssl.crt
SSLCertificateKeyFile   /home/parallels/ssl/apache2_ssl.key

parallels@ubuntu-linux-20-04-desktop:~$ sudo service apache2 start

Enter passphrase for SSL/TLS keys for 127.0.1.1:443 (RSA): *********  

Результат проверки:
http://joxi.ru/p27jbpgtnZJlvm
http://joxi.ru/v29zXb7tRjg0vA

4.
parallels@ubuntu-linux-20-04-desktop:~/github/netology-devops10$ git clone --depth 1 https://github.com/drwetter/testssl.sh.git

Cloning into 'testssl.sh'...
remote: Enumerating objects: 96, done.
remote: Counting objects: 100% (96/96), done.
remote: Compressing objects: 100% (89/89), done.
remote: Total 96 (delta 13), reused 49 (delta 5), pack-reused 0
Unpacking objects: 100% (96/96), 8.60 MiB | 1.05 MiB/s, done.

parallels@ubuntu-linux-20-04-desktop:~/github/netology-devops10$ cd testssl.sh/
parallels@ubuntu-linux-20-04-desktop:~/github/netology-devops10/testssl.sh$ ./testssl.sh -e --fast --parallel https://www.google.com/

###########################################################
    testssl.sh       3.1dev from https://testssl.sh/dev/
    (f15da8d 2021-08-08 21:33:14 -- )

      This program is free software. Distribution and
             modification under GPLv2 permitted.
      USAGE w/o ANY WARRANTY. USE IT AT YOUR OWN RISK!

       Please file bugs @ https://testssl.sh/bugs/

###########################################################

 Using "OpenSSL 1.1.1f  31 Mar 2020" [~98 ciphers]
 on ubuntu-linux-20-04-desktop:/usr/bin/openssl
 (built: "Jul 23 12:32:42 2021", platform: "debian-arm64")


 Start 2021-08-12 15:26:25        -->> 216.58.209.164:443 (www.google.com) <<--

 rDNS (216.58.209.164):  bud02s21-in-f4.1e100.net. hem09s02-in-f4.1e100.net. bud02s21-in-f164.1e100.net.
 Service detected:       HTTP



 Testing all 98 locally available ciphers against the server, ordered by encryption strength 


Hexcode  Cipher Suite Name (OpenSSL)       KeyExch.   Encryption  Bits     Cipher Suite Name (IANA/RFC)
-----------------------------------------------------------------------------------------------------------------------------
./testssl.sh: line 1145: 120762 Segmentation fault      (core dumped) $OPENSSL s_client $(s_client_options "$proto -cipher "\'${ciphers_to_test:1}\'" -ciphersuites "\'${tls13_ciphers_to_test:1}\'" $STARTTLS $BUGS -connect $NODEIP:$PORT $PROXY $SNI") > $TMPFILE 2> $ERRFILE < /dev/null
 Oops: openssl s_client connect problem
 x1302   TLS_AES_256_GCM_SHA384            ECDH 253   AESGCM      256      TLS_AES_256_GCM_SHA384                             
 xc02c   ECDHE-ECDSA-AES256-GCM-SHA384     ECDH 253   AESGCM      256      TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384            
 xc030   ECDHE-RSA-AES256-GCM-SHA384       ECDH 253   AESGCM      256      TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384              
 xcca9   ECDHE-ECDSA-CHACHA20-POLY1305     ECDH 253   CHACHA20    256      TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256      
 xcca8   ECDHE-RSA-CHACHA20-POLY1305       ECDH 253   CHACHA20    256      TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256        
 xc00a   ECDHE-ECDSA-AES256-SHA            ECDH 253   AES         256      TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA               
 xc014   ECDHE-RSA-AES256-SHA              ECDH 253   AES         256      TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA                 
 x9d     AES256-GCM-SHA384                 RSA        AESGCM      256      TLS_RSA_WITH_AES_256_GCM_SHA384                    
 x35     AES256-SHA                        RSA        AES         256      TLS_RSA_WITH_AES_256_CBC_SHA                       
 xc02b   ECDHE-ECDSA-AES128-GCM-SHA256     ECDH 253   AESGCM      128      TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256            
 xc02f   ECDHE-RSA-AES128-GCM-SHA256       ECDH 253   AESGCM      128      TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256              
 xc009   ECDHE-ECDSA-AES128-SHA            ECDH 253   AES         128      TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA               
 xc013   ECDHE-RSA-AES128-SHA              ECDH 253   AES         128      TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA                 
 x9c     AES128-GCM-SHA256                 RSA        AESGCM      128      TLS_RSA_WITH_AES_128_GCM_SHA256                    
 x2f     AES128-SHA                        RSA        AES         128      TLS_RSA_WITH_AES_128_CBC_SHA                       


 Done 2021-08-12 15:26:40 [  17s] -->> 216.58.209.164:443 (www.google.com) <<--

5.
На ВМ с Kali Linux выполнил:

parallels@kali-linux:~$ ssh-keygen -t rsa

Generating public/private rsa key pair.
Enter file in which to save the key (/home/parallels/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/parallels/.ssh/id_rsa
Your public key has been saved in /home/parallels/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:1t2M35qcGzBGBSFqxKEevwVpWSDux0anSKHUG4+jMdY parallels@ubuntu-linux-20-04-desktop
The key's randomart image is:
+---[RSA 3072]----+
|    ..o.+oo oo.  |
|   . oo=.= . .   |
|    ..==O . .    |
|    ++EO.= o +   |
|   . ++.S o * o  |
|    .  + o . + . |
|        .     o .|
|             . = |
|              *. |
+----[SHA256]-----+

parallels@kali-linux:~/.ssh$ sudo ssh-copy-id -i /home/parallels/.ssh/id_rsa.pub "parallels@10.211.55.5"

/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/parallels/.ssh/id_rsa.pub"
The authenticity of host '10.211.55.5 (10.211.55.5)' can't be established.
ECDSA key fingerprint is SHA256:8Iiv/8aBCprlS3ohWLFH9iiofaIpwXFjxaRKAT6pZvc.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
parallels@10.211.55.5's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'parallels@10.211.55.5'"
and check to make sure that only the key(s) you wanted were added.

parallels@kali-linux:~/.ssh$ ssh parallels@10.211.55.5
Enter passphrase for key '/home/parallels/.ssh/id_rsa':

Welcome to Ubuntu 20.04.2 LTS (GNU/Linux 5.4.0-66-generic aarch64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

 * Super-optimized for small spaces - read how we shrank the memory
   footprint of MicroK8s to make it the smallest full K8s around.

   https://ubuntu.com/blog/microk8s-memory-optimisation

2 updates can be applied immediately.
To see these additional updates run: apt list --upgradable


Last login: Thu Aug 12 17:05:31 2021 from 10.211.55.5

6.
На ВМ с Ubuntu выполняем:
mv 

На ВМ с Kali linux выполняем:

parallels@kali-linux:~/.ssh$ sudo vim /etc/hosts
Добавляем строку
10.211.55.5 ubuntu_20_04

parallels@kali-linux:~/.ssh$ sudo ssh-copy-id -i /home/parallels/.ssh/id_rsa.pub "parallels@ubuntu_20_04"

/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/parallels/.ssh/id_rsa.pub"
The authenticity of host 'ubuntu_20_04 (10.211.55.5)' can't be established.
ECDSA key fingerprint is SHA256:8Iiv/8aBCprlS3ohWLFH9iiofaIpwXFjxaRKAT6pZvc.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
parallels@ubuntu_20_04's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'parallels@ubuntu_20_04'"
and check to make sure that only the key(s) you wanted were added.

parallels@kali-linux:~/.ssh$ ssh parallels@ubuntu_20_04

The authenticity of host 'ubuntu_20_04 (10.211.55.5)' can't be established.
ECDSA key fingerprint is SHA256:8Iiv/8aBCprlS3ohWLFH9iiofaIpwXFjxaRKAT6pZvc.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'ubuntu_20_04' (ECDSA) to the list of known hosts.
Enter passphrase for key '/home/parallels/.ssh/id_rsa': 
Welcome to Ubuntu 20.04.2 LTS (GNU/Linux 5.4.0-66-generic aarch64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

 * Super-optimized for small spaces - read how we shrank the memory
   footprint of MicroK8s to make it the smallest full K8s around.

   https://ubuntu.com/blog/microk8s-memory-optimisation

2 updates can be applied immediately.
To see these additional updates run: apt list --upgradable


Last login: Thu Aug 12 17:06:35 2021 from 10.211.55.5

7.
parallels@ubuntu-linux-20-04-desktop:~/.ssh$ sudo tcpdump -c 100 -w ~/ubuntu2004.pcap

tcpdump: listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
100 packets captured
114 packets received by filter
0 packets dropped by kernel

parallels@ubuntu-linux-20-04-desktop:~$ ll | grep pcap
-rw-r--r--  1 tcpdump   tcpdump   34605 Aug 12 19:07 ubuntu2004.pcap

Скриншот открытия этого файла в wireshark:
http://joxi.ru/8AnYp13UoKdlP2
