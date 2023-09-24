import turtle

jerry = turtle.Turtle()


def move_forward():
    jerry.forward(20)


def move_backward():
    jerry.backward(20)


def move_clockwise():
    jerry.left(45)


def move_anticlockwise():
    jerry.right(45)


def undo_recent():
    jerry.undo()


def clear_drawing():
    jerry.reset()


def draw_curve():
    jerry.circle(50, 10)


screen = turtle.Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_clockwise)
screen.onkey(key="d", fun=move_anticlockwise)
screen.onkey(key="Right", fun=draw_curve)
screen.onkey(key="BackSpace", fun=undo_recent)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()

