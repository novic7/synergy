# Ввод целых чисел A и B
A = int(input("Введите целое число A (A ≤ B): "))
B = int(input("Введите целое число B: "))

# Список для хранения четных чисел
even_numbers = []

# Поиск четных чисел в заданном диапазоне
for number in range(A, B + 1):
    if number % 2 == 0:  # Проверяем, является ли число четным
        even_numbers.append(number)

# Вывод четных чисел через пробел
print("Четные числа на отрезке от A до B:", ' '.join(map(str, even_numbers)))