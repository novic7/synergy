def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def factorial_list(n):
    # Находим факториал числа n
    fact_n = factorial(n)
    
    # Создаем список факториалов от fact_n до 1
    fact_list = [factorial(i) for i in range(fact_n, 0, -1)]
    
    return fact_list

# Пример использования
number = 3
result = factorial_list(number)
print(f"Факториал числа {number} равен {factorial(number)}")
print("Список факториалов в убывающем порядке:", result)