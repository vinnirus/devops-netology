# devops-netology
devops-10 student

HW-3.4. Операционные системы, лекция 2

п.1
Использовал parallels c ВМ ubuntu 20.04 для arm64
В репозитории не оказалось пакета node_exporter дяя требуемой архитектуры, поэтому:

Установил компилятор golang
sudo snap install go --classic

Далее я клонировал исходники
git clone https://github.com/prometheus/node_exporter.git
cd node_exporter/
go build

cd /etc/systemd/system/
touch node_exporter.service
vim node_exporter.service
##############################
[Unit]
Description=Node Exporter
 
[Service]
ExecStart=/opt/node_exporter/node_exporter
 
[Install]
WantedBy=default.target
##############################

Затем перечитал настройки для systemctl
systemctl daemon-reload

Активировал службу
systemctl enable node_exporter.service

И запустил службу
systemctl start node_exporter.service

Ниже приведен вывод команды systemctl status node_exporter.service после перезапуска ВМ:

parallels@ubuntu-linux-20-04-desktop:/etc/systemd/system$ systemctl status node_exporter.service 
● node_exporter.service - Node Exporter
     Loaded: loaded (/etc/systemd/system/node_exporter.service; enabled; vendor preset: enabled)
     Active: active (running) since Wed 2021-07-21 23:17:06 MSK; 30min ago
   Main PID: 553 (node_exporter)
      Tasks: 5 (limit: 2268)
     Memory: 17.1M
     CGroup: /system.slice/node_exporter.service
             └─553 /opt/node_exporter/node_exporter

Jul 21 23:17:06 ubuntu-linux-20-04-desktop node_exporter[553]: level=info ts=2021-07-21T20:17:06.180Z caller=node_exporter.go:115 collector=time
Jul 21 23:17:06 ubuntu-linux-20-04-desktop node_exporter[553]: level=info ts=2021-07-21T20:17:06.180Z caller=node_exporter.go:115 collector=timex
Jul 21 23:17:06 ubuntu-linux-20-04-desktop node_exporter[553]: level=info ts=2021-07-21T20:17:06.180Z caller=node_exporter.go:115 collector=udp_queues
Jul 21 23:17:06 ubuntu-linux-20-04-desktop node_exporter[553]: level=info ts=2021-07-21T20:17:06.180Z caller=node_exporter.go:115 collector=uname
Jul 21 23:17:06 ubuntu-linux-20-04-desktop node_exporter[553]: level=info ts=2021-07-21T20:17:06.180Z caller=node_exporter.go:115 collector=vmstat
Jul 21 23:17:06 ubuntu-linux-20-04-desktop node_exporter[553]: level=info ts=2021-07-21T20:17:06.180Z caller=node_exporter.go:115 collector=xfs
Jul 21 23:17:06 ubuntu-linux-20-04-desktop node_exporter[553]: level=info ts=2021-07-21T20:17:06.180Z caller=node_exporter.go:115 collector=zfs
Jul 21 23:17:06 ubuntu-linux-20-04-desktop node_exporter[553]: level=info ts=2021-07-21T20:17:06.184Z caller=node_exporter.go:199 msg="Listening on" address=:9100
Jul 21 23:17:06 ubuntu-linux-20-04-desktop node_exporter[553]: level=info ts=2021-07-21T20:17:06.186Z caller=tls_config.go:191 msg="TLS is disabled." http2=false
Jul 21 23:18:14 ubuntu-linux-20-04-desktop node_exporter[553]: level=error ts=2021-07-21T20:18:14.031Z caller=collector.go:169 msg="collector failed" name=nvme duration_seconds=1.>
lines 1-19/19 (END)

