"""
5.4 
Create a class Person with the following features:
    a. In the method (__init__) the name, surname, birthdate, address, telephone and email.
    b. Calculate the age of the person based on the current date (import datetime)
"""

import datetime

class Person:
    
    def __init__(self, name: str, surname: str, birthdate: str, address: str, telephone: str, email: str):
        self.__name = name
        self.__surname = surname
        self.__birthdate = birthdate
        self.__address = address
        self.__telephone = telephone
        self.__email = email

    def age_calcuator(self):
        date_obj = datetime.datetime.strptime(self.__birthdate, "%d-%m-%Y")
        difference = datetime.datetime.now()-date_obj
        diff_in_days = difference.days
        diff_in_years = diff_in_days / 365
        print(f"Age: {diff_in_years:.2f} years")
        


def main():
    man_1 = Person("Gary", "White", "14-09-1996", "Birmingham", "+12344", "GaryKO1@gmail.com")
    man_1.age_calcuator()


if __name__ == "__main__":
    main()