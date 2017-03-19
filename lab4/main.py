from random import randint


class Runner:
    user_one_private_decimal = int
    user_two_private_decimal = int
    user_one_public_decimal = int
    user_two_public_decimal = int

    g = int
    p = int

    def __init__(self, gg, pp):
        self.g = gg
        self.p = pp
        self.gen_publ_dec()

    def modfx(self, gg, x, pp):
        result = pow(gg, x) % pp
        return result

    def gen_publ_dec(self):
        self.user_one_private_decimal = randint(0, 50)
        print("Пользователь №1 генерирует случайное приватное число Х: " + str(self.user_one_private_decimal))
        self.user_one_public_decimal = self.modfx(self.g, self.user_one_private_decimal, self.p)
        print("Пользователь №1 посылает публичный результат Пользователю №2: " + str(self.user_one_public_decimal))
        f = open('D:\public_result_1.txt', 'w')
        f.write(str(self.user_one_public_decimal))
        f.close()

        self.user_two_private_decimal = randint(0, 50)
        print("\nПользователь №2 генерирует случайное приватное число Х: " + str(self.user_two_private_decimal))
        self.user_two_public_decimal = self.modfx(self.g, self.user_two_private_decimal, self.p)
        print("Пользователь №2 посылает публичный результат Пользователь №1: " + str(self.user_two_public_decimal))
        f = open('D:\public_result_2.txt', 'w')
        f.write(str(self.user_two_public_decimal))
        f.close()

    def user_one(self):
        print("Пользователь №1:")
        print("Пользователь №1 получил публичный ключ от Пользователь №2: " + str(self.user_two_public_decimal))
        result = self.modfx(self.user_two_public_decimal, self.user_one_private_decimal, self.p)
        print("Пользователь №1 создал общий секретный ключ: " + str(result))
        return result

    def user_two(self):
        print("Пользователь №2:")
        print("Пользователь №2 получил публичный ключ от Пользователь №1: " + str(self.user_one_public_decimal))
        result = self.modfx(self.user_one_public_decimal, self.user_two_private_decimal, self.p)
        print("Пользователь №2 создал общий секретный ключ: " + str(result))
        return result


if __name__ == "__main__":
    print("Выберите g")
    g = int(input())
    print("Выберите p")
    p = int(input())
    variable = Runner(g, p)
    print("____________________________________________________________________")
    variable.user_one()
    print("____________________________________________________________________")
    variable.user_two()
