name = input()
number = int(input())
number_child = number % 10
number_bed = number // 10 % 10
number_group = number // 100 % 10
print(f"""Группа №{number_group}.  
{number_child}. {name}.  
Шкафчик: {number}.  
Кроватка: {number_bed}.""")
