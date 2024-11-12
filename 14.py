def rearrange_array(arr):
    # Создаем новый массив, где элементы будут в нужном порядке
    rearranged = []
    for i in range(len(arr)):
        if i % 2 == 0:  # Четные индексы
            rearranged.append(arr[len(arr) - 1 - (i // 2)])
        else:  # Нечетные индексы
            rearranged.append(arr[i // 2])
    return rearranged

# Вводим число N
N = int(input("Введите число N: "))

# Вводим N чисел через пробел
numbers = list(map(int, input("Введите N чисел через пробел: ").split()))

# Изменяем массив
rearranged_numbers = rearrange_array(numbers)

# Выводим измененный массив
print(" ".join(map(str, rearranged_numbers)))