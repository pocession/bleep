# Practice check_item

def main():
    months_list = ["January", "February", "March", "April", "May", "June", "July"]

    answer = input("Enter a month? ")
    if any(answer.lower() == a.lower() for a in months_list):
        print("Great, we find the month in the list")
    else:
        print("Sorry, we didn't find the month in the list")

# run the main program
if __name__ == "__main__":
    main()