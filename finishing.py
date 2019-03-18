import ru_local
import turtle
turtle.speed(150)
turtle.up()
turtle.goto(-150, 0)
turtle.down()


#Square
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


def main_k():
    check = False
    while not check:
        try:
            n = int(input('{}'.format(ru_local.LENTH)))
            check = True
            check1 = False
            while not check1:
                try:
                    a = int(input('{}'.format(ru_local.DEEP)))
                    check1 = True
                    k(n, a)
                except ValueError:
                    check1 = False
                    print('{}'.format(ru_local.INPINT))

        except ValueError:
            check = False
            print('{}'.format(ru_local.INPINT))


#Tree#
def tree(l, n):
    if n == 0:
        return
    turtle.forward(l)
    turtle.right(45)
    tree(0.75*l, n-1)
    turtle.left(90)
    tree(0.75*l, n-1)
    turtle.right(45)
    turtle.backward(l)


def main_tree():
    turtle.left(90)
    check = False
    while not check:
        try:
            n = int(input('{}'.format(ru_local.LENTH)))
            check = True
            check1 = False
            while not check1:
                try:
                    a = int(input('{}'.format(ru_local.DEEP)))
                    check1 = True
                    tree(n, a)
                except ValueError:
                    check1 = False
                    print('{}'.format(ru_local.INPINT))

        except ValueError:
            check = False
            print('{}'.format(ru_local.INPINT))


#fractal "branch"#
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


def main_branch():
    turtle.up()
    turtle.goto(0,-100)
    turtle.left(90)
    turtle.down()
    check = False
    while not check:
        try:
            n = int(input('{}'.format(ru_local.DEEP)))
            check = True
            check1 = False
            while not check1:
                try:
                    a = int(input('{}'.format(ru_local.LENTH)))
                    check1 = True
                    branch(n, a)
                except ValueError:
                    check1 = False
                    print('{}'.format(ru_local.INPINT))

        except ValueError:
            check = False
            print('{}'.format(ru_local.INPINT))


#Kochs fractals#
def koch_snowflake(order, size):
    koch(order, size)
    turtle.right(120)
    koch(order, size)
    turtle.right(120)
    koch(order, size)


