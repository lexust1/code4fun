import graphics as gr


window = gr.GraphWin("House", 800, 600)


def create_ground():
    ground = gr.Rectangle(gr.Point(0, 300), gr.Point(800, 600))
    ground.setFill("lightgrey")
    ground.draw(window)


def create_sky():
    sky = gr.Rectangle(gr.Point(0, 0), gr.Point(800, 300))
    sky.setFill("darkblue")
    sky.draw(window)


def create_house():
    # The house.
    house = gr.Rectangle(gr.Point(200, 200), gr.Point(400, 400))
    house.setFill("grey")
    # The window and beads.
    pane = gr.Rectangle(gr.Point(250, 250), gr.Point(350, 350))
    pane.setFill("yellow")
    bead_vert = gr.Line(gr.Point(300, 250), gr.Point(300, 350))
    bead_hor = gr.Line(gr.Point(250, 300), gr.Point(350, 300))
    # The roof.
    roof = gr.Polygon(
        gr.Point(200, 200),
        gr.Point(300, 100),
        gr.Point(400, 200)
    )
    roof.setFill("brown")
    # Draw all parts of the house.
    house.draw(window)
    pane.draw(window)
    bead_vert.draw(window)
    bead_hor.draw(window)
    roof.draw(window)


def create_cloud():
    cld1 = gr.Circle(gr.Point(80 - 30, 80 - 20), 20)
    cld1.setFill("white")
    cld2 = gr.Circle(gr.Point(80 - 10, 80 - 20), 20)
    cld2.setFill("white")
    cld3 = gr.Circle(gr.Point(80, 80), 20)
    cld3.setFill("white")
    cld4 = gr.Circle(gr.Point(80 - 20, 80), 20)
    cld4.setFill("white")
    cld5 = gr.Circle(gr.Point(80 - 40, 80), 20)
    cld5.setFill("white")
    cld1.draw(window)
    cld2.draw(window)
    cld3.draw(window)
    cld4.draw(window)
    cld5.draw(window)


def create_moon():
    moon = gr.Circle(gr.Point(600, 100), 50)
    moon.setFill("yellow")
    moon.draw(window)


def create_fir():
    # The branches.
    delta = 60
    y1 = 450
    y2 = 350
    y3 = 450
    for i in range(3):
        fr = gr.Polygon(
            gr.Point(500, y1),
            gr.Point(600, y2),
            gr.Point(700, y3))
        y1 -= delta
        y2 -= delta
        y3 -= delta
        fr.setFill("green")
        fr.draw(window)
    # The trunk.
    trunk = gr.Rectangle(gr.Point(600 - 20, 450), gr.Point(600 + 20, 500))
    trunk.setFill("brown")
    trunk.draw(window)


def create_scene():
    create_ground()
    create_sky()
    create_house()
    create_cloud()
    create_moon()
    create_fir()


create_scene()

window.getMouse()
window.close()
