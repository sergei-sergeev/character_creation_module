from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculatesquareroot(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    if your_number <= 0:
        return

    print(f'Мы вычислили квадратный корень из '
          f'введённого вами числа. Это будет:'
          f'{calculatesquareroot(your_number)}')


calc(25.5)
