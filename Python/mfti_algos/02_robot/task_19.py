#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    while wall_is_beneath() and not wall_is_on_the_left():
        move_left()
    # Exit on the left.
    if not wall_is_beneath():
        while not wall_is_on_the_left():
            move_left()
        while not wall_is_above():
            move_up()
    # No exit on the left.
    elif wall_is_on_the_left():
        while wall_is_beneath() and not wall_is_on_the_right():
            move_right()
        # Exit on the right.
        if not wall_is_beneath():
            while not wall_is_above():
                move_up()
            while not wall_is_on_the_left():
                move_left()
        # No exit on the right.
        elif wall_is_on_the_right():
            print("No exit at all.")
        else:
            print("Something strange 1.")
    else:
        print("Something strange 2.")


if __name__ == '__main__':
    run_tasks()
