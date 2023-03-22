#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    for step1 in range(12):
        for step2 in range(27):
            move_right()
            fill_cell()
        move_left(27)
        move_down()
    move_right()


if __name__ == '__main__':
    run_tasks()
