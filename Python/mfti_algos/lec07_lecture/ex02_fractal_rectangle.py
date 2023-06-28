# Фрактальный квадрат, O(n)
# https://www.youtube.com/watch?v=0Bc8zLURY-c&t=1341s
import graphics as gr


def fractal_rectangle(window, a, b, c, d, alpha, deep=50):
    if deep < 1:
        return
    for p1, p2 in (a, b), (b, c), (c, d), (d, a):
        gr.Line(gr.Point(*p1), gr.Point(*p2)).draw(window)
    a1 = (a[0] * (1 - alpha) + b[0] * alpha, a[1] * (1 - alpha) + b[1] * alpha)
    b1 = (b[0] * (1 - alpha) + c[0] * alpha, b[1] * (1 - alpha) + c[1] * alpha)
    c1 = (c[0] * (1 - alpha) + d[0] * alpha, c[1] * (1 - alpha) + d[1] * alpha)
    d1 = (d[0] * (1 - alpha) + a[0] * alpha, d[1] * (1 - alpha) + a[1] * alpha)
    fractal_rectangle(window, a1, b1, c1, d1, alpha, deep - 1)


def main():
    # Set the graphics library
    window = gr.GraphWin("Fractal Rectangle", 600, 600)
    window.setBackground("white")
    # The initial settings
    alpha = 0.1
    a, b, c, d = (100, 100), (500, 100), (500, 500), (100, 500)
    fractal_rectangle(window, a, b, c, d, alpha)
    # Close the window
    window.getMouse()


if __name__ == "__main__":
    main()
