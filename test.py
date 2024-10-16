string = 'Hi! What about you'.lower()
count_vowel = 0
count_consonant = 0
vowels = {'a', 'e', 'i', 'o', 'u'}  # Используем множество для гласных

for i in string:
    if i.isalpha():  # Проверяем, является ли символ буквой
        if i in vowels:
            count_vowel += 1
        else:
            count_consonant += 1

print("Гласные:", count_vowel)
print("Согласные:", count_consonant)
print("Пробую создать вторую версию")