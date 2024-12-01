import math

def find_min_max():
    """Знаходження найменшого та найбільшого числа серед трьох"""
    a, b, c = map(int, input("Введіть три числа через пробіл: ").split())
    min_num = min(a, b, c)
    max_num = max(a, b, c)
    print(f"Найменше число: {min_num}")
    print(f"Найбільше число: {max_num}")

def describe_number():
    """Опис числа (парне/непарне, однозначне/двозначне/тризначне)"""
    n = int(input("Введіть число в діапазоні 1–999: "))
    if 1 <= n <= 999:
        parity = "парне" if n % 2 == 0 else "непарне"
        if n < 10:
            digits = "однозначне"
        elif n < 100:
            digits = "двозначне"
        else:
            digits = "тризначне"
        description = f"{parity} {digits} число"
        print(description)
    else:
        print("Число не входить в діапазон 1–999.")

def calculate_green_area():
    """Обчислення площі червоної області для варіанту 23"""
    try:
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

def main():
    """Головне меню для вибору завдання"""
    while True:
        print("\nМеню:")
        print("1. Знайти найменше і найбільше число серед трьох.")
        print("2. Описати число (парне/непарне, однозначне/двозначне/тризначне).")
        print("3. Обчислити площу червоної області для варіанту 23.")
        print("4. Вихід")
        
        choice = input("Виберіть завдання (1/2/3/4): ")
        
        if choice == '1':
            find_min_max()
        elif choice == '2':
            describe_number()
        elif choice == '3':
            calculate_red_area()
        elif choice == '4':
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір! Спробуйте ще раз.")

# Викликаємо головну функцію для запуску меню
if __name__ == "__main__":
    main()