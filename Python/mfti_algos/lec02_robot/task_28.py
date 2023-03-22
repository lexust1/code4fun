#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    cnt = 0
    while not wall_is_on_the_right() and cnt < 5:
        if cell_is_filled():
            cnt += 1
        if cnt < 5:
            move_right()


if __name__ == '__main__':
    run_tasks()
