import turtle


def ice2(d, n):
    if n == 0:
        turtle.forward(d)
        return
    ice2(d, n-1)
    turtle.left(120)
    ice2(d/2, n-1)
    turtle.left(180)
    ice2(d/2, n-1)
    turtle.left(120)
    ice2(d/2, n-1)
    turtle.left(180)
    ice2(d/2, n-1)
    turtle.left(120)
    ice2(d, n-1)


def main():
    ice2(int(input()), int(input()))
    turtle.mainloop()


if __name__ == '__main__':
    main()
