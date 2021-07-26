# devops-netology
devops-10 student

HW-3.5. Файловые системы

**************
Использовал виртуализацию vbox c ВМ ubuntu 20.04 для x86_64
**************

п.1
Разреженным называется файл, в котором последовательности нулевых байтов заменены на информацию об этих последовательностях (список дыр).

п.2
Жесткая ссылка и файл, для которого она создавалась имеют одинаковые inode. Поэтому жесткая ссылка имеет те же права доступа, владельца и время последней модификации, что и целевой файл. Различаются только имена файлов. Фактически жесткая ссылка это еще одно имя для файла.
Жесткие ссылки появились раньше, чем символические, но сейчас уже устаревают. В повседневной работе жесткие ссылки используются редко.
 
п.3
Вывод команды lsblk после создания VagrantFile и запуска ВМ:

vagrant@vagrant:~$ lsblk
NAME                 MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda                    8:0    0   64G  0 disk
├─sda1                 8:1    0  512M  0 part /boot/efi
├─sda2                 8:2    0    1K  0 part
└─sda5                 8:5    0 63.5G  0 part
  ├─vgvagrant-root   253:0    0 62.6G  0 lvm  /
  └─vgvagrant-swap_1 253:1    0  980M  0 lvm  [SWAP]
sdb                    8:16   0  2.5G  0 disk
sdc                    8:32   0  2.5G  0 disk

п.4
Результат работы fdisk по созднанию разделов:

vagrant@vagrant:/$ lsblk
NAME                 MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda                    8:0    0   64G  0 disk
├─sda1                 8:1    0  512M  0 part /boot/efi
├─sda2                 8:2    0    1K  0 part
└─sda5                 8:5    0 63.5G  0 part
  ├─vgvagrant-root   253:0    0 62.6G  0 lvm  /
  └─vgvagrant-swap_1 253:1    0  980M  0 lvm  [SWAP]
sdb                    8:16   0  2.5G  0 disk
├─sdb1                 8:17   0  1.9G  0 part
└─sdb2                 8:18   0  652M  0 part
sdc                    8:32   0  2.5G  0 disk

п.5
vagrant@vagrant:~$ sudo sfdisk -d /dev/sdb > partitions.sdb
vagrant@vagrant:~$ sudo sfdisk /dev/sdc < partitions.sdb
Checking that no-one is using this disk right now ... OK

Disk /dev/sdc: 2.51 GiB, 2684354560 bytes, 5242880 sectors
Disk model: VBOX HARDDISK
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes

>>> Script header accepted.
>>> Script header accepted.
>>> Script header accepted.
>>> Script header accepted.
>>> Created a new DOS disklabel with disk identifier 0xee43352c.
/dev/sdc1: Created a new partition 1 of type 'Linux' and of size 1.9GiB.
/dev/sdc2: Created a new partition 2 of type 'Linux' and of size 652 MiB.
/dev/sdc3: Done.

New situation:
Disklabel type: dos
Disk identifier: 0xee43352c

Device     Boot   Start     End Sectors  Size Id Type
/dev/sdc1          2048 3907583 3905536  1.9G 83 Linux
/dev/sdc2       3907584 5242879 1335296  652M 83 Linux

The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.

Вывод команды lsblk:
vagrant@vagrant:~$ lsblk
NAME                 MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda                    8:0    0   64G  0 disk
├─sda1                 8:1    0  512M  0 part /boot/efi
├─sda2                 8:2    0    1K  0 part
└─sda5                 8:5    0 63.5G  0 part
  ├─vgvagrant-root   253:0    0 62.6G  0 lvm  /
  └─vgvagrant-swap_1 253:1    0  980M  0 lvm  [SWAP]
sdb                    8:16   0  2.5G  0 disk
├─sdb1                 8:17   0  1.9G  0 part
└─sdb2                 8:18   0  652M  0 part
sdc                    8:32   0  2.5G  0 disk
├─sdc1                 8:33   0  1.9G  0 part
└─sdc2                 8:34   0  652M  0 part

