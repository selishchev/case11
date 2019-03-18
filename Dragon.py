import turtle
turtle.speed(100)
def draco(size, n):
    turtle.fd(size)
    Part1(size, n - 1)


def Part1(size, n):
    if n == 0:
        return
    Part1(size, n - 1)
    turtle.right(90)
    Part2(size, n - 1)
    turtle.fd(size)
    turtle.right(90)


def Part2(size, n):
    if n == 0:
        return
    turtle.left(90)
    turtle.fd(size)
    Part1(size, n - 1)
    turtle.left(90)
    Part2(size, n - 1)


draco(int(input()), int(input()))

turtle.done()
