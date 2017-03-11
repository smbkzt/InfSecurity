class Vizhner:
    encode_key = str
    word_to_de_encode = str

    numbers_of_key = []
    numbers_of_word = []
    word_plus_key_numbers = {}

    alphabet_latin_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_cyrillic_lower = "абвгдеёжхийклмнопрстуфхцчшщъыьэюя"

    def __init__(self, key, word):
        self.encode_key = key
        self.word_to_de_encode = word

    def make_numbered_alphabet(self):
        numbered_alphabet = {}
        count = 0
        for char in self.alphabet_latin_lower:
            numbered_alphabet[count] = char
            count += 1
        return numbered_alphabet

    def find_numbers_of_key(self):
        for x in self.encode_key:
            for key, val in self.make_numbered_alphabet().items():
                if val == x:
                    self.numbers_of_key.append(key)

    def find_numbers_of_word(self):
        for x in self.word_to_de_encode:
            for key, val in self.make_numbered_alphabet().items():
                if val == x:
                    self.numbers_of_word.append(key)

    def make_word_plus_key_codes(self):
        self.find_numbers_of_key()
        self.find_numbers_of_word()
        count = 0
        iteration = 0
        len_key = len(self.encode_key)

        for i in self.numbers_of_word:
            self.word_plus_key_numbers[count] = [i, self.numbers_of_key[iteration]]
            count += 1
            iteration += 1
            if iteration >= len_key:
                iteration = 0
        print(self.word_plus_key_numbers)

    # ______________________ENCODE_____________________

    def do_encode(self):
        self.make_word_plus_key_codes()
        encoded_word = ''
        sum_of_numbers = []

        for x in self.word_plus_key_numbers:
            sum_of_numbers.append(self.word_plus_key_numbers[x][0] + self.word_plus_key_numbers[x][1])

        for x in sum_of_numbers:
            encoded_word += self.alphabet_latin_lower[int(x) % len(self.alphabet_latin_lower)]

        print(sum_of_numbers)
        print(encoded_word)

    # ______________________DECODE_____________________

    def do_decode(self):
        numbers = []
        decoded_word_latin = ''
        self.make_word_plus_key_codes()

        for x in self.word_plus_key_numbers:
            numbers.append((self.word_plus_key_numbers[x][0] - self.word_plus_key_numbers[x][1] + 26) % 26)

        for number in numbers:
            decoded_word_latin += self.alphabet_latin_lower[int(number)]

        print(numbers)
        print(decoded_word_latin)


if __name__ == "__main__":
    print("Хотите зашифровать(1) или расшифровать(2) слово? ")
    answer = int(input())
    print("Введите слово: ")
    _word = str(input())
    print("Введите ключ: ")
    _key = str(input())
    v = Vizhner(_key.lower(), _word.lower())
    if answer == 1:
        v.do_encode()
    elif answer == 2:
        v.do_decode()
    else:
        print("Ошибка!")
