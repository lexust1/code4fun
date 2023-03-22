#!/usr/bin/python3

from pyrob.api import *


def draw_cross():
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

def draw_ten_crosses():
    for step in range(10):
        draw_cross()
        if step < 9:
            move_right(4)

@task(delay=0.001)
def task_2_4():
    # Draw 5 lines with 10 crosses.
    for step in range(5):
        draw_ten_crosses()
        move_left(36)
        if step < 4:
            move_down(4)


if __name__ == '__main__':
    run_tasks()
