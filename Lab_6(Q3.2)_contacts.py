# Creating a simple contact app

import os

def freeze():
    '''
    This function hold the output of different functions of this script for users to read it till "Enter" key is pressed.
    '''
    input("\nPress Enter to continue...") #Awating user key press for allowing the user to read terminal texts
    #Clearing the terminal so as to keep the terminal clean
    if os.name =="nt": #windows
        os.system("cls")
    else:
        os.system("clear") #unix

def menu_options():
    print("\nSelect an operation:\nv view contacts\na add contact\nd delete contact\nq quit")
    user_option = input("\nEnter choice(v/a/d/q- to quit): ")
    return user_option.lower()

def view_contacts(contact_in):
    print("\n-------- view_contacts --------\n\n")

    for counter, i in enumerate(contact_in):
        print("  {} {:<20}{:<20}".format(counter+1, i[0], i[1]))

def add_contact(contact_in):
    contact_out = contact_in
    print("\n-------- add_contact --------\n\n")

    name = input("Enter contact name: ")
    number = input("\nEnter contact number: ")

    contact_out.append((name, number))

    print(f"\n{name} - {number} has been added into the contact.")

    return contact_out

def delete_contact(contact_in):
    contact_out = contact_in
    print("\n-------- delete_contact --------\n\n")

    for counter, i in enumerate(contact_in):
        print("  {} {:<20}{:<20}".format(counter+1, i[0], i[1]))

    try:
        to_del = int(input("\n\nEnter the ID of the contact to delete: "))
        to_del -= 1 
        if to_del < 1 or to_del > len(contact_in):
            print("\nPlease enter a valid ID!")
            return contact_out

        print(f"Deleting: Record {to_del} {contact_in[to_del][0]} {contact_in[to_del][1]}")
        contact_out.pop(to_del)
        return contact_out
        
    except:
        print("\nPlease enter a valid 'number' ID!")
        return contact_out

    

def quit():
    print("\n-------- goodbye --------\n\n")

def invalid():
    print("\n-------- invalid_choice --------\n\nTry again...")


# contact = {"Abhash":255, "Dexter": 585}
def main(contacts):

    while True:
        user_code = menu_options()

        if user_code not in ["v","a","d","q"]:
            invalid()
            freeze()

        elif user_code == "v":
            view_contacts(contacts)
            freeze()

        elif user_code == "a":
            contacts = add_contact(contacts)
            freeze()

        elif user_code == "d":
            contacts = delete_contact(contacts)
            freeze()

        elif user_code == "q":
            quit()
            break

if __name__ == "__main__":
    main(contacts=[("Abhash","255"), ("Dexter","585")])