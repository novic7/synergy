# Запрос у пользователя ввода слова
word = input("Введите слово из маленьких латинских букв: ")
# Определение гласных и согласных букв
vowels = "aeiou"
vowel_count = {vowel: 0 for vowel in vowels}  # Словарь для подсчета гласных
consonant_count = 0  # Счетчик согласных
# Проход по каждому символу в слове
for char in word:
    if char in vowels:
        vowel_count[char] += 1  # Увеличиваем счетчик соответствующей гласной
    elif char.isalpha():  # Проверяем, что символ является буквой
        consonant_count += 1  # Увеличиваем счетчик согласных
# Проверка наличия каждой гласной буквы
if all(count > 0 for count in vowel_count.values()):
    print(f"Количество согласных букв: {consonant_count}")
    print("Количество каждой из гласных букв:")
    for vowel, count in vowel_count.items():
        print(f"{vowel}: {count}")
else:
    print("False")