import traceback

def traceback_printer(): #creating a error traceback printer which prints error message without terminating the program
    traceback_str = traceback.format_exc()
    print(traceback_str)






print("------------------------------------------------------------------------------------")




""" 1. If the constructor is not present in the child class, it calls the constructer of parent class to create an object. """
class Vehicle1:
    def __init__(self, vehicle_name, price):
        self.__vehicle_name = vehicle_name
        self.__price = price

    def get_vehicle_name(self):
        print("Vehicle name is:", self.__vehicle_name)
    
    def get_vehicle_price(self):
        print("Vehicle price is:", self.__price)
    
    def move_vehicle(self):
        print("Vehicle moved!")

class Car1(Vehicle1):

    # No __init__ here

    def move_car(self):
        print("Car moved!")

c1 = Car1("SUV", 1)
c1.move_vehicle()
c1.get_vehicle_name()
c1.get_vehicle_price()
c1.move_car()
print("------------------------------------------------------------------------------------")







""" 2. If child class has its own constructor, it does not call constructor from parent class. """
class Vehicle2:
    def __init__(self, vehicle_name, price):
        self.__vehicle_name = vehicle_name
        self.__price = price

    def get_vehicle_name(self):
        print("Vehicle name is:", self.__vehicle_name)
    
    def get_vehicle_price(self):
        print("Vehicle price is:", self.__price)
    
    def move_vehicle(self):
        print("Vehicle moved!")

class Car2(Vehicle2):

    def __init__(self, car_name, price):
        self.__car_name = car_name
        self.__price = price

    def get_car_name(self):
        print("Car name is:", self.__car_name)
    
    def get_car_price(self):
        print("Car name is:", self.__price)

    def move_car(self):
        print("Car moved!")

c2 = Car2("Buggati", 2)
c2.get_car_name()
c2.get_car_price()
c2.move_car()
print("------------------------------------------------------------------------------------")






""" 3. Only public attributes of parents class can be accessed by the child class directly; not the private attributes """
class Vehicle3:
    def __init__(self, vehicle_name, price):
        self.number_of_tyres = 4 # public attribute
        self.__number_of_passengers_seats = 5 # private attribute

class Car3(Vehicle3):
    def __init__(self, car_name, price):
        self.__car_name = car_name
        self.__price = price

    def vehicle_object_creator(self):
        return Vehicle3("asc", 12)

    def print_public_attribute_of_parent_class(self):
        print(self.vehicle_object_creator().number_of_tyres) # Accessing public attribute

    def print_private_attribute_of_parent_class(self):
        try:
            print(self.vehicle_object_creator().__number_of_passengers_seats) # Accessing private attribute
        except:
            print()
            traceback_printer() # Calling our function to print error without terminating program

c3 = Car3("Buggati", 3)
c3.print_public_attribute_of_parent_class()
c3.print_private_attribute_of_parent_class()
print("------------------------------------------------------------------------------------")









""" 4 Method overriding: Child class can override methods of parent class. So, method inside child class gets executed if same methond is present in both child and parent class. """


