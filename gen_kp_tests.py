import random

min_matrix = 100  # минималный размер матрицы
max_matrix = 300  # макисмальный размер матрицы
min_elem = -20  # минимальное значение элемента (вещественное)
max_elem = -min_elem  # максимальное значение элемента (вещественное)
count = 20  # приблизительное количество генерируемых элементов делёное на 2


def main():
    n = random.randint(min_matrix, max_matrix)
    print(n)
    for i in range(n):
        val = random.uniform(min_elem, max_elem)
        print(i, i, val)
    for i in range(count):
        i = random.randrange(0, n)
        j = random.randrange(0, n)
        val = random.uniform(min_elem, max_elem)
        print(i, j, val)
        if i != j:
            print(j, i, val)
    print(-1, -1, 0.)

    # свободный столбец
    for i in range(n):
        val = random.uniform(min_elem, max_elem)
        print(val)


if __name__ == '__main__':
    main()
