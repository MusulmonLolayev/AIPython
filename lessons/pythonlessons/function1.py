def my_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


@my_decorator  # say_whee = my_decorator(say_whee)
def say_whee(name):
    return "Whee!, {name}".format(name=name)

print(say_whee("Ali"))

@my_decorator  # say_whee = my_decorator(say_whee)
def say_whee_age(name, age):
     return "Whee!, {name}, Age = {age}".format(name=name, age=age)

print(say_whee_age("Ali", 23))



