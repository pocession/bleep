# Practice replace

def main():
    a = input("String: ")
    a_modified = ''.join([w.replace("i", "*") for w in a])

    print("Your entry: '{a}' is changed to: '{a_modified}'".format(a = a, a_modified = a_modified), end="")
    print()

# run the main program
if __name__ == "__main__":
    main()