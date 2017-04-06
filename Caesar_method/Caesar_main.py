from Caesar import Caesar
from Caesar_file import CaesarFile

if __name__ == "__main__":
    caesar = Caesar()
    caesar_file = CaesarFile()
    while True:
        print("\nХотите работать с файлом(1) или ввести слово вручную?(2) || 'выход' для выхода")
        answer = input()
        if answer == "1":
            caesar_file.main()
        elif answer == "2":
            caesar.main()
        elif answer.lower() == "выход":
            break
        else:
            print("Ошибка!")