п.6
vagrant@vagrant:~$ sudo mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdb1 /dev/sdc1
mdadm: Note: this array has metadata at the start and
    may not be suitable as a boot device.  If you plan to
    store '/boot' on this device please ensure that
    your boot-loader understands md/v1.x metadata, or use
    --metadata=0.90
Continue creating array? y
mdadm: Defaulting to version 1.2 metadata
mdadm: array /dev/md0 started.

Вывод команды lsblk:
vagrant@vagrant:~$ lsblk
NAME                 MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
sda                    8:0    0   64G  0 disk
├─sda1                 8:1    0  512M  0 part  /boot/efi
├─sda2                 8:2    0    1K  0 part
└─sda5                 8:5    0 63.5G  0 part
  ├─vgvagrant-root   253:0    0 62.6G  0 lvm   /
  └─vgvagrant-swap_1 253:1    0  980M  0 lvm   [SWAP]
sdb                    8:16   0  2.5G  0 disk
├─sdb1                 8:17   0  1.9G  0 part
│ └─md0                9:0    0  1.9G  0 raid1
└─sdb2                 8:18   0  652M  0 part
sdc                    8:32   0  2.5G  0 disk
├─sdc1                 8:33   0  1.9G  0 part
│ └─md0                9:0    0  1.9G  0 raid1
└─sdc2                 8:34   0  652M  0 part

п.7
vagrant@vagrant:~$ sudo mdadm --create /dev/md1 --level=0 --raid-devices=2 /dev/sdb2 /dev/sdc2
mdadm: Defaulting to version 1.2 metadata
mdadm: array /dev/md1 started.

Вывод команды lsblk:
vagrant@vagrant:~$ lsblk
NAME                 MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
sda                    8:0    0   64G  0 disk
├─sda1                 8:1    0  512M  0 part  /boot/efi
├─sda2                 8:2    0    1K  0 part
└─sda5                 8:5    0 63.5G  0 part
  ├─vgvagrant-root   253:0    0 62.6G  0 lvm   /
  └─vgvagrant-swap_1 253:1    0  980M  0 lvm   [SWAP]
sdb                    8:16   0  2.5G  0 disk
├─sdb1                 8:17   0  1.9G  0 part
│ └─md0                9:0    0  1.9G  0 raid1
└─sdb2                 8:18   0  652M  0 part
  └─md1                9:1    0  1.3G  0 raid0
sdc                    8:32   0  2.5G  0 disk
├─sdc1                 8:33   0  1.9G  0 part
│ └─md0                9:0    0  1.9G  0 raid1
└─sdc2                 8:34   0  652M  0 part
  └─md1                9:1    0  1.3G  0 raid0
  
п.8
vagrant@vagrant:~$ sudo pvcreate /dev/md0
  Physical volume "/dev/md0" successfully created.
vagrant@vagrant:~$ sudo pvcreate /dev/md1
  Physical volume "/dev/md1" successfully created.
  
п.9
vagrant@vagrant:~$ sudo vgcreate vg_raid /dev/md0 /dev/md1
  Volume group "vg_raid" successfully created
  
п.10
vagrant@vagrant:~$ sudo lvcreate -n lv_01 -L 100M /dev/vg_raid /dev/md1
  Logical volume "lv_01" created.
  
п.11
vagrant@vagrant:~$ sudo mkfs.ext4 /dev/vg_raid/lv_01
mke2fs 1.45.5 (07-Jan-2020)
Creating filesystem with 25600 4k blocks and 25600 inodes

Allocating group tables: done
Writing inode tables: done
Creating journal (1024 blocks): done
Writing superblocks and filesystem accounting information: done

п.12
vagrant@vagrant:~$ mkdir /tmp/new
vagrant@vagrant:~$ sudo mount /dev/vg_raid/lv_01 /tmp/new

vagrant@vagrant:~$ ls -la /tmp/new
total 24
drwxr-xr-x  3 root root  4096 Jul 26 14:39 .
drwxrwxrwt 11 root root  4096 Jul 26 14:42 ..
drwx------  2 root root 16384 Jul 26 14:39 lost+found

