#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    # Count the number of cells in one side.
    cnt_length = 0
    while not wall_is_on_the_right():
        move_right()
        cnt_length += 1
    move_left(cnt_length)
    # Fill lines.
    row_cnt = 0
    for row_num in range(cnt_length + 1):
        for col_num in range(cnt_length):
            if col_num != row_num and col_num != cnt_length - row_num:
                fill_cell()
            move_right()
            # Special conditions for the right cells.
            if wall_is_on_the_right() and not (wall_is_above() or wall_is_beneath()):
                fill_cell()
        move_left(cnt_length)
        if row_num < cnt_length:
            move_down()


if __name__ == '__main__':
    run_tasks()
