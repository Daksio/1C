import pickle

text_to_write = input()

# Преобразуем текст в бинарное представление и записываем в файл
with open("file.bin", 'wb') as binary_file:
    binary_text = pickle.dumps(text_to_write)
    binary_file.write(binary_text)