#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    while not wall_is_on_the_right():
        if wall_is_beneath() and wall_is_above():
            move_right()
        elif wall_is_beneath() and not wall_is_above():
            fill_cell()
            move_right()
    if wall_is_on_the_right() and not wall_is_above():
        fill_cell()


if __name__ == '__main__':
    run_tasks()
