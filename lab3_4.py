def derivative(x, y, val):
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
    first_1 = (y[k + 1] - y[k]) / (x[k + 1] - x[k])

    # апроксимация многочленом второй степени
    first_2 = first_1 + \
              ((y[k + 2] - y[k + 1]) / (x[k + 2] - x[k + 1]) - (y[k + 1] - y[k]) / (x[k + 1] - x[k])) * \
              (2 * val - x[k] - x[k + 1]) / \
              (x[k + 2] - x[k])

    # Для вычисления второй производной, необходимо использовать
    # интерполяционный многочлен, как минимум второй степени.
    second = 2 * ((y[k + 2] - y[k + 1]) / (x[k + 2] - x[k + 1]) - (y[k + 1] - y[k]) / (x[k + 1] - x[k])) \
             / (x[k + 2] - x[k])

    return first_2, second


def main():
    x = [float(num) for num in input().split(' ')]
    y = [float(num) for num in input().split(' ')]
    val = float(input())
    first, second = derivative(x, y, val)
    print("В точке ", val)
    print("Первая производная ", first)
    print("Вторая производная ", second)


if __name__ == '__main__':
    main()
