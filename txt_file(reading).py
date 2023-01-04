#Reading from a text file

def read_entire_text_file_at_once(text_file_path):
    """
    This function takes a file path as input and reads the entire text file at once using readlines().
    It then prints the contents of the text file to the console.
    """
    with open(text_file_path, "r") as text_file:
        print()
        entire_text_file = text_file.readlines()
        print("\nUsing readlines():\n")
        print(entire_text_file) # --> Gives each line as elements in a list.

def iterate_over_each_line_of_text_file(text_file_path):
    """
    This function takes a file path as input and iterates over each line in the text file.
    It then prints the line number and the line itself to the console.
    """
    with open(text_file_path, "r") as text_file:
        print("\nIterating over each line in the text file:\n")
        for index_, line in enumerate(text_file): # --> iterating over each line and then printing each line
            print(f"Line {index_+1} --> {line.strip()}") # line.strip() is used to remove newline character "\n" so there won't be extra empty lines 

if __name__ == "__main__":
    read_entire_text_file_at_once("./sample.txt")

    print("\n\n\n") # Printing three empty lines
    iterate_over_each_line_of_text_file("./sample.txt")
