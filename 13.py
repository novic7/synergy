# Вводим число N
N = int(input("Введите число N: "))

# Инициализируем список для хранения чисел
numbers = []

# Вводим N чисел
for _ in range(N):
    number = int(input())
    numbers.append(number)

# Переворачиваем массив
reversed_numbers = numbers[::-1]

# Выводим перевернутый массив
for num in reversed_numbers:
    print(num)