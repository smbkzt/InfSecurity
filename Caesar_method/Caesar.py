class Caesar:
    alphabet_latin_upper = 'abcdefghijklmnopqrstuvwxyz'.upper()
    alphabet_latin_lower = 'abcdefghijklmnopqrstuvwxyz'

    alphabet_cyrillic_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    alphabet_cyrillic_lower = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ".lower()

    def caesar_encode(self, key, word):
        res = ''
        for char in word:
            if self.alphabet_cyrillic_lower.__contains__(char):
                res += self.alphabet_cyrillic_lower[
                    (self.alphabet_cyrillic_lower.index(char) + key) % len(self.alphabet_cyrillic_lower)]
            elif self.alphabet_cyrillic_upper.__contains__(char):
                res += self.alphabet_cyrillic_upper[
                    (self.alphabet_cyrillic_upper.index(char) + key) % len(self.alphabet_cyrillic_upper)]
            elif self.alphabet_latin_lower.__contains__(char):
                res += self.alphabet_latin_lower[
                    (self.alphabet_latin_lower.index(char) + key) % len(self.alphabet_latin_lower)]
            elif self.alphabet_latin_upper.__contains__(char):
                res += self.alphabet_latin_upper[
                    (self.alphabet_latin_upper.index(char) + key) % len(self.alphabet_latin_upper)]
        return res

    def caesar_decode(self, key, word):
        result = ''
        for char in word:
            if self.alphabet_cyrillic_lower.__contains__(char):
                result += self.alphabet_cyrillic_lower[
                    (self.alphabet_cyrillic_lower.index(char) - key) % len(self.alphabet_cyrillic_lower)]
            elif self.alphabet_cyrillic_upper.__contains__(char):
                result += self.alphabet_cyrillic_upper[
                    (self.alphabet_cyrillic_upper.index(char) - key) % len(self.alphabet_cyrillic_upper)]
            elif self.alphabet_latin_lower.__contains__(char):
                result += self.alphabet_latin_lower[
                    (self.alphabet_latin_lower.index(char) - key) % len(self.alphabet_latin_lower)]
            elif self.alphabet_latin_upper.__contains__(char):
                result += self.alphabet_latin_upper[
                    (self.alphabet_latin_upper.index(char) - key) % len(self.alphabet_latin_upper)]
        return result


def main():
    caesar = Caesar()
    while True:
        print("\nХотите зашифровать(1) или расшифровать(2) слово?")
        answer = int(input())

        if answer == 1 or answer == 2:
            print("Введи ключ: ")
            key_to_encode_decode = int(input())
            print("Введите текст для шифрования/расшифрования :")
            word_to_encode = input().strip()  # Удаление пробелов спереди и сзади

            if answer == 1:
                print()
                print(caesar.caesar_encode(key_to_encode_decode, word_to_encode))
            elif answer == 2:
                print()
                print(caesar.caesar_decode(key_to_encode_decode, word_to_encode))
        else:
            print("Ошибка!")
