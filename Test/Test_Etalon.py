from Test.read_data import ToFormArray, ToFormNumpy
from ai.own.fris import Fris

def main():

    X, types, y = ToFormNumpy("D:\\tanlanmalar\\giper_my.txt")
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\MATBIO_MY.txt")

    y -= 1

    file = open("test.txt", "w")
    print(Fris(X, y, types=types, file=file))
    file.close()

if __name__ == '__main__':
    main()