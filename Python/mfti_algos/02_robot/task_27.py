#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_7_5():
    move_right()
    fill_cell()
    # The actual position counter.
    cell_cnt = 2
    # The last gap between the filled cells.
    next_gap = 1
    # The last filled cell.
    last_filled_cell = 2
    while not wall_is_on_the_right():
        move_right()
        cell_cnt += 1
        # (last_filled_cell + next_gap) helps to find the next cell that
        # we have to fill.
        if (cell_cnt == last_filled_cell + next_gap and not
            wall_is_on_the_right()):
            fill_cell()
            last_filled_cell = cell_cnt
            next_gap += 1


if __name__ == '__main__':
    run_tasks()
