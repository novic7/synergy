# Запрос у пользователя ввода пятизначного целого числа
number = int(input("Введите пятизначное целое число: "))
# Извлечение цифр из числа
ten_thousands = number // 10000 % 10  # Десятки тысяч
thousands = number // 1000 % 10        # Тысячи
hundreds = number // 100 % 10          # Сотни
tens = number // 10 % 10                # Десятки
units = number % 10                     # Единицы
# Возведение количества десятков в степень количества единиц
result = (tens ** units) * hundreds
# Вычисление разности между количеством десятков тысяч и количеством тысяч
difference = ten_thousands - thousands
# Проверка, чтобы избежать деления на ноль
if difference != 0:
    final_result = result / difference
    print(f"Результат: {final_result}")
else:
    print("Ошибка: деление на ноль.")