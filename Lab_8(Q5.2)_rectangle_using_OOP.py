"""
5.2 self.
Write a Rectangle class in Python language, allowing you to build a rectangle with length and width
attributes. Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to
calculate the area of the rectangle. Create a method display() that display the length, width, perimeter and
area of an object created using an instantiation on rectangle class.
"""

class Rectangle:

    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    # def __str__(self):
    #     return self

    def perimeter(self) -> float:
        return 2*(self. __length + self.__breadth )

    def area(self) -> float:
        return self.__length * self.__breadth

    def display(self):
        print(f"\n{self}\nLength: {self.__length}\nBreadth: {self.__breadth}\nPerimeter: {self.perimeter()}\nArea: {self.area()}")

def main():
    rectangle1 = Rectangle(11,22)
    rectangle2 = Rectangle(66,99)

    rectangle1.display()
    rectangle2.display()

if __name__ == "__main__":
    main()