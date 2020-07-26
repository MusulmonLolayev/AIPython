# Examples for object-function
def add_number(number):
    return number + 1

print(add_number(2)) # 3

def say_hello(name):
    return f"Hello, {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Ali")

print(greet_bob(say_hello)) # Hello, Ali
print(greet_bob(be_awesome)) # Yo Ali, together we are the awesomest!

# Inner functions
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child() # Calling the second inner function
    first_child() # Calling the first inner function

parent()

# Returning Functions From Functions

def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child

first = parent(1)
second = parent(2)

print(first) # <function parent.<locals>.first_child at 0x02FC04A8>
print(first()) # Hi, I am Emma

print(second) # <function parent.<locals>.second_child at 0x02FC03D0>
print(second()) # Call me Liam

# Simple Decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee() # Whee

say_whee = my_decorator(say_whee)

say_whee()  #  Something is happening before the function is called.
            #  Whee!
            #  Something is happening after the function is called.

say_whee = my_decorator(say_whee)

print(say_whee) # <function my_decorator.<locals>.wrapper at 0x008003D0>

# A fewer complexion examples
from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)

print(say_whee())# None or

# Using a little other easier syntax
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee()  #  Something is happening before the function is called.
            #  Whee!
            #  Something is happening after the function is called.
# Reusing Decorators
from lessons.realpython.decorators import do_twice

@do_twice
def say_whee():
    print("Whee!")

say_whee()  # Whee!
            # Whee!

# Decorating Functions With Arguments

@do_twice
def greet(name):
    print(f"Hello {name}")

greet("World") # Error

# Returning Values From Decorated Functions

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

hi_adam = return_greeting("Adam") # None