# Введення трьох чисел
a, b, c = map(int, input("Введіть три числа через пробіл: ").split())

# Знаходження найменшого і найбільшого числа
min_num = min(a, b, c)
max_num = max(a, b, c)

# Виведення результату
print(f"Найменше число: {min_num}")
print(f"Найбільше число: {max_num}")

# Введення числа в діапазоні 1–999
try:
    n = int(input("Введіть число в діапазоні 1–999: "))

    # Перевірка діапазону
    if 1 <= n <= 999:
        # Визначення парності
        parity = "парне" if n % 2 == 0 else "непарне"
        
        # Визначення кількості цифр
        if n < 10:
            digits = "однозначне"
        elif n < 100:
            digits = "двозначне"
        else:
            digits = "тризначне"
        
        # Формування рядка-опису
        description = f"{parity} {digits} число"
        print(description)
    else:
        print("Число не входить в діапазон 1–999.")
except ValueError:
    print("Введіть коректне ціле число!")

import math

# Функція обчислення площі зеленої області
def task_area_variant23():
    """Обчислення площі червоної області для варіанту 23"""
    try:
        # Ввід даних
        a = float(input("Введіть сторону квадрата (a): "))
        r = float(input("Введіть радіус кола (r): "))
        
        # Перевірка на валідність
        if r > a / 2:
            print("Радіус кола не може перевищувати половину сторони квадрата.")
            return
        
        # Обчислення площ
        square_area = a**2  # Площа квадрата
        quarter_square_area = square_area / 4  # Чверть площі квадрата
        sector_area = (math.pi * r**2) / 4  # Площа сектора кола
        
        # Червона область
        red_area = quarter_square_area - sector_area
        
        # Виведення результату
        print(f"Площа червоної області: {red_area:.10f}")
    
    except ValueError:
        print("Помилка введення! Введіть коректні числові значення.")
    except Exception as ex:
        print(f"Сталася помилка: {ex}")

# Виклик функції
task_area_variant23()