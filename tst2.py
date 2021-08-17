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
print(os.getcwd())
for each in result_changing_files:
    print(each)