п.13
vagrant@vagrant:/tmp/new$ sudo wget --quiet https://mirror.yandex.ru/ubuntu/ls-lR.gz -O /tmp/new/test.gz

Просмотрим содержимое каталога /tmp/new:
vagrant@vagrant:/tmp/new$ ls -la ./
total 24
drwxr-xr-x  3 root root  4096 Jul 26 14:43 .
drwxrwxrwt 11 root root  4096 Jul 26 15:56 ..
drwx------  2 root root 16384 Jul 26 14:39 lost+found
-rw-r--r--  1 root root     0 Jul 26 17:07 test.gz

п.14
NAME                 MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
sda                    8:0    0   64G  0 disk
├─sda1                 8:1    0  512M  0 part  /boot/efi
├─sda2                 8:2    0    1K  0 part
└─sda5                 8:5    0 63.5G  0 part
  ├─vgvagrant-root   253:0    0 62.6G  0 lvm   /
  └─vgvagrant-swap_1 253:1    0  980M  0 lvm   [SWAP]
sdb                    8:16   0  2.5G  0 disk
├─sdb1                 8:17   0  1.9G  0 part
│ └─md0                9:127  0  1.9G  0 raid1
└─sdb2                 8:18   0  652M  0 part
  └─md1                9:126  0  1.3G  0 raid0
    └─vg_raid-lv_01  253:2    0  100M  0 lvm   /tmp/new
sdc                    8:32   0  2.5G  0 disk
├─sdc1                 8:33   0  1.9G  0 part
│ └─md0                9:127  0  1.9G  0 raid1
└─sdc2                 8:34   0  652M  0 part
  └─md1                9:126  0  1.3G  0 raid0
    └─vg_raid-lv_01  253:2    0  100M  0 lvm   /tmp/new

п.15
root@vagrant:/tmp/new# ls
lost+found  test.gz
root@vagrant:/tmp/new# gzip -t /tmp/new/test.gz
root@vagrant:/tmp/new# echo $?
0

п.16
vagrant@vagrant:/tmp/$ sudo pvmove -n lv_01 /dev/md1 /dev/md0
  /dev/md1: Moved: 16% 
  /dev/md1: Moved: 100%

Вывод команды lsblk:
vagrant@vagrant:/$ lsblk
NAME                 MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
sda                    8:0    0   64G  0 disk
├─sda1                 8:1    0  512M  0 part  /boot/efi
├─sda2                 8:2    0    1K  0 part
└─sda5                 8:5    0 63.5G  0 part
  ├─vgvagrant-root   253:0    0 62.6G  0 lvm   /
  └─vgvagrant-swap_1 253:1    0  980M  0 lvm   [SWAP]
sdb                    8:16   0  2.5G  0 disk
├─sdb1                 8:17   0  1.9G  0 part
│ └─md0                9:127  0  1.9G  0 raid1
│   └─vg_raid-lv_01  253:2    0  100M  0 lvm   /tmp/new
└─sdb2                 8:18   0  652M  0 part
  └─md1                9:126  0  1.3G  0 raid0
sdc                    8:32   0  2.5G  0 disk
├─sdc1                 8:33   0  1.9G  0 part
│ └─md0              9:127  0  1.9G  0 raid1
│   └─vg_raid-lv_01  253:2    0  100M  0 lvm   /tmp/new
└─sdc2                 8:34   0  652M  0 part
  └─md1                9:126  0  1.3G  0 raid0
  
п.17
vagrant@vagrant:/$ sudo mdadm /dev/md0 --fail /dev/sdc1
mdadm: set /dev/sdc1 faulty in /dev/md0

п.18
vagrant@vagrant:/$ dmesg
[ 1380.824801] md/raid1:md0: Disk failure on sdc1, disabling device.
               md/raid1:md0: Operation continuing on 1 devices.
			   
п.19
root@vagrant:/tmp/new# ls
lost+found  test.gz
root@vagrant:/tmp/new# gzip -t /tmp/new/test.gz
root@vagrant:/tmp/new# echo $?
0
