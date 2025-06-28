from palindrome_check import palindrome_check
from num_palindrome_check import num_palindrome_check

def main(): 
    while True:
        print("1. Question 1: Palindrome Check")
        print("2. Question 2: Number Palindrome Check")
        print("0. Enter end app.")
        choice = input("Please enter your choice: ")
    
        if choice == "1":
            print("\nPalindrome Check\n")
            s = input("Please enter a string: ")
            palindrome_check(s)
            print("\n")
        elif choice == "2":
            print("\nPalindrome Nuumber Check\n")
            x = input("Please enter a number: ")
            num_palindrome_check(x)
            print("\n")
        elif choice == "0" or choice == "End" or choice == "end" or choice == "Stop" or choice == "stop":
            break
        else:
            print("\nYou have entered an invalid choice, please choose again.\n")
        
main()