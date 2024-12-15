import time
from multiprocessing import Pool

# Функция для считывания данных из файла
def read_info(name):
    all_data = []  # Локальный список для хранения строк
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

if __name__ == '__main__':
    # Список файлов для чтения
    filenames = [f'file {number}.txt' for number in range(1, 5)]  # Формат "file 1.txt", "file 2.txt" и т.д.

    # Линейное выполнение
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_time = time.time() - start_time
    print(f"Линейный подход: {linear_time:.6f} секунд")

    # Многопроцессное выполнение
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    multiprocessing_time = time.time() - start_time
    print(f"Многопроцессный подход: {multiprocessing_time:.6f} секунд")