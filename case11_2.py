import turtle

#Square#
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
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    k(n, a)

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
    turtle.speed(1)
    turtle.left(90)
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    tree(n, a)

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
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    branch(n, a)


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
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    koch(n, a)

def main_koch_snowflake():
    turtle.up()
    turtle.goto(-100,0)
    turtle.down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    koch_snowflake(n, a)


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
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    ice(n, a)

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
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    ice2(n, a)


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
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    minkovskiy(n, a)


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
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    levi(n, a)


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
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    draco(n, a)





def menu():
    print('1 - Квадратичная рекурсия')
    print('2 - Дерево')
    print('3 - Фрактал "Ветка"')
    print('4 - Кривая Коха')
    print('5 - Снежинка Коха')
    print('6 - Кривая Минковского')
    print('7 - "Ледяные" фракталы\nПервый пример - 1, Второй пример - 2')
    print('8 - Кривая Леви')
    print('9 - Фрактал Дракон Хартера-Хейтуэя')
    x = input()
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
        y = input('Выберите пример')
        if y == 1:
            main_ice()
        elif y == 2:
            main_ice2()
    elif x == 8:
        main_levi()
    elif x == 9:
        main_draco()

menu()
