from datetime import datetime

def is_leap_year(year):
    """Проверяет, является ли год високосным."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def day_of_week(day, month, year):
    """Определяет день недели для заданной даты на русском языке."""
    days_of_week = {
        0: "Понедельник",
        1: "Вторник",
        2: "Среда",
        3: "Четверг",
        4: "Пятница",
        5: "Суббота",
        6: "Воскресенье"
    }
    date = datetime(year, month, day)
    return days_of_week[date.weekday()]  # Возвращает день недели на русском

def calculate_age(birth_date):
    """Вычисляет возраст пользователя на основе даты рождения."""
    today = datetime.now()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def mask_date(date_str):
    """Заменяет цифры в строке даты на звёздочки."""
    return ''.join('*' if char.isdigit() else char for char in date_str)

def main():
    # Запрашиваем у пользователя дату рождения в формате ДД.ММ.ГГГГ
    birth_date_input = input("Введите дату рождения (в формате ДД.ММ.ГГГГ): ")
    
    # Разбиваем введенную строку на день, месяц и год
    day, month, year = map(int, birth_date_input.split('.'))

    # Формируем дату рождения
    birth_date = datetime(year, month, day)

    # Определяем день недели
    week_day = day_of_week(day, month, year)

    # Проверяем, был ли год високосным
    leap_year_message = f"{year} год {'был' if is_leap_year(year) else 'не был'} високосным."

    # Вычисляем возраст
    age = calculate_age(birth_date)

    # Выводим результаты
    print(f"Вы родились в {week_day}.")
    print(leap_year_message)
    print(f"Сейчас вам {age} лет.")
    # Заменяем цифры в дате рождения на звёздочки
    masked_date = mask_date(birth_date.strftime('%d.%m.%Y'))
    print(f"Ваша дата рождения: {masked_date}")

if __name__ == "__main__":
    main()
