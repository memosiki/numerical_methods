from lab3_1 import newton


def derivative(x, y, val, calc_second=True):
    n = len(x)
    k = 0
    try:
        while x[k + 1] < val:
            k += 1
    except IndexError:
        print("Значение не входит в заданный интервал")
        exit(1)

    if k + 1 > n + 1:
        k -= 1  # самый последний элемент
    # апроксимация отрезками прямой
    first = (y[k + 1] - y[k]) / (x[k + 1] - x[k])

    # апроксимация многочленом второй степени
    first = first + \
            ((y[k + 2] - y[k + 1]) / (x[k + 2] - x[k + 1]) - (y[k + 1] - y[k]) / (x[k + 1] - x[k])) * \
            (2 * val - x[k] - x[k + 1]) / \
            (x[k + 2] - x[k])

    # апроксимация многочленом Ньютона
    first_new = newton(val, x, show=False)

    y_diff = [newton(elem, x, show=False) for elem in x]

    if calc_second:
        _, second_new, _, _ = derivative(x, y_diff, val, calc_second=False)
        # Для вычисления второй производной, необходимо использовать
        # интерполяционный многочлен, как минимум второй степени.
        second = 2 * ((y[k + 2] - y[k + 1]) / (x[k + 2] - x[k + 1]) - (y[k + 1] - y[k]) / (x[k + 1] - x[k])) \
                 / (x[k + 2] - x[k])
    else:
        second_new = second = None

    return first, first_new, second, second_new


def main():
    x = [float(num) for num in input().split(' ')]
    y = [float(num) for num in input().split(' ')]
    val = float(input())
    first, first_new, second, second_new = derivative(x, y, val)
    print("В точке ", val)
    print("Первая производная многочленом 2 степени", first)
    print("Первая производная многочленом Ньютона {} степени".format(len(x)), first_new)
    print("Разница: ", abs(first - first_new))
    print("Вторая производная многочленом 2 степени", second)
    print("Вторая производная многочленом Ньютона {} степени".format(len(x)), second_new)
    print("Разница: ", abs(second - second_new))
# # TODO: Сделать вычисление производных с помощью многочлена Ньютона
# Для второй придётся вычислять прозводную от этого многочлена


if __name__ == '__main__':
    main()
