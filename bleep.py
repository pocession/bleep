# bleep

from cs50 import get_string
from sys import argv


def main():

    # Prompt users for correct entry
    argc = len(sys.argv)
    if argc != 2:
        print("Usage: python bleep.py dictionary", end="")
        print()
        exit(1)


if __name__ == "__main__":
    main()
