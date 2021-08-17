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
            return False
        else:
            return True


def list_changing_files(path_to_git):
    if is_git_repo(path_to_git):
        git_statuses = ['modified', 'new file', 'deleted']
        bash_command = ["cd " + path_to_git, "git status"]
        result_os = run_bash_commands(bash_command)
        result_changing_files = []
        for result in result_os.split('\n'):
            for status in git_statuses:
                if result.find(status) != -1:
                prepare_result = result.replace('\t' + status + ':   ', '')
                result_changing_files.append(prepare_result)
    for each in result_changing_files:
        print(each)
    return result_changing_files


if __name__ == "__main__":
    if len (sys.argv) == 1:
        list_changing_files(sys.argv[1])
    else:
        print ("Enter correct path to git directory")