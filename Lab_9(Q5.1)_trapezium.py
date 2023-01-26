"""
Create a Trapezium class with the following features:
    a) the constructor method (__init__) must initialize the attributes of the trapezium (majorBase, minorBase and height) using the mandatory parameters B, b and h provided by the user
    
    b) it must contain the area method to calculate and return the Trapezium area (formula: Area = (B + b)∙ h/2 ), returning an explanatory text string if the user inserts non-numerical inputs
    
    c) it must contain the __str__ special method to create its text representation with a text string similar to the following (allow the user to insert a null or negative minor base in order to transform the trapezium into a triangle):

The object created is a trapezium/triangle with the following features:
    - B = xxx
    - b = xxx
    - h = xxx
    - area = #,###.###

To test the class, complete the program by creating the following instances and displaying their
content with the print function:

            object_name             B                 b                   h
                Tr1                300               100                 250 
                Tr2               21.36               0                  9.7 
                Tr3               twenty              12                   5 
                Tr4                 20              twelve                 5 
"""

class Trapezium:

    def __init__(self, B, b, h):
        self.__majorBase = B
        self.__minorBase = b
        self.__height = h

    def area(self):
        if type(self.__majorBase) not in [int, float] or type(self.__minorBase) not in [int, float] or type(self.__height) not in [int, float]:
            print("One or more of the parameter provided to the class are non-numeric! Provide numeric values.")
        else:
            return (self.__majorBase + self.__minorBase) * (self.__height / 2)

    def __str__(self):
        return f"Giving either first or the second parameter a value of '0' will transform the trapezium into a triangle with a verticalheight of third parameter."

def main():
    Tr1 = Trapezium(300, 100, 250)
    Tr2 = Trapezium(21.36, 0, 9.7)
    Tr3 = Trapezium("twenty", 12, 5)
    Tr4 = Trapezium(20, "twenty", 5)

    Trs = [Tr1,Tr2, Tr3, Tr4]

    for Tr in Trs:
        print()
        print(Tr)

        area_val = Tr.area()
        if area_val != None:
            print(f"{area_val:.2f}")
        else:
            print(area_val)

if __name__ == "__main__":
    main()