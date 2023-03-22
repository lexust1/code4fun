#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    # The upper left corner.
    if wall_is_on_the_left() and wall_is_above():
        while not wall_is_on_the_right():
            move_right()
        while not wall_is_beneath():
            move_down()
    # The upper right corner.
    elif wall_is_on_the_right() and wall_is_above():
        while not wall_is_beneath():
            move_down()
        while not wall_is_on_the_left():
            move_left()
    # The lower right corner.
    elif wall_is_on_the_right() and wall_is_beneath():
        while not wall_is_on_the_left():
            move_left()
        while not wall_is_above():
            move_up()
    # The lower left corner.
    elif wall_is_on_the_left() and wall_is_beneath():
        while not wall_is_above():
            move_up()
        while not wall_is_on_the_right():
            move_right()


if __name__ == '__main__':
    run_tasks()
