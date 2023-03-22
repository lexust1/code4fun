import graphics as gr


window = gr.GraphWin("House", 800, 600)


def create_ground(top, bottom):
    ground = gr.Rectangle(gr.Point(0, top), gr.Point(800, bottom))
    ground.setFill("lightgrey")
    ground.draw(window)


def create_sky(top, bottom):
    sky = gr.Rectangle(gr.Point(0, top), gr.Point(800, bottom))
    sky.setFill("darkblue")
    sky.draw(window)


def create_house(upper_left_corner_x, upper_left_corner_y, height, width):
    # The house.
    house = gr.Rectangle(
        gr.Point(upper_left_corner_x, upper_left_corner_y),
        gr.Point(upper_left_corner_x + width, upper_left_corner_y + height)
    )
    house.setFill("grey")
    # The window and beads.
    pane = gr.Rectangle(
        gr.Point(
            upper_left_corner_x + 50,
            upper_left_corner_y + 50
        ),
        gr.Point(
            upper_left_corner_x + width - 50,
            upper_left_corner_y + height - 50
        )
    )
    pane.setFill("yellow")
    bead_vert = gr.Line(
        gr.Point(
            upper_left_corner_x + width / 2,
            upper_left_corner_y + 50
        ),
        gr.Point(
            upper_left_corner_x + width / 2,
            upper_left_corner_y + height - 50
        )
    )
    bead_hor = gr.Line(
        gr.Point(
            upper_left_corner_x + 50,
            upper_left_corner_y + height / 2
        ),
        gr.Point(
            upper_left_corner_x + width - 50,
            upper_left_corner_y + height / 2
        )
    )
    # The roof.
    roof = gr.Polygon(
        gr.Point(upper_left_corner_x, upper_left_corner_y),
        gr.Point(upper_left_corner_x + width / 2, upper_left_corner_y - 100),
        gr.Point(upper_left_corner_x + width, upper_left_corner_y)
    )
    roof.setFill("brown")
    # Draw all parts of the house.
    house.draw(window)
    pane.draw(window)
    bead_vert.draw(window)
    bead_hor.draw(window)
    roof.draw(window)


def create_cloud(x, y, r):
    cld1 = gr.Circle(gr.Point(x - 30, y - 20), r)
    cld1.setFill("white")
    cld2 = gr.Circle(gr.Point(x - 10, y - 20), r)
    cld2.setFill("white")
    cld3 = gr.Circle(gr.Point(x, y), r)
    cld3.setFill("white")
    cld4 = gr.Circle(gr.Point(x - 20, y), r)
    cld4.setFill("white")
    cld5 = gr.Circle(gr.Point(x - 40, y), r)
    cld5.setFill("white")
    cld1.draw(window)
    cld2.draw(window)
    cld3.draw(window)
    cld4.draw(window)
    cld5.draw(window)


def create_moon(x , y, radius):
    moon = gr.Circle(gr.Point(x, y), radius)
    moon.setFill("yellow")
    moon.draw(window)


def create_fir(x, y):
    # The branches.
    delta = 60
    y1 = y - 50
    y2 = y - 150
    y3 = y - 50
    for i in range(3):
        fr = gr.Polygon(
            gr.Point(x - 100, y1),
            gr.Point(x, y2),
            gr.Point(x + 100, y3))
        y1 -= delta
        y2 -= delta
        y3 -= delta
        fr.setFill("green")
        fr.draw(window)
    # The trunk.
    trunk = gr.Rectangle(gr.Point(x - 20, y - 50), gr.Point(x + 20, y))
    trunk.setFill("brown")
    trunk.draw(window)


def create_scene():
    create_ground(300, 600)
    create_sky(0, 300)
    create_house(100, 200, 200, 200)
    create_cloud(200, 70, 20)
    create_cloud(500, 50, 20)
    create_cloud(720, 100, 20)
    create_moon(600, 100, 50)
    create_fir(450, 500)
    create_fir(700, 400)


create_scene()

window.getMouse()
window.close()
