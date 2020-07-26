# creating super class
from math import sqrt


class Taxta:
    """
    Board of chess
    8
    7
    6
    5
    4
    3
    2
    1
      A  B  C  D  E  F  G  H
    """
    def __init__(self, letter = 1, number = "A"):
        self.__letter = letter
        self.__number = number

        self.letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.numbers = [8, 7, 6, 5, 4, 3, 2, 1]

    @property
    def letter(self):
        return self.__letter
    @letter.setter
    def letter(self, letter):
        if "9" < letter and letter < "I":
            self.__letter = letter
        else:
            raise ValueError("Letter is not correct")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if 0 < number and number < 10:
            self.__number = number
        else:
            raise ValueError("Number is over the interval")
    def print(self):
        for i in self.numbers:
            print(i, end="\t")
            for j in self.letters:
                print(j + str(i), end="\t")
            print()
        print(" \t", end="")
        for j in self.letters:
            print(j, end="\t")
    def IsMove(self):
        pass

class Farzin(Taxta):
    def __init__(self, letter=1, number="A"):
        super(letter, number)

        self.let, self.num = self.convert(letter, number)

    def convert(self, letter, number):
        let = 1
        for i in range(len(Taxta.letters)):
            if Taxta.letters[i] == letter:
                self.let == i + 1
                break
        num = number
        return let, num

    """
    2 * sqrt((x1 - x2)^2 + (y1 - y2)^2) qiymati 
    2 yoki sqrt(2) teng bo'lsa, u holda farzin yurinshi mumkin.
    """
    def print(self):
        for i in range(len(self.numbers)):
            print(i, end="\t")
            for j in range(len(self.letters)):
                diff = 2 * sqrt(((i + 1) - self.num) ** 2
                                + ((j + 1) - self.let) ** 2)
                if diff == sqrt(2) or diff == 2:
                    print("X", end="\t")
                else:
                    print(j + str(i), end="\t")
            print()
        for j in self.letters:
            print(j, end="\t")
    def IsMove(self, letter, number):
        j, i = self.convert(letter, number)
        diff = 2 * sqrt((i - self.num) ** 2 + (j - self.let) ** 2)
        if diff == sqrt(2) or diff == 2:
            return True
        else:
            return False
        pass

if __name__ == '__main__':
    taxta = Taxta()
    taxta.print()

