print ("hello world")
a1 = 1
a2 = 2
a3 = 3
print(a1, a2, a3, sep='+')  # Вывод: 1+2+3

def main():
    # Запрашиваем данные у пользователя
    pet_type = input("Введите вид питомца: ")
    pet_name = input("Введите кличку питомца: ")
    pet_age = input("Введите возраст питомца: ")
    
    # Формируем строку с данными
    result = f"Это {pet_type} по кличке \"{pet_name}\". Возраст: {pet_age} года."
    
    # Выводим результат
    print(result)

if __name__ == "__main__":
    main()