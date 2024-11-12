# Ввод последовательности чисел через пробел
numbers = input().split()

# Множество для хранения уже встреченных чисел
seen_numbers = set()

# Проходим по каждому числу в последовательности
for number in numbers:
    # Проверяем, встречалось ли число ранее
    if number in seen_numbers:
        print("YES")
    else:
        print("NO")
        # Добавляем число в множество
        seen_numbers.add(number)