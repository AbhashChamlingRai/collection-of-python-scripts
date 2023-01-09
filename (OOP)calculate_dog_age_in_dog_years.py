"""
create a Dog Class

Class Dog

Atibutes:
    o Name
    o size
    o Breed Defaut: 'Unknown'
    o Date of birth in DD/MM/YYYY format Default: 'Unknown'

Methods:
    o Bark
        o This should get the dog to bark (print ot the word 'Woof!')
    o get_name
        o This shoud return the dog's name
    o set_name
        o This should allow the user to set an alphabetical name between 2 and 30 characters.
        o Convert the name to title case before setting 
          (In title case, the first letter of each word in the string is capitalized, while the remaining letters are lowercase.)
    o dog_years
        o This should calculate a dog's age in dog years (use 1 year = 7 dod years)
"""

import datetime

class Dog:
    def __init__(self, name, size, breed='Unknown', date_of_birth='Unknown'):
        self.name = name
        self.size = size
        self.breed = breed
        self.date_of_birth = date_of_birth

        print(f"\n\n\nCreated a new dog instance of {self.name}")
    
    def bark(self):
        print("\nWoof!")
    
    def get_name(self):
        print(f"\nThe dog's name is {self.name}.")

    def set_name(self, new_name):
        if len(new_name) >= 2 and len(new_name) <= 30:
            each_words = new_name.split(" ") # stores each words in the user given name in a list
            title_case_modified_word = "" # Title case modified name will bestored here

            for word in each_words:
                first_letter_capital_word = ''
                for num, each_character in enumerate(word):
                    if num == 0:
                        first_letter_capital_word += each_character.upper()
                    else:
                        first_letter_capital_word += each_character
                if word != each_words[-1]:
                    title_case_modified_word += f"{first_letter_capital_word} "
                else:
                    title_case_modified_word += first_letter_capital_word
            
            self.name = title_case_modified_word
            print(f"\nNew name '{self.name}' set successfully!")

        else:
            print("\nGive a name with character length between 2 to 30!")

    def dog_years(self):
        # Parse the birth date string and convert it to a datetime object
        birth_date = datetime.datetime.strptime(self.date_of_birth, "%d/%m/%Y")

        # Get the current date
        today = datetime.datetime.now()

        # Calculate the difference between the current date and the birth date
        age = today - birth_date

        # Convert the difference to decimal years (human years)
        age_in_human_years = age.days / 365.25

        # Convert human years to dog years
        age_in_dog_years = age_in_human_years * 7

        print(f"\nIn dog years, {self.name} is {age_in_dog_years:.2f} years old.")



if __name__ == "__main__":

    dog1 = Dog("Roger", "Small", "chihuahua", "20/09/2021")
    dog1.bark()
    dog1.get_name()
    dog1.set_name("clay junior")
    dog1.dog_years()


    dog2 = Dog('Fido', 'Large', 'Labrador', '01/01/2010')
    dog2.bark()
    dog2.get_name()
    dog2.set_name("Happy harry")
    dog2.dog_years()