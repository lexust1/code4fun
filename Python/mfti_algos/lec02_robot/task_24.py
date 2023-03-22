#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    # Go to the start point.
    move_down()
    move_right()
    # Go to the cross center.
    move_down()
    move_right()
    # Create the cross.
    fill_cell()
    move_up()
    fill_cell()
    move_down(2)
    fill_cell()
    move_up()
    move_right()
    fill_cell()
    move_left(2)
    fill_cell()
    #Go the final point.
    move_up()


if __name__ == '__main__':
    run_tasks()
