def is_palindrome(s):
    # Сравниваем строку с её обратной версией
    return s == s[::-1]

# Ввод строки
input_string = input("Введите строку: ")

# Проверка на палиндром и вывод результата
if is_palindrome(input_string):
    print("yes")
else:
    print("no")