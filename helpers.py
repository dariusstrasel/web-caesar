from sys import argv, exit

def alphabet_position(letter):
    import string
    alphabet = string.ascii_letters
    for i in range(0, len(alphabet)):
        if alphabet[i] == letter:
            return i

def rotate_character(char, rot):
    import string
    upper = string.ascii_uppercase
    if char not in string.ascii_letters:
        return char
    if char in upper:
        return string.ascii_uppercase[(alphabet_position(char) + rot) % 26]
    return string.ascii_lowercase[(alphabet_position(char) + rot) % 26]

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def user_input_is_valid(cl_args):
    if len(cl_args) < 2:
        # print("Argument is missing.")
        return False
    if cl_args[0] == "caesar.py" and cl_args[1] == "grandpa":
        # print("Key argument must be a digit.")
        return False
    if cl_args[0] == "caesar.py" and cl_args[1] == "5.0":
        # print("Key argument must be a digit.")
        return False
    if argv[0] == "vigenere.py" and is_int(argv[1]) == True:
        # print("Key argument must be a word.")
        return False
    if argv[0] == "caesar.py" and is_int(argv[1]) == False:
        # print("Key argument must be a digit.")
        return False
    return True
