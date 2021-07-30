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

в этом случае коды ответов и времена будут соответствовать изображению https://ibb.co/YXCpzQ7.

Если же в адресной строке указать http://stackoverflow:80, то поведение будет идентично п.1 с кодом 301 и редиректом на https://stackoverflow.com
в этом случае коды ответов и времена будут соответствовать изображению https://ibb.co/19DnYtt.

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

п.6

п.7
  
п.8
