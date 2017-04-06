'''
    Caesar encoder/decoder from file
'''
from Caesar import Caesar


class CaesarFile(Caesar):
    '''
        Main class of caesar file encoder/decoder
        Takes functionality from Caesar file and use it to write/read from file
    '''
    def file_reader_decoder(self, key, file_path):
        '''
            decode data from file using algorithm in caesar file
        '''
        count = 0
        print("Результат: ")
        file = open(file_path, 'r')
        for line in file:
            count += 1
            print("Строка №" + str(count) + ": " + self.caesar_decode(key, line))
        file.close()

    def file_reader_encoder(self, key, file_path):
        '''
            encode data from file using algorithm in caesar file
        '''
        count = 0
        print("Результат: ")
        file = open(file_path, 'r')
        for line in file:
            count += 1
            print("Строка №" + str(count) + ": " + self.caesar_encode(key, line))
        file.close()

    def main(self):
        while True:
            print("\nХотите зашифровать(1) или расшифровать(2) файл?")
            answer = int(input())

            if answer == 1 or answer == 2:
                key_to_encode_decode = int(input("Введи ключ: "))
                path = input("Введите путь к файлу :").strip()  # Удаление пробелов спереди и сзади
                if answer == 1:
                    self.file_reader_encoder(key_to_encode_decode, path)
                elif answer == 2:
                    self.file_reader_decoder(key_to_encode_decode, path)
            else:
                print("Ошибка!")


if __name__ == '__main__':
    caesar_file = CaesarFile()
    caesar_file.main()
    