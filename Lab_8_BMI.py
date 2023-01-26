class BMI:

    def __init__(self):
        __weight = 0 # Initilizing variable with value 0
        __height = 0 # Initilizing variable with value 0
    
    def set_weight(self, w: float):
        self.__weight = w
    
    def set_height(self, h: float):
        self.__height = h

    def __cal_BMI(self) -> float:
        BMI = self.__weight/(self.__height**2)
        return BMI
    
    def display_BMI(self):
        BMI = self.__cal_BMI()
        print(f"\nBMI is {BMI:.2f}")


if __name__ == "__main__":
    person1 = BMI()
    person1.set_weight(74.84)
    person1.set_height(1.88)
    person1.display_BMI()
    