from Caesar_method.Caesar import Caesar
caesar = Caesar()


def file_reader_decoder(key, file_path):
    count = 0
    print("Результат: ")
    file = open(file_path, 'r')
    for line in file:
        count += 1
        print("Строка №" + str(count) + ": " + caesar.caesar_decode(key, line))


def file_reader_encoder(key, file_path):
    count = 0
    print("Результат: ")
    file = open(file_path, 'r')
    for line in file:
        count += 1
        print("Строка №" + str(count) + ": " + caesar.caesar_encode(key, line))


def main():
    while True:
        print("\nХотите зашифровать(1) или расшифровать(2) файл?")
        answer = int(input())

        if answer == 1 or answer == 2:
            print("Введи ключ: ")
            key_to_encode_decode = int(input())
            print("Введите путь к файлу :")
            path = input().strip()  # Удаление пробелов спереди и сзади
            if answer == 1:
                file_reader_encoder(key_to_encode_decode, path)
            elif answer == 2:
                file_reader_decoder(key_to_encode_decode, path)
        else:
            print("Ошибка!")


