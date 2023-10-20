import os
from difflib import SequenceMatcher

def similar(a, b):
    # Вычисляет процент сходства между строками a и b.
    return SequenceMatcher(None, a, b).ratio()

def compare_files(file1, file2):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        content1 = f1.read()
        content2 = f2.read()
        similarity = 100 * similar(content1, content2)
        return similarity

def compare_directories(dir1, dir2, similarity_threshold):
    # Получаем список файлов в каждой директории
    files_dir1 = [os.path.join(dir1, f) for f in os.listdir(dir1)]
    files_dir2 = [os.path.join(dir2, f) for f in os.listdir(dir2)]

    for file1 in files_dir1:
        for file2 in files_dir2:
            similarity = compare_files(file1, file2)
            if similarity >= similarity_threshold:
                if (similarity == 100):
                    print(f"{file1} - {file2} - Полное сходство")
                else:
                    print(f"{file1} - {file2} - {similarity:.2f}%")

    # Находим файлы, которые есть в одной директории, но отсутствуют в другой
    for file1 in files_dir1:
        found = False
        for file2 in files_dir2:
            if compare_files(file1, file2) >= similarity_threshold:
                found = True
                break
        if not found:
            print(f"Файла {file1} нет в директории {dir2}")

    for file2 in files_dir2:
        found = False
        for file1 in files_dir1:
            if compare_files(file1, file2) >= similarity_threshold:
                found = True
                break
        if not found:
            print(f"Файла {file2} нет в директории {dir1}")

if __name__ == "__main__":
    dir1 = "dir1"
    dir2 = "dir2"
    similarity_threshold = int(input("Введите процент сходства, сэр: "))  # Процент сходства для сравнения файлов

    compare_directories(dir1, dir2, similarity_threshold)
