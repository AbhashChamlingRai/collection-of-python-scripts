"""
5.1 Write a program that reads integers from the user and stores them in a list. Use 0 as a sentinel
Value to mark the end of the input. Once all o the values have been read your program should
display them in reverse order.
"""


def read_from_user():
    list_user_given_order = []
    while True:
        temp_container = input("\nEnter integer value: ")
        try:
            temp_container = int(temp_container)
            if temp_container == 0:
                break
            list_user_given_order.append(temp_container)
        except:
            print("\n-- Please given an interger value only!")
            continue
    list_user_given_order.reverse()
    print()
    print(list_user_given_order) 

if __name__ == "__main__":
    read_from_user()