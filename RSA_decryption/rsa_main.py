'''
    custom rsa realization
'''
class RSA:
    '''
        rsa main class of algorith
    '''
    alphabet_latin_lower = ' abcdefghijklmnopqrstuvwxyz'
    length = len(alphabet_latin_lower)
    d = int
    n = int
    e = int
    k = int
    numbers_of_original_chars = list()
    numbers_of_encoded = list()
    numbers_of_decoded = list()
    encoded_str = str
    decoded_str = str

    def count(self, pp, qq):
        '''
            counts values using formula
            writes counted values in file to generate closed key
        '''
        self.k = (pp - 1) * (qq - 1)
        self.n = pp * qq

        for x in range(self.k + 1):
            if x == 0:
                continue
            if self.k % x is not 0:
                self.d = x
                break

        for e in range(10000):
            if ((e * self.d) % self.k) == 1:
                self.e = e
                break

        file = open(r'D:\InfSec\closed_key.txt', 'w')
        file.write(str(self.d))
        file.write("\n")
        file.write(str(self.n))
        file.close()

    def encode(self, word_to_encode):
        '''
            This method encodes data
            returns None
        '''
        # Ищет номера букв слова
        for char in word_to_encode:
            for x in self.alphabet_latin_lower:
                if x == char:
                    self.numbers_of_original_chars.append(self.alphabet_latin_lower.index(x) + 1)

        # Производит вычисления с найденными номерами и получает номера зашифрованных букв
        for number in self.numbers_of_original_chars:
            self.numbers_of_encoded.append(pow(number, self.e) % self.n)

        new_data = str(self.numbers_of_encoded)
        file = open(r'D:\InfSec\encoded_data.txt', 'w')
        file.write(str(self.numbers_of_encoded)[1:len(new_data) - 1])
        file.close()

        # Перебирает эти номера чтобы найти соответствующие им буквы
        for encoded_number in self.numbers_of_encoded:
            if encoded_number > self.length:
                self.encoded_str += self.alphabet_latin_lower[
                    (encoded_number + self.length) % self.length]
            else:
                self.encoded_str += self.alphabet_latin_lower[encoded_number % self.length]

    def decode(self, word_to_decode, dd, nn):
        '''
            Decoding method using open keys

            prints result
        '''
        t = word_to_decode.split(',')
        for char in t:
            self.numbers_of_decoded.append(pow(int(char), dd) % nn)

        for numbers in self.numbers_of_decoded:
            for chars in self.alphabet_latin_lower:
                if (numbers - 1) == self.alphabet_latin_lower.index(chars):
                    self.decoded_str += chars
        print(self.decoded_str)

    def encoding_file(self, path, path_data):
        '''
            Encodes data using encode method and writes it in the file

            returns None
        '''
        t = []
        file = open(path, 'r')
        for line in file:
            if line.find('\n'):
                t.append(line.replace('\n', ''))
        self.count(int(t[0]), int(t[1]))
        file.close()

        file = open(path_data, 'r')
        string = ''
        for line in file:
            if line.find('\n'):
                string += line.replace('\n', ' ')
            else:
                string += line
        self.encode(string)
        file.close()

    def decode_file(self, path, path_data):
        '''
            Encodes data using decode method

            returns None
        '''
        t = []
        file = open(path, 'r')
        for line in file:
            if line.find('\n'):
                t.append(line.replace('\n', ''))

        file = open(path_data, 'r')
        string = ''
        for line in file:
            if line.find('\n'):
                string += line.replace('\n', ' ')
            else:
                string += line
        file.close()
        self.decode(string, int(t[0]), int(t[1]))


if __name__ == "__main__":
    print("Зашифровать(1) /// Расшифровать(2) ??")
    rsa = RSA()
    answer = int(input())

    if answer == 1:
        print("Введите путь к открытому ключу ")
        _path = input()
        print("Введите путь к данным ")
        _path_data = input()
        rsa.encoding_file(_path, _path_data)

    elif answer == 2:
        print("Введите путь к закрытому ключу ")
        _path = input()
        print("Введите путь к зашифрованным данным ")
        _path_data = input()
        rsa.decode_file(_path, _path_data)
