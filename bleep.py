# bleep

import cs50 as cs50
import sys as sys
from cs50 import get_string
from sys import argv


def main():

    # Prompt users for correct entry
    argc = len(sys.argv)
    if argc != 2:
        print("Usage: python bleep.py dictionary", end="")
        print()
        exit(1)

    # Get users' entry
    print("Enter your string: ", end="")
    string = cs50.get_string()
    user_input = string.split()

    # Make a banned list
    banned = [line.strip() for line in open(sys.argv[1], 'r')]

    # Compare
    print(user_input, end="")
    print()
    print(banned, end="")
    print()
    a = list(set(user_input) & set(banned))

    print(a, end = "")
    print()





if __name__ == "__main__":
    main()
