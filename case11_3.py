import turtle


def branch(n, size):
    if n == 0:
        turtle.left(180)
        return

    x = size/(n+1)
    for i in range(n):
        turtle.forward(x)
        turtle.left(45)
        branch(n-i-1, 0.5*x*(n-i-1))
        turtle.left(90)
        branch(n-i-1, 0.5*x*(n-i-1))
        turtle.right(135)

    turtle.forward(x)
    turtle.left(180)
    turtle.forward(size)


turtle.up()
turtle.goto(0,-100)
turtle.left(90)
turtle.down()
branch(5,400)
