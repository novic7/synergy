# Ввод данных
X = int(input("Введите минимальную сумму инвестиций (X): "))
A = int(input("Введите сумму, которую может вложить Майкл (A): "))
B = int(input("Введите сумму, которую может вложить Иван (B): "))
# Проверка условий
michael_can_invest = A >= X
ivan_can_invest = B >= X
if michael_can_invest and ivan_can_invest:
    print(2)  # Оба могут вложиться
elif michael_can_invest:
    print("Mike")  # Только Майкл может вложиться
elif ivan_can_invest:
    print("Ivan")  # Только Иван может вложиться
elif A + B >= X:
    print(1)  # Вместе могут вложиться
else:
    print(0)  # Никто не может вложиться