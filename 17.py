# Ввод первого списка чисел
list1 = set(map(int, input().split()))

# Ввод второго списка чисел
list2 = set(map(int, input().split()))

# Находим пересечение двух множеств
intersection = list1.intersection(list2)

# Выводим количество общих чисел
print(len(intersection))