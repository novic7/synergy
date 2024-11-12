def min_boats(weights, max_weight):
    weights.sort()  # Сортируем веса рыбаков
    left = 0  # Указатель на самого легкого рыбака
    right = len(weights) - 1  # Указатель на самого тяжелого рыбака
    boats = 0  # Счетчик лодок

    while left <= right:
        # Проверяем, можем ли поместить самого легкого и самого тяжелого рыбаков в одну лодку
        if weights[left] + weights[right] <= max_weight:
            left += 1  # Убираем самого легкого
        right -= 1  # Убираем самого тяжелого
        boats += 1  # Увеличиваем счетчик лодок

    return boats

# Вводим максимальный вес, который может выдержать лодка
m = int(input("Введите максимальный вес лодки: "))

# Вводим количество рыбаков
n = int(input("Введите количество рыбаков: "))

# Вводим веса рыбаков
weights = []
for _ in range(n):
    weight = int(input())
    weights.append(weight)

# Вычисляем минимальное количество лодок
result = min_boats(weights, m)

# Выводим результат
print(result)