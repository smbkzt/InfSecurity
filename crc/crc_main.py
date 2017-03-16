import binascii


def CRC32_from_file(filename):
    buf = open(filename, 'rb').read()
    string = str(hex(binascii.crc32(buf)))
    print("")
    print("CRC32: " + string)


if __name__ == "__main__":
    print("Введите путь к файлу")
    path = input()
    CRC32_from_file(path)
