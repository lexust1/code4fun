# Опираясь на примеры и используя новые инструменты,
# реализуйте модель математического маятника.
import graphics as gr
from math import pi, sin, cos


# Constants
G = 9.8
LENGTH = 200
RADIUS = 20
TIME_STEP = 1
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400 + 2 * RADIUS
WINDOW_CENTER = gr.Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)


# Create window and draw initial pendulum
window = gr.GraphWin("Pendulum", WINDOW_WIDTH, WINDOW_HEIGHT)
line = gr.Line(
    WINDOW_CENTER,
    gr.Point(WINDOW_CENTER.x, WINDOW_CENTER.y + LENGTH)
)
line.draw(window)
weight = gr.Circle(
    gr.Point(WINDOW_CENTER.x, WINDOW_CENTER.y + LENGTH),
    RADIUS
)
weight.draw(window)


# Update angle and angular velocity using Euler's method
def update_angle_and_velocity(theta, omega):
    alpha = -G / LENGTH * sin(theta)
    omega += alpha * TIME_STEP
    theta += omega * TIME_STEP
    return theta, omega


# Update pendulum position
def update_pendulum_position(theta):
    x = WINDOW_CENTER.x + LENGTH * sin(theta)
    y = WINDOW_CENTER.y + LENGTH * cos(theta)
    weight.move(x - weight.getCenter().x, y - weight.getCenter().y)


# Update line position
def update_line_position(line):
    line.undraw()
    line = gr.Line(WINDOW_CENTER, weight.getCenter())
    line.draw(window)


# Simulation loop
# Initial conditions
theta = pi / 2
omega = 0
while True:
    # Update angle and angular velocity
    theta, omega = update_angle_and_velocity(theta, omega)
    # Update pendulum position
    update_pendulum_position(theta)
    # Update line position
    line.undraw()
    line = gr.Line(WINDOW_CENTER, weight.getCenter())
    line.draw(window)

    gr.time.sleep(TIME_STEP)
