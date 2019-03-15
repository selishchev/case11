import turtle


def minkovskiy(d, n):
    if n == 0:
        turtle.forward(d)
        return
    turtle.forward(d)
    turtle.left(90)
    turtle.forward(d)
    turtle.right(90)
    turtle.forward(d)
    turtle.right(90)
    turtle.forward(d)
    turtle.forward(d)
    turtle.left(90)
    turtle.forward(d)
    turtle.left(90)
    turtle.forward(d)
    turtle.right(90)
    turtle.forward(d)
    for i in range(n-1):
        turtle.left(90)
        minkovskiy(d, n-1)
        turtle.right(90)
        minkovskiy(d, n-1)
        turtle.right(90)
        minkovskiy(d, n-1)
        minkovskiy(d, n - 1)
        turtle.left(90)
        minkovskiy(d, n - 1)
        turtle.left(90)
        minkovskiy(d, n - 1)
        turtle.right(90)
        minkovskiy(d, n - 1)


def main():
    minkovskiy(int(input()), int(input()))
    turtle.mainloop()


if __name__ == '__main__':
    main()
