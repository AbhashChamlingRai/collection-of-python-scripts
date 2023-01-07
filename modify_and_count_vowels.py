"""
Write a Python script that:
    1. defines a function that takes a string as an argument and returns a modified version of the string where all vowels are replaced with an asterisk. 
    2. counts total number of vowels present
    3. counts occurance of each vowels
"""

def change_vowels_to_asterisk(text):
    vowels_lowercase = ["a", "e", "i", "o", "u"] # List of lowercase vowels
    vowels_uppercase = ["A", "E", "I", "O", "U"] # List of Uppercase vowels

    modified_text = "" # Initialize an empty string to store the modified text

    total_vowel_occurance = 0 # Initialize a counter to store the total number of vowel occurances

    each_vowel_occurance = {} # Initialize a dictionary to store the count of each vowel occurance

    for each_letter in text:
        # If the letter is a vowel (either lowercase or uppercase)
        if each_letter in vowels_lowercase or each_letter in vowels_uppercase:
            modified_text += "*"
            total_vowel_occurance += 1
            if each_letter not in each_vowel_occurance:
                each_vowel_occurance[each_letter] = 1
            else:
                each_vowel_occurance[each_letter] += 1
        else:
            modified_text += each_letter

    # Sort the dictionary of vowel occurances by the vowel keys
    sorted_dict = dict(sorted(each_vowel_occurance.items(), key=lambda x: x[0]))

    return modified_text, total_vowel_occurance, sorted_dict

if __name__ == "__main__":
    my_sentences = "My name is Abhash Rai. I am a student of Birmingham City University."
    modified_sentences, total_vowel_count, each_vowel_count = change_vowels_to_asterisk(my_sentences)

    print(f"\nInitial text:\n{my_sentences}")

    print(f"\nModified text:\n{modified_sentences}")

    print(f"\nTotal vowel charcters count: {total_vowel_count}")

    print("\nCount of each vowel present:")
    for vowel, count in each_vowel_count.items():
        print(f"{vowel} --> {count}")