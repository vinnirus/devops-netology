# devops-netology
devops-10 student

HW-3.4. Операционные системы, лекция 2

п.1
Использовал parallels c ВМ ubuntu 20.04 для arm64
В репозитории не оказалось пакета node_exporter дяя требуемой архитектуры, поэтому:

Установил компилятор golang
sudo snap install go --classic

Далее я клонировал исходники и скомпилировал код в исполняемые файлы
git clone https://github.com/prometheus/node_exporter.git
cd node_exporter/
go build

Определил юнит-файл для будущего сервиса

touch /etc/systemd/system/node_exporter.service
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

Активировал автозагрузку службы
systemctl enable node_exporter.service

И запустил службу
systemctl start node_exporter.service

Для того, чтобы предусмотреть возможность добавления опций к запускаемому процессу, необходимо создать конфигурационный файл
Например, изменим порт по которому будет доступна служба
echo 'ARGS=--web.listen-address=localhost:9991' > /etc/node_exporter.conf

И прописать путь к конфигурационному файлу в описании юнита
vim /etc/systemd/system/node_exporter.service
Добавили строку EnvironmentFile=/etc/node_exporter.conf и изменили значение для параметра ExecStart в раздел [Service]
[Service]
EnvironmentFile=/etc/node_exporter.conf
ExecStart=/opt/node_exporter/node_exporter $ARGS

Затем необходимо перечитать настройки systemctl
systemctl daemon-reload

И перезапустить службу
systemctl restart node_exporter.service

Для проверки выполним
curl localhost:9991/metrics > /home/parallels/mon.metrics
tail /home/parallels/mon.metrics

root@ubuntu-linux-20-04-desktop:/etc/systemd/system# tail /home/parallels/mon.metrics 
promhttp_metric_handler_errors_total{cause="encoding"} 0
promhttp_metric_handler_errors_total{cause="gathering"} 0
# HELP promhttp_metric_handler_requests_in_flight Current number of scrapes being served.
# TYPE promhttp_metric_handler_requests_in_flight gauge
promhttp_metric_handler_requests_in_flight 1
# HELP promhttp_metric_handler_requests_total Total number of scrapes by HTTP status code.
# TYPE promhttp_metric_handler_requests_total counter
promhttp_metric_handler_requests_total{code="200"} 3
promhttp_metric_handler_requests_total{code="500"} 0
promhttp_metric_handler_requests_total{code="503"} 0


Ниже приведен вывод команды systemctl status node_exporter.service после перезапуска ВМ:

root@ubuntu-linux-20-04-desktop:/etc/systemd/system# systemctl status node_exporter.service
● node_exporter.service - Node Exporter
     Loaded: loaded (/etc/systemd/system/node_exporter.service; enabled; vendor preset: enabled)
     Active: active (running) since Thu 2021-07-22 15:40:55 MSK; 8min ago
   Main PID: 20692 (node_exporter)
      Tasks: 6 (limit: 2268)
     Memory: 8.1M
     CGroup: /system.slice/node_exporter.service
             └─20692 /opt/node_exporter/node_exporter --web.listen-address=localhost:9991

Jul 22 15:40:55 ubuntu-linux-20-04-desktop node_exporter[20692]: level=info ts=2021-07-22T12:40:55.898Z caller=node_exporter.go:115 collector>
Jul 22 15:40:55 ubuntu-linux-20-04-desktop node_exporter[20692]: level=info ts=2021-07-22T12:40:55.898Z caller=node_exporter.go:115 collector>
Jul 22 15:40:55 ubuntu-linux-20-04-desktop node_exporter[20692]: level=info ts=2021-07-22T12:40:55.898Z caller=node_exporter.go:115 collector>
Jul 22 15:40:55 ubuntu-linux-20-04-desktop node_exporter[20692]: level=info ts=2021-07-22T12:40:55.898Z caller=node_exporter.go:115 collector>
Jul 22 15:40:55 ubuntu-linux-20-04-desktop node_exporter[20692]: level=info ts=2021-07-22T12:40:55.899Z caller=node_exporter.go:199 msg="List>
Jul 22 15:40:55 ubuntu-linux-20-04-desktop node_exporter[20692]: level=info ts=2021-07-22T12:40:55.899Z caller=tls_config.go:191 msg="TLS is >
Jul 22 15:41:07 ubuntu-linux-20-04-desktop node_exporter[20692]: level=error ts=2021-07-22T12:41:07.788Z caller=collector.go:169 msg="collect>
Jul 22 15:41:21 ubuntu-linux-20-04-desktop node_exporter[20692]: level=error ts=2021-07-22T12:41:21.413Z caller=collector.go:169 msg="collect>
Jul 22 15:46:54 ubuntu-linux-20-04-desktop node_exporter[20692]: level=error ts=2021-07-22T12:46:54.654Z caller=collector.go:169 msg="collect>
Jul 22 15:47:44 ubuntu-linux-20-04-desktop node_exporter[20692]: level=error ts=2021-07-22T12:47:44.343Z caller=collector.go:169 msg="collect>

п.2
На основании имеющихся метрик, для мониторинга состояния сервера я выбрал:
[cpu]
node_cpu_seconds_total,
[disk/io]
node_disk_io_now
node_disk_io_time_seconds_total
node_filesystem_free_bytes
[ram]
node_memory_MemTotal_bytes
node_memory_Cached_bytes
node_memory_MemAvailable_bytes
node_memory_Shmem_bytes
[net]
node_network_receive_bytes_total
node_network_receive_errs_total
node_network_up

п.3
