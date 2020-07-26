class Person:
    def __init__(self, name):
        self.name = name  # ismini o'rnatish
        self.age = 1  # yoshni o'rnatish

    def display_info(self):
        print("Ism:", self.name, "\tYosh:", self.age)


ali = Person("Ali")
ali.name = "O'rgamchak odam"  # name atributini o'zgartirish
ali.age = -129  # age atributini o'zgartirish
ali.display_info()  # Ism: O'rgamchik odam     Yosh: -129