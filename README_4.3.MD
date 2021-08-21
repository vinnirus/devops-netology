### devops-10 student

### HW-4.3. Языки разметки JSON и YAML
---

1.<br>
Формат *json* предполагает наличие пары *key:value*, причем *key* является строкой, в исходном файле допущена ошибка в последней паре, необходимо закрыть `"` ключ `ip` и указать тип его значения, т.к. при парсинге значение будет преобразовано в число, и произойдет ошибка при чтении точки во втором октете ip-адреса. Также, для удобства чтения правильнее будет расставить символ `:` одинаково во всем документе.<br>
Корректный *json* будет выглядеть следующим образом:

```json
 { "info": "Sample JSON output from our service\t",
   "elements": [
        {"name": "first",
        "type": "server",
        "ip": 7175 
        },
        {"name": "second",
        "type": "proxy",
        "ip": "71.78.22.43"
        }
    ]
}
```

2.


```python
#!/usr/bin/env python3

import os
import sys
import socket
import json
import yaml


path_cfg_file = './app.cfg'
path_prev_check_file = './previous_check'
json_file = './result.json'
yml_file = './result.yml'

check_dict = {}
check_list = []
prev_check_dict = {}
errors_count = 0

with open(path_cfg_file, 'r') as ip_file:
    ip_list = ip_file.readlines()
ip_list = (x.strip() for x in ip_list)

# get ip by name
for dns_name in ip_list:
    current_ip = socket.gethostbyname(dns_name)
    current_check_pair = check_dict.update({dns_name: current_ip})

# compare with results from previous check
if os.path.isfile(path_prev_check_file) and os.path.getsize(path_prev_check_file) > 0:

    with open(path_prev_check_file, 'r+') as prev_file:
        for line in prev_file:
            key, value = line.replace('\n', '').split(':')
            prev_check_dict[key] = value

        for key in check_dict.keys():
            if check_dict.get(key) != prev_check_dict.get(key):
                print(f'[ERROR] {key} IP mismatch: {prev_check_dict.get(key)} {check_dict.get(key)}')
                errors_count = 1

        if errors_count == 0:
            prev_file.truncate(0)
            prev_file.seek(0)
            for key in check_dict.keys():
                prev_file.write(f'{key}:{check_dict.get(key)}\n')
                print(f'{key}:{check_dict.get(key)}\n')

else:
    with open(path_prev_check_file, 'w') as prev_file:
        for dns_name in check_dict:
            prev_file.write(f'{dns_name}:{check_dict.get(dns_name)}\n')

with open(json_file, 'w') as f_json:
    f_json.write(json.dumps(check_dict))

with open(yml_file, 'w') as f_yml:
    f_yml.write(yaml.dump(check_dict))
```
