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
