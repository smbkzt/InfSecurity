def table(choice):
    alphabet_latin_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_cyrillic_lower = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ".lower()
    if choice == 1:
        main_alph = alphabet_cyrillic_lower
    else:
        main_alph = alphabet_latin_lower

    abc = len(main_alph)
    line = ""

    for i in range(abc):
        for j in range(abc):
            if j < abc:
                line += main_alph[(j + i + abc) % abc]
            else:
                line += main_alph[(j + abc) % abc]
            line += '  '
        line += "\n"
    print(line)

if __name__ == "__main__":
    print("Кириллица(1) || Латиница(2)")
    answer = int(input())

    if answer == 1:
        table(1)
    elif answer == 2:
        table(2)
    else:
        print("Ошибка!")
