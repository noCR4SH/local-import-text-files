THIS_IS_CONST = "Hello World!"

def greetings(name):
    print(f"Hello {name}")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello! My name is {self.name}!\nI'm {self.age} years old.")