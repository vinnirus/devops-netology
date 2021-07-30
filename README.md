# devops-netology
devops-10 student

HW-3.6. Компьютерные сети, лекция 1

**************
Использовал виртуализацию parallels c ВМ ubuntu 20.04 для arm64
**************

п.1
parallels@ubuntu-linux-20-04-desktop:~$ telnet stackoverflow.com 80
Trying 151.101.129.69...
Connected to stackoverflow.com.
Escape character is '^]'.
GET /questions HTTP/1.0
HOST: stackoverflow.com

HTTP/1.1 301 Moved Permanently
cache-control: no-cache, no-store, must-revalidate
location: https://stackoverflow.com/questions
x-request-guid: bca82a93-62da-4e5e-9535-e7f60d900341
feature-policy: microphone 'none'; speaker 'none'
content-security-policy: upgrade-insecure-requests; frame-ancestors 'self' https://stackexchange.com
Accept-Ranges: bytes
Date: Tue, 27 Jul 2021 12:14:17 GMT
Via: 1.1 varnish
Connection: close
X-Served-By: cache-hhn4025-HHN
X-Cache: MISS
X-Cache-Hits: 0
X-Timer: S1627388058.893455,VS0,VE86
Vary: Fastly-SSL
X-DNS-Prefetch-Control: off
Set-Cookie: prov=864fdb6f-27dd-a07c-8b0c-9f4700956fad; domain=.stackoverflow.com; expires=Fri, 01-Jan-2055 00:00:00 GMT; path=/; HttpOnly

Connection closed by foreign host.

Сервер вернул код 301, это означает, что запрошенному ресурсу был назначен новый постоянный URI https://stackoverflow.com/questions и любые будущие ссылки на этот ресурс ДОЛЖНЫ использовать этот URI.

п.2
Если указать в адресной строке http://stackoverflow.com, то сразу происходит редирект на https://stackoverflow.com, 

GET	
scheme		https
host		stackoverflow.com
filename	/
Address		151.101.65.69:443
Status		200
		OK
Version		HTTP/2
Transferred	57.16 KB (202.07 KB size)

в этом случае коды ответов и времена будут соответствовать изображению http://joxi.ru/DrlDbxEcGG6vqr.

Если же в адресной строке указать http://stackoverflow:80, то поведение будет идентично п.1 с кодом 301 и редиректом на https://stackoverflow.com
в этом случае коды ответов и времена будут соответствовать изображению http://joxi.ru/Y2LOK18fMMY9jm.

п.3
parallels@ubuntu-linux-20-04-desktop:~$ wget -qO - eth0.me
178.176.78.186

п.4
parallels@ubuntu-linux-20-04-desktop:~$ whois 178.176.78.186

organisation:   ORG-OM1-RIPE
org-name:       PJSC MegaFon
country:        RU
org-type:       LIR
address:        41, Oruzheyniy lane
address:        127006
address:        Moscow
address:        RUSSIAN FEDERATION
phone:          +74955077777

% Information related to '178.176.64.0/19AS25159'

route:          178.176.64.0/19
descr:          MF-MOSCOW-NAT-POOL-178-176-64-0
origin:         AS25159

п.5
parallels@ubuntu-linux-20-04-desktop:~$ traceroute 8.8.8.8
traceroute to 8.8.8.8 (8.8.8.8), 64 hops max
  1   8.8.8.8  17.045ms  16.275ms  15.981ms 

parallels@ubuntu-linux-20-04-desktop:~$ ping -i 1 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=128 time=17.6 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=128 time=17.7 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=128 time=17.6 ms

parallels@ubuntu-linux-20-04-desktop:~$ whois -I 8.8.8.8

NetRange:       8.8.8.0 - 8.8.8.255
CIDR:           8.8.8.0/24
NetName:        LVLT-GOGL-8-8-8
NetHandle:      NET-8-8-8-0-1
Parent:         LVLT-ORG-8-8 (NET-8-0-0-0-1)
NetType:        Reallocated
OriginAS:       
Organization:   Google LLC (GOGL)
RegDate:        2014-03-14
Updated:        2014-03-14
Ref:            https://rdap.arin.net/registry/ip/8.8.8.0


OrgName:        Google LLC
OrgId:          GOGL
Address:        1600 Amphitheatre Parkway
City:           Mountain View
StateProv:      CA

п.6
parallels@ubuntu-linux-20-04-desktop:~$ mtr -r -w -z -j -c 10 8.8.8.8 > ./mtr.out.json
parallels@ubuntu-linux-20-04-desktop:~$ less mtr.out.json

{
  "report": {
    "mtr": {
      "src": "ubuntu-linux-20-04-desktop",
      "dst": "8.8.8.8",
      "tos": "0x0",
      "psize": "64",
      "bitpattern": "0x00",
      "tests": "10"
    },
    "hubs": [{
      "count": "1",
      "host": "dns.google",
      "ASN": "AS15169",
      "Loss%": 0.00,
      "Snt": 10,
      "Last": 16.87,
      "Avg": 34.93,
      "Best": 16.87,
      "Wrst": 134.47,
      "StDev": 35.58
    }]
  }

п.7
parallels@ubuntu-linux-20-04-desktop:~$ dig -t ANY dns.google +noall +answer

dns.google.		3568	IN	A	8.8.4.4
dns.google.		3568	IN	A	8.8.8.8
dns.google.		3568	IN	RRSIG	A 8 2 900 20210829161016 20210730161016 1773 dns.google. JYSlVxqwA9LHOlOp8Vxohsa5zv9wO34/BDf9miZcAvMnlSlRwse5sbje nNXLp/DKQ5h3ab6WbdHEkPvkRFjUr/DwXF09kCv+R92q2fgKu9jvF0aA LbG+I255DhRwbQGVN0xSyT6i4QOfdGIU/NeuUmFQ3iY7PZySnvR+KDo+ snY=
dns.google.		524	IN	RRSIG	AAAA 8 2 900 20210829161016 20210730161016 1773 dns.google. DRkYro14B7TId3qPFfG3/PCsQnlAEnmxfatUP5YnuOvIih2f7a9FUo1D OiWv/pfi3RYdxWmfBbYBkJJFRq80WZ6e5bfVciZYD4Zt8aumcFTdhuSU hNS90BokooqJJY9iNg70vQBmXBNBuEhelemnTchi7VeD7Z+X0NXtFrrC aXs=

A-записи:
dns.google.		3568	IN	A	8.8.4.4
dns.google.		3568	IN	A	8.8.8.8

п.8
parallels@ubuntu-linux-20-04-desktop:~$ dig -x 8.8.4.4 +noall +answer
4.4.8.8.in-addr.arpa.	5533	IN	PTR	dns.google.

parallels@ubuntu-linux-20-04-desktop:~$ dig -x 8.8.8.8 +noall +answer
8.8.8.8.in-addr.arpa.	5565	IN	PTR	dns.google.

PTR-запись: dns.google.
