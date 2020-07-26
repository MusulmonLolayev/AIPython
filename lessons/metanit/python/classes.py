class Person:
    # конструктор
    def __init__(self, name):
        self.name = name  # устанавливаем имя

    def display_info(self):
        print("Привет, меня зовут", self.name)

    def __del__(self):
        print("Obyekt o'chirildi...", self.name)