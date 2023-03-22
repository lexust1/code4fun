#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    num_cells = 1
    for step2 in range(13):
        move_down()
        for step in range(num_cells):
            move_right()
            fill_cell()
        move_left(num_cells)
        num_cells += 1
    move_down()
    move_right()


if __name__ == '__main__':
    run_tasks()
