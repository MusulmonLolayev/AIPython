from py4j.java_gateway import JavaGateway

gateway = JavaGateway()
random = gateway.jvm.java.util.Random()

addition_app = gateway.entry_point

from Test.read_data import ToFormNumpy


def main():
    pass
    #X, types, y = ToFormNumpy("D:\\tanlanmalar\\spame.txt")

if __name__ == '__main__':
    main()
