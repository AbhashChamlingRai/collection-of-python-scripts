"""
How to convert a string into variable in python
"""
random_string = "unique" # This is a string

globals()[random_string] = "I am a unique variable!" # Use 'globals' when you want to create global variable
locals()[random_string] = "I am a unique variable!"  # Use 'locals' when you want to create global variable
# Line 6 & 7 are equivalent to doing --> unique = "I am a unique variable!"


print(unique)