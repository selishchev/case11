import turtle


def k(d, n):
    if n == 0:
        return
    turtle.right(20)
    turtle.up()
    turtle.forward(d/4)
    turtle.down()
    for i in range(4):
        turtle.forward(d)
        turtle.right(90)
    return k(0.9*d, n-1)


def main():
    k(int(input()), int(input()))


if __name__ == '__main__':
    main()
