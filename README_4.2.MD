### devops-10 student

### HW-4.2. Использование Python для решения типовых DevOps задач

---

1.
При попытке присвоить переменной `c` результат сложения переменных `a` и `b` мы получим ошибку о неподдерживаемых типах операндов для операции сложения `(+)`. В итоге скрипт завершится с ошибкой.

Для того, чтобы в результате сложения переменная `c` получила числовые значения, равные `12` и `3`, необходимо использовать встроенные функции преобразования типов `int()` и `str()`:

```
#!/usr/bin/env python3

a = 1
b = '2'
c = int(str(a) + b)
```
и, соответственно,
`c = a + int(b)`.

2.

```python
#!/usr/bin/env python3

import os
path_to_git = '/Users/nikitavinogradov/Documents/education/netology/devops-netology'
bash_command = ["cd " + path_to_git, "git status"]
git_statuses = ['modified', 'new file', 'deleted']
result_os = os.popen(' && '.join(bash_command)).read()
result_changing_files = []
is_change = 0
for result in result_os.split('\n'):
    for status in git_statuses:
        if result.find(status) != -1:
            prepare_result = result.replace('\t' + status + ':   ', '')
            result_changing_files.append(prepare_result)
            is_change += 1
print(f'Current git directory is {path_to_git}')
for each in result_changing_files:
    print(each)
```

3.

```python
#!/usr/bin/env python3

import os
import sys


def run_bash_commands(command_list):
    return os.popen(' && '.join(command_list)).read()


def is_git_repo(git_path):
    bash_commands = ["cd " + git_path, "git status"]
    result_os = run_bash_commands(bash_commands)
    for result in result_os:
        if result.find('fatal: not a git repository') != -1:
            print('it is not a git repo')
            return False
        else:
            print('it is a git repo')
            return True


def list_changing_files(path_to_git):
    result_changing_files = []
    if is_git_repo(path_to_git):
        git_statuses = ['modified', 'new file', 'deleted']
        bash_command = ["cd " + path_to_git, "git status"]
        result_os = run_bash_commands(bash_command)

        for result in result_os.split('\n'):
            for status in git_statuses:
                if result.find(status) != -1:
                    prepare_result: str = result.replace('\t' + status + ':   ', '')
                    result_changing_files.append(prepare_result)

    for each in result_changing_files:
        print(each)
    return result_changing_files


if __name__ == "__main__":
    if len(sys.argv) == 1:
        list_changing_files(sys.argv[1])
    else:
        print('invalid input parameter')
```

4.

```python
#!/usr/bin/env python3

import os
import sys
import socket

path_cfg_file = './app.cfg'
path_prev_check_file = './previous_check'
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
```
