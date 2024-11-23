def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for item in numbers:
        try:
            result += item
        except TypeError:
            print(f"Некорректный тип данных для подсчёта суммы - {item}")
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):
    try:
        for i in numbers:
            pass
        total, incorrect_count = personal_sum(numbers)
        try:
            average = total / (len(numbers) - incorrect_count)
        except ZeroDivisionError:
            return 0
        return average
    except TypeError:
        print("В numbers записан некорректный тип данных")
        return None

# Тестируем функции
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, символы не числа
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Суммируются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Не коллекция, ошибка
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё корректно