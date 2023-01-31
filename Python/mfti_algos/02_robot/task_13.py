#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
    while not wall_is_on_the_right():
        if not wall_is_beneath() and not wall_is_above():
            move_down()
            fill_cell()
            move_up(2)
            fill_cell()
            move_down()
            move_right()
        elif not wall_is_beneath() and wall_is_above():
            move_down()
            fill_cell()
            move_up()
            move_right()
        elif wall_is_beneath() and not wall_is_above():
            move_up()
            fill_cell()
            move_down()
            move_right()
        elif wall_is_beneath() and wall_is_above():
            move_right()
        else:
            print("Something strange.")
    if wall_is_on_the_right():
        if not wall_is_beneath() and not wall_is_above():
            move_down()
            fill_cell()
            move_up(2)
            fill_cell()
            move_down()
        elif not wall_is_beneath() and wall_is_above():
            move_down()
            fill_cell()
            move_up()
        elif wall_is_beneath() and not wall_is_above():
            move_up()
            fill_cell()
            move_down()
        else:
            print("No actions")


if __name__ == '__main__':
    run_tasks()
