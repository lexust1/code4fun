#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    cnt_of_filled_cells = 0
    while not wall_is_on_the_right() and cnt_of_filled_cells < 3:
        if cell_is_filled():
            cnt_of_filled_cells += 1
        else:
            cnt_of_filled_cells = 0
        if cnt_of_filled_cells < 3:
            move_right()


if __name__ == '__main__':
    run_tasks()
