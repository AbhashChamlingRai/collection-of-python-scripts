"""
5.3 
Create a Person class with the following features:

    a. in the method (__init__) the name attribute (mandatory) and the age attribute (optional, to be set
    equal to -1 by default) must be defined

    b. it contains a method, called hello, which:
        1. receives the name of the friend you want to greet as a mandatory parameter
        2. converts the name of the friend to upper case
        3. prints the following message: Hello FRIEND, I am XXX and I'm YY years old (the last part of the sentence must be omitted if the age is not defined, i.e. it is equal to -1)

The main program creates the following instances:
Object name              name            age
man_1                     Al              31
girl_1                   Wanda            


Then apply the hello method to the objects just created, greeting a friend called Jack.
"""


class Person:
    
    def __init__(self, name: str, age: int = -1):
        self.__name = name
        self.__age = age

    def hello(self, friend_name: str):
        friend_name = friend_name.upper()
        if self.__age != -1:
            print(f"\nHello {friend_name}, I am {self.__name} and I'm {self.__age} years old.")
        else:
            print(f"\nHello {friend_name}, I am {self.__name}.")


def main():
    man_1 = Person("Al", 31)
    girl_1 = Person("Wanda")

    man_1.hello("Naomi")
    girl_1.hello("Joe")


if __name__ == "__main__":
    main()