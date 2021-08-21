# Author: Dot-Block
# Creation Date: 21/08/2021
# Title: ez_time_management.py
# Last Change: 21/08/2021

import time

def error(error_string):
    print(error_string)

def get_int(input_string):
    try:
        int_input = abs(int(input(input_string)))
    except:
        error("Invalid input")
        return -1
    return int_input


def get_tasks():
    task_num = get_int("How many tasks you got pal?: ")
    task_names = []
    task_time = []
    print("Oh ho? Name em!")
    for i in range(task_num):
        task_names.append(input("Task {0} Name: ".format(i)))
        task_time.append(get_int("Task {0} Duration (per interval): ".format(i)))
    return task_names, task_time

if __name__ == "__main__":

    task_names, task_times = get_tasks()
    while True:
        for index, task_name in enumerate(task_names):
            print("You are currently doing task: {0}".format(task_name))
            time.sleep(int(task_times[index]))