def koch(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        koch(order-1, size/3)
        turtle.left(60)
        koch(order-1, size/3)
        turtle.right(120)
        koch(order-1, size/3)
        turtle.left(60)
        koch(order-1, size/3)


def main_koch():
    turtle.up()
    turtle.goto(-100, 0)
    turtle.down()
    check = False
    while not check:
        try:
            n = int(input('{}'.format(ru_local.DEEP)))
            check = True
            check1 = False
            while not check1:
                try:
                    a = int(input('{}'.format(ru_local.LENTH)))
                    check1 = True
                    koch(n, a)
                except ValueError:
                    check1 = False
                    print('{}'.format(ru_local.INPINT))

        except ValueError:
            check = False
            print('{}'.format(ru_local.INPINT))


def main_koch_snowflake():
    turtle.up()
    turtle.goto(-100,0)
    turtle.down()
    check = False
    while not check:
        try:
            n = int(input('{}'.format(ru_local.DEEP)))
            check = True
            check1 = False
            while not check1:
                try:
                    a = int(input('{}'.format(ru_local.LENTH)))
                    check1 = True
                    koch_snowflake(n, a)
                except ValueError:
                    check1 = False
                    print('{}'.format(ru_local.INPINT))

        except ValueError:
            check = False
            print('{}'.format(ru_local.INPINT))


#Ice fractals#
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


def main_ice():
    check = False
    while not check:
        try:
            n = int(input('{}'.format(ru_local.LENTH)))
            check = True
            check1 = False
            while not check1:
                try:
                    a = int(input('{}'.format(ru_local.DEEP)))
                    check1 = True
                    ice(n, a)
                except ValueError:
                    check1 = False
                    print('{}'.format(ru_local.INPINT))

        except ValueError:
            check = False
            print('{}'.format(ru_local.INPINT))


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


def main_ice2():
    check = False
    while not check:
        try:
            n = int(input('{}'.format(ru_local.LENTH)))
            check = True
            check1 = False
            while not check1:
                try:
                    a = int(input('{}'.format(ru_local.DEEP)))
                    check1 = True
                    ice2(n, a)
                except ValueError:
                    check1 = False
                    print('{}'.format(ru_local.INPINT))

        except ValueError:
            check = False
            print('{}'.format(ru_local.INPINT))


#Minkovskiy fractals#
def minkovskiy(d, n):
    if n == 0:
        turtle.forward(d)
        return
    minkovskiy(d, n-1)
    turtle.left(90)
    minkovskiy(d, n-1)
    turtle.right(90)
    minkovskiy(d, n-1)
    turtle.right(90)
    minkovskiy(d, n-1)
    minkovskiy(d, n-1)
    turtle.left(90)
    minkovskiy(d, n-1)
    turtle.left(90)
    minkovskiy(d, n-1)
    turtle.right(90)
    minkovskiy(d, n-1)


def main_minkovskiy():
    check = False
    while not check:
        try:
            n = int(input('{}'.format(ru_local.DEEP)))
            check = True
            check1 = False
            while not check1:
                try:
                    a = int(input('{}'.format(ru_local.LENTH)))
                    check1 = True
                    minkovskiy(n, a)
                except ValueError:
                    check1 = False
                    print('{}'.format(ru_local.INPINT))

        except ValueError:
            check = False
            print('{}'.format(ru_local.INPINT))


#levy curve#
def levi(order, size):
    if order == 0:
        turtle.forward(size)

    else:
        levi(order-1, size/3)
        turtle.right(90)
        levi(order-1, size/3)
        turtle.left(90)


def main_levi():
    turtle.up()
    turtle.goto(-100,0)
    turtle.down()
    check = False
    while not check:
        try:
            n = int(input('{}'.format(ru_local.DEEP)))
            check = True
            check1 = False
            while not check1:
                try:
                    a = int(input('{}'.format(ru_local.LENTH)))
                    check1 = True
                    levi(n, a)
                except ValueError:
                    check1 = False
                    print('{}'.format(ru_local.INPINT))

        except ValueError:
            check = False
            print('{}'.format(ru_local.INPINT))


##
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


def main_draco():
    check = False
    while not check:
        try:
            n = int(input('{}'.format(ru_local.DEEP)))
            check = True
            check1 = False
            while not check1:
                try:
                    a = int(input('{}'.format(ru_local.LENTH)))
                    check1 = True
                    draco(n, a)
                except ValueError:
                    check1 = False
                    print('{}'.format(ru_local.INPINT))

        except ValueError:
            check = False
            print('{}'.format(ru_local.INPINT))


def menu():
    print('{}'.format(ru_local.SQR))
    print('{}'.format(ru_local.TREE))
    print('{}'.format(ru_local.BRANCH))
    print('{}'.format(ru_local.KOCH))
    print('{}'.format(ru_local.SNOW))
    print('{}'.format(ru_local.MINK))
    print('{}'.format(ru_local.ICE))
    print('{}'.format(ru_local.LEVI))
    print('{}'.format(ru_local.DRACO))
    check = False
    while not check:
        try:
            x = int(input('{}'.format(ru_local.CHOOSEFR)))
            check = True
            if x == 1:
                main_k()
            elif x == 2:
                main_tree()
            elif x == 3:
                main_branch()
            elif x == 4:
                main_koch()
            elif x == 5:
                main_koch_snowflake()
            elif x == 6:
                main_minkovskiy()
            elif x == 7:
                check = False
                while not check:
                    try:
                        y = int(input('{}'.format(ru_local.CHOOSEPR)))
                        check = True
                        if y == 1:
                            main_ice()
                        elif y == 2:
                            main_ice2()
                        if y != 1 or 2:
                            check = False
                            print('{}'.format(ru_local.ONEORTWO))
                    except ValueError:
                        check = False
                        print('{}'.format(ru_local.ONEORTWO))
            elif x == 8:
                main_levi()
            elif x == 9:
                main_draco()
        except ValueError:
            check = False
            print('{}'.format(ru_local.NINE))

    turtle.exitonclick()

menu()
