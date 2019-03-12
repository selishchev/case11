import turtle


def tree(l, n):
    if n == 0:
        return
    turtle.forward(l)
    turtle.right(30)
    tree(0.75*l, n-1)
    turtle.left(60)
    tree(0.75*l, n-1)
    turtle.right(30)
    turtle.backward(l)


def main():
    turtle.speed(1)
    turtle.left(90)
    tree(int(input()), int(input()))


if __name__ == '__main__':
    main()
