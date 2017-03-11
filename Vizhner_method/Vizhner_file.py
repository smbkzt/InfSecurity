from Vizhner_method.Vizhner import Vizhner


def file_reader_decoder(key, file_path, lang):
    words_to_encode = ''
    print("Результат: ")
    file = open(file_path, 'r')
    for line in file:
        words_to_encode += line
    vizhner = Vizhner(key, words_to_encode, lang)
    vizhner.do_decode()


def file_reader_encoder(key, file_path, lang):
    print("Результат: ")
    file = open(file_path, 'r')
    words_to_encode = ''
    for line in file:
        words_to_encode += line
    vizhner = Vizhner(key, words_to_encode, lang)
    vizhner.do_encode()


if __name__ == "__main__":
    while True:
        print("\nХотите зашифровать(1) или расшифровать(2) файл?")
        answer = int(input())
        print("Языки английский(1) || русский(2)")
        language = int(input())

        if answer == 1 or answer == 2:
            print("Введи ключ: ")
            key_to_encode_decode = input()
            print("Введите путь к файлу :")
            path = input().strip()  # Удаление пробелов спереди и сзади
            if answer == 1:
                file_reader_encoder(key_to_encode_decode, path, language)
            elif answer == 2:
                file_reader_decoder(key_to_encode_decode, path, language)
        else:
            print("Ошибка!")
