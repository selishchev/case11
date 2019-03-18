import turtle


def ice(d, n):
    if n == 0:
        turtle.forward(d)
        return
    ice(d, n-1)
    turtle.left(90)
    ice(d/2, n-1)
    turtle.left(180)
    ice(d/2, n-1)
    turtle.left(90)
    ice(d, n-1)


def main():
    ice(int(input()), int(input()))
    turtle.mainloop()


if __name__ == '__main__':
    main()
