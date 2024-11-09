# Запрос у пользователя ввода целого числа
number = int(input("Введите целое число: "))
# Проверка на ноль
if number == 0:
    description = "нулевое число"
else:
    # Определение знака числа
    if number > 0:
        sign = "положительное"
    else:
        sign = "отрицательное"
    
    # Проверка на четность
    if number % 2 == 0:
        parity = "четное"
    else:
        parity = "нечетное"
    
    # Формирование описания числа
    description = f"{sign} {parity} число"
# Проверка на нечетность
if number % 2 != 0:
    print(description)
    print("число не является четным")
else:
    print(description)