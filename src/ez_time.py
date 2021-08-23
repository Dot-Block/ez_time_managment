# Author: Dot-Block
# Creation Date: 21/08/2021
# Title: ez_time_management.py
# Last Change: 21/08/2021

import time
import datetime

def error(error_string):
    print(error_string)

def get_int(input_string):
    try:
        int_input = abs(int(input(input_string)))
    except:
        error("Invalid input")
        return -1
    return int_input

def get_time():
    time = datetime.datetime.now()
    return time

def get_tasks():
    task_num = get_int("How many tasks you got pal?: ")
    task_names = []
    task_time = []
    print("Oh ho? Name em!")
    for i in range(task_num):
        task_names.append(input("Task {0} Name: ".format(i)))
        task_time.append(60 * get_int("Task {0} Duration (per interval) (mins): ".format(i)))
    return task_names, task_time

if __name__ == "__main__":
    get_time()
    task_names, task_times = get_tasks()
    while True:
        for index, task_name in enumerate(task_names):
            current_time = get_time()
            future_time = (current_time + datetime.timedelta(seconds=task_times[index]))
            print("You are currently doing task: {0}".format(task_name))
            print("The current time is {0} and you should be done at {1}".format(current_time.strftime("%H:%M:%S"),
                                                                                 future_time.strftime("%H:%M:%S")))
            time.sleep(int(task_times[index]))

