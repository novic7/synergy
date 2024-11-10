def reduce_spaces(s):
    # Используем метод split для разделения строки по пробелам и join для объединения
    return ' '.join(s.split())

# Ввод строки
input_string = input("Введите строку: ")

# Преобразование пробелов и вывод результата
result_string = reduce_spaces(input_string)
print(result_string)