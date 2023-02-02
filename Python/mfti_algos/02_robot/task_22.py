#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_5_10():
    # 1x1
    if (wall_is_beneath() and wall_is_on_the_left() and wall_is_above() and
            wall_is_on_the_right()):
        fill_cell()
    elif wall_is_on_the_left():
        while wall_is_on_the_left():
            count_steps = 0
            while not wall_is_on_the_right():
                fill_cell()
                move_right()
                count_steps += 1
            fill_cell()
            move_left(count_steps)
            if not wall_is_beneath():
                move_down()
            else:
                break


if __name__ == '__main__':
    run_tasks()
