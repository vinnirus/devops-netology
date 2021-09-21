### devops-10 student

### HW-5.4. Практические навыки работы с Docker

---

1.<br>
Dockerfile:

```
FROM archlinux:latest

RUN pacman -Syu --noconfirm

RUN pacman -S ponysay --noconfirm

ENTRYPOINT ["/usr/bin/ponysay"]

CMD ["Hey, netology”]

```

Build logs

```
vinni@vinni-VM:~/netology/hw5.4/1$ docker build -t vinnirus/my_arch:0.1 -f Dockerfile ./
Sending build context to Docker daemon  2.048kB
Step 1/5 : FROM archlinux:latest
 ---> 1d6f90387c13
Step 2/5 : RUN pacman -Syu --noconfirm
 ---> Using cache
 ---> 4d19fcef40b8
Step 3/5 : RUN pacman -S ponysay --noconfirm
 ---> Running in d3bb3827d5f5
resolving dependencies...
looking for conflicting packages...

Packages (4) gdbm-1.21-1  libnsl-2.0.0-1  python-3.9.7-1  ponysay-3.0.3-4

Total Download Size:   12.52 MiB
Total Installed Size:  64.07 MiB

:: Proceed with installation? [Y/n] 
:: Retrieving packages...
 python-3.9.7-1-x86_64 downloading...
 ponysay-3.0.3-4-any downloading...
 gdbm-1.21-1-x86_64 downloading...
 libnsl-2.0.0-1-x86_64 downloading...
checking keyring...
checking package integrity...
loading package files...
checking for file conflicts...
:: Processing package changes...
installing gdbm...
installing libnsl...
installing python...
Optional dependencies for python
    python-setuptools
    python-pip
    sqlite [installed]
    mpdecimal: for decimal
    xz: for lzma [installed]
    tk: for tkinter
installing ponysay...
:: Running post-transaction hooks...
(1/1) Arming ConditionNeedsUpdate...
Removing intermediate container d3bb3827d5f5
 ---> 1f46b3f634a0
Step 4/5 : ENTRYPOINT ["/usr/bin/ponysay"]
 ---> Running in 7217f887f209
Removing intermediate container 7217f887f209
 ---> 136ec7e40a01
Step 5/5 : CMD ["Hey, netology”]
 ---> Running in ac4dd4855123
Removing intermediate container ac4dd4855123
 ---> 117fe3b576f3
Successfully built 117fe3b576f3
Successfully tagged vinnirus/my_arch:0.1
```

[Reference to vinnirus/my_arch](https://hub.docker.com/repository/docker/vinnirus/my_arch) <br>

2. In progress <br>
3. In progress <br>
