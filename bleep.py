# bleep

import cs50 as cs50
import sys as sys
import re
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
    print("What message would you like to censor?", end="")
    print()
    string = cs50.get_string()
    user_input = string.split()

    # Make a banned list
    banned = [line.strip() for line in open(sys.argv[1], 'r')]

    # Compare
    lista = []
    for a in user_input:
        a_modified = a
        for b in banned:
            if a.lower() == b.lower():
                a_modified = '*' * len(a)
            elif a.lower != b.lower():
                a_modifed = a
        lista.append(a_modified)
    print(" ".join(lista))


if __name__ == "__main__":
    main()
