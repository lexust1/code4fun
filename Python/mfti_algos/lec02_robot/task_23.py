#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_6_6():
    stp_cnt2 = 0
    while not wall_is_on_the_right():
        move_right()
        if not wall_is_above():
            stp_cnt = 0
            while not wall_is_above():
                move_up()
                fill_cell()
                stp_cnt += 1
            move_down(stp_cnt)
        stp_cnt2 += 1
    if wall_is_on_the_right():
        move_left(stp_cnt2)


if __name__ == '__main__':
    run_tasks()
