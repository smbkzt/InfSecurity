class Vizhner:
    encode_key = str
    word_to_encode = str

    def __init__(self, key, word):
        self.encode_key = key
        self.word_to_encode = word

    alphabet_latin_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_cyrillic_lower = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ".lower()
    word_plus_code_chars = {}

    def make_numbered_alphabet(self):
        numbered_alphabet = {}
        count = 0
        for char in self.alphabet_latin_lower:
            numbered_alphabet[count] = char
            count += 1
        return numbered_alphabet

    def make_word_plus_code(self):
        count = 0
        iter = 0
        len_key = len(self.encode_key)
        for i in self.word_to_encode:
            self.word_plus_code_chars[count] = [i, self.encode_key[iter]]
            count += 1
            iter += 1
            if iter >= len_key:
                iter = 0

    def do_encode(self):
        self.make_word_plus_code()
        print(self.word_plus_code_chars)
        encoded_word = ''
        key1 = 0
        key2 = 0
        char_count_latin = 0
        answer_latin = []

        for x in self.word_plus_code_chars:
            for char in self.alphabet_latin_lower:
                if self.word_plus_code_chars[x][0] == char:
                    key1 = char_count_latin
                if self.word_plus_code_chars[x][1] == char:
                    key2 = char_count_latin
                char_count_latin += 1

            answer_latin.append(key2 + key1)

        for x in answer_latin:
            encoded_word += self.alphabet_latin_lower[int(x) % len(self.alphabet_latin_lower)]

        print(encoded_word)


# ______________________DECODE_____________________

class VezhnerDecode:
    encode_key = str
    word_to_decode = str
    decoded_word_plus_code_chars = {}

    def __init__(self, key, word):
        self.encode_key = key
        self.word_to_decode = word

    def make_encoded_word_plus_code(self):
        count = 0
        iter = 0
        len_key = len(self.encode_key)
        for i in self.word_to_decode:
            self.decoded_word_plus_code_chars[count] = [i, self.encode_key[iter]]
            count += 1
            iter += 1
            if iter >= len_key:
                iter = 0
        print(self.decoded_word_plus_code_chars)

    def do_decode(self):
        numbers_of_decoded_words = []
        vizhner = Vizhner()
        alphabet = vizhner.make_numbered_alphabet()
        print(alphabet)

        code_of_decoded_char = 0

        for char in self.word_to_decode:
            for key, value in alphabet.items():
                if char == value:
                    numbers_of_decoded_words.append(key)

        for number in numbers_of_decoded_words:
            pass



        print(numbers_of_decoded_words)


if __name__ == "__main__":
    # print("Введите слово для шифрования: ")
    # _word = str(input())
    # print("Введите ключ: ")
    # _key = str(input())
    # variable = Vizhner(_key, _word)
    # variable.do_encode()
    # variable.do_decode()

    var = VezhnerDecode("code", "inform")
    var.make_encoded_word_plus_code()
