from helpers import rotate_character, user_input_is_valid, is_int
from sys import argv


def encrypt(text, rot):
    result = ""
    for i in text:
        result += rotate_character(i, rot)
    return result


def main(message, rotation):
    return encrypt(message, rotation)


if __name__ == '__main__':
    if user_input_is_valid(argv):
        main(input("Type a message:\n"), int(argv[1]))
