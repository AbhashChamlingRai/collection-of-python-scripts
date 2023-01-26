"""
5.2 Create a Python program in which the following classes are defined:
    • HumanBeing, parent class
    • Boy, subclass of HumanBeing
    • Girl, subclass of Boy

The HumanBeing superclass must contain:
    a) the attributes gender and name, initialized to empty strings
    b) the set_gender method, which receives a value as mandatory parameter and assigns it to the gender attribute
    c) the get_gender method, which returns the value saved in the gender attribute
    d) the __str__ special method, which returns the string “NAME's gender is genderValue”, with the name written with capital letters

The Boy's and Girl's constructor method __init__ must:
    a) receive the name as a mandatory parameter
    b) use the set_gender method to set the gender attribute to "male" and "female" respectively

Complete the program by creating an instance for each class and printing their contents with the print
function.
"""

class HumanBeing:

    def __init__(self):
        self.__gender = ""
        self.__name = ""

    def set_gender(self, new_gender):
        self.__gender = new_gender
    
    def get_gender(self):
        return self.__gender

    def set_name(self, new_name):
        self.__name = new_name
    
    def get_name(self):
        return self.__name

    def __str__(self):
        return f"{self.__name.upper()}'s gender is {self.__gender}"

class Boy(HumanBeing):
    def __init__(self, name):
        super().__init__()
        self.set_gender("Male")
        self.set_name(name)

class Girl(Boy):
    def __init__(self, name):
        super().__init__(name)
        self.set_gender("Female")
        self.set_name(name)
        

def main():
    human1 = HumanBeing()
    boy1 = Boy("John")
    girl = Girl("Karen")

    objects_list = [human1, boy1, girl] 

    for each in objects_list:
        print()
        print(each)
        print(each.get_gender())

if __name__ == "__main__":
    main()