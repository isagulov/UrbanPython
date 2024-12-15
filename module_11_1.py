import requests
import pandas as pd

# URL для запроса
url = "https://jsonplaceholder.typicode.com/posts"

# Выполняем GET-запрос
response = requests.get(url)

# Проверяем статус ответа
if response.status_code == 200:
    # Преобразуем JSON-ответ в Python-объект
    data = response.json()
    print("Первые два поста:")
    for post in data[:2]:
        print(f"ID: {post['id']}, Title: {post['title']}")
else:
    print(f"Ошибка запроса: {response.status_code}")


# Создаем данные в виде словаря
data = {
    "Имя": ["Анна", "Борис", "Виктор", "Галина"],
    "Возраст": [25, 30, 35, 40],
    "Город": ["Москва", "Санкт-Петербург", "Новосибирск", "Казань"]
}

# Создаем DataFrame
df = pd.DataFrame(data)

# Выводим DataFrame
print("Исходный DataFrame:")
print(df)

# Фильтруем строки, где возраст больше 30
filtered_df = df[df["Возраст"] > 30]
print("\nФильтруем строки, где возраст больше 30:")
print(filtered_df)

# Добавляем новый столбец
df["Возраст через 5 лет"] = df["Возраст"] + 5
print("\nДобавляем новый столбец 'Возраст через 5 лет':")
print(df)

# Группировка данных по городу (например, подсчет количества записей на город)
grouped = df.groupby("Город").size()
print("\nГруппировка данных по городу:")
print(grouped)
