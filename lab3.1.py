import math


def f(x):
    # return x ** 0.5
    return math.sin(x * math.pi / 6)


n = int(input())
x_list = [float(num) for num in input().split(' ')]
x_0 = float(input())
y = [f(x) for x in x_list]


def lagrange(x_0, x):
    print("Многочлен Лагранжа: ")
    polynom = ""
    summ = 0
    n = len(x)
    for i in range(n):
        mul = 1
        w = 1
        braces = ""
        for j in range(n):
            if j != i:
                w *= x[i] - x[j]
                mul *= x_0 - x[j]
                braces += '(x - {:3.1f})'.format(x[j])
        w = f(x[i]) / w
        mul = mul * w
        summ += mul
        # вывод полинома
        if polynom != '' and w >= 0:
            polynom += '+'
        if w != 0:
            polynom += "{:3.3f}".format(w) + braces
    print(polynom)
    return summ


def newton(x_0, x):
    print("Многочлен Ньютона: ")
    polynom = ""
    summ = 0
    n = len(x)
    fi = []
    for i in range(n):
        mul = 1
        braces = ""
        for j in range(i):
            mul *= x_0 - x[j]
            braces += '(x - {:3.1f})'.format(x[j])
        fi_prev = fi.copy()
        fi = []
        for j in range(n - i):
            if i > 0:
                fi.append((fi_prev[j] - fi_prev[j + 1]) / \
                          ( x[j] - x[j + i]))
            else:
                fi.append(f(x[j]))
        w = fi[0]
        mul = mul * w
        summ += mul
        # вывод полинома
        if polynom != '' and w >= 0:
            polynom += '+'
        if w != 0 and braces != ' ':
            polynom += "{:3.3f}".format(w) + braces
    print(polynom)
    return summ


interp = lagrange(x_0, x_list)
print("Значение полученное многочленом Лагранжа: ", interp)
print("Точное значение: ", f(x_0))
print("Погрешность интерполяции: ", abs(interp - f(x_0)))
print()
interp = newton(x_0, x_list)
print("Значение полученное многочленом Ньютона: ", interp)
print("Точное значение: ", f(x_0))
print("Погрешность интерполяции: ", abs(interp - f(x_0)))
