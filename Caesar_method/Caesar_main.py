from Caesar_method import Caesar
from Caesar_method import Caesar_file

if __name__ == "__main__":
    while True:
        print("\nХотите работать с файлом(1) или ввести слово вручную?(2) || 'выход' для выхода")
        answer = input()
        if answer == "1":
            Caesar_file.main()
        elif answer == "2":
            Caesar.main()
        elif answer.lower() == "выход":
            break
        else:
            print("Ошибка!")
