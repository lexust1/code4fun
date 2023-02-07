#!/usr/bin/python3

from pyrob.api import *


def one_cycle():
    if wall_is_beneath() and wall_is_on_the_right():
        while not wall_is_on_the_left() and wall_is_beneath():
            move_left()
        if not wall_is_on_the_left() and not wall_is_beneath():
            move_down()
            while not wall_is_on_the_right():
                move_right()
    elif not wall_is_beneath() and wall_is_on_the_right():
        while not wall_is_beneath():
            move_down()


@task(delay=0.01)
def task_8_30():
    while wall_is_on_the_right():
        one_cycle()


if __name__ == '__main__':
    run_tasks()
