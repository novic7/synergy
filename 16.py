# Ввод количества чисел
N = int(input())

# Ввод самих чисел и преобразование их в список
numbers = list(map(int, input().split()))

# Используем множество для нахождения уникальных чисел
unique_numbers = set(numbers)

# Выводим количество уникальных чисел
print(len(unique_numbers))