from datetime import datetime

def get_day_of_week(day, month, year):
    date = datetime(year, month, day)
    return date.strftime("%A")

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_age(day, month, year):
    today = datetime.now()
    birth_date = datetime(year, month, day)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def print_date_with_stars(day, month, year):
    day_str = f"{day:02d}"
    month_str = f"{month:02d}"
    year_str = f"{year:04d}"
    
    date_str = f"{day_str} {month_str} {year_str}"
    for char in date_str:
        if char == ' ':
            print(' ', end=' ')
        else:
            print('*' * len(char), end=' ')
    print()

def main():
    day = int(input("Введите день рождения (1-31): "))
    month = int(input("Введите месяц рождения (1-12): "))
    year = int(input("Введите год рождения (например, 1990): "))

    # Определяем день недели
    day_of_week = get_day_of_week(day, month, year)
    print(f"День недели: {day_of_week}")

    # Проверяем, был ли год високосным
    leap_year = is_leap_year(year)
    if leap_year:
        print(f"{year} год был високосным.")
    else:
        print(f"{year} год не был високосным.")

    # Рассчитываем возраст
    age = calculate_age(day, month, year)
    print(f"Сейчас вам {age} лет.")

    # Выводим дату рождения в формате с звёздочками
    print("Дата рождения в формате с звёздочками:")
    print_date_with_stars(day, month, year)

if __name__ == "__main__":
    main()
# Описание программы:
# get_day_of_week: Определяет, какому дню недели соответствует заданная дата.
# is_leap_year: Проверяет, является ли год високосным.
# calculate_age: Рассчитывает возраст пользователя на основе даты рождения.
# print_date_with_stars: Выводит дату рождения в формате, где каждая цифра заменена на звёздочки.
# main: Основная функция, которая запрашивает у пользователя дату рождения и вызывает другие функции для выполнения поставленных задач.