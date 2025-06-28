from palindrome_check import palindrome_check
from num_palindrome_check import num_palindrome_check

def main(): 
    while True:
        print("1. Question 1: Palindrome Check")
        print("2. Question 2: Number Palindrome Check")
        print("0. End app.")
        choice = input("Please enter your choice: ")
    
        if choice == "1":
            print("\nPalindrome Check\n")
            s = input("Please enter a string: ")
            
            if 1 > len(s) or len(s) > 2000:
                print("You have entered an invalid input, ensure that input length is at lease 1 character and no longer then 2000 characters.\n")
            else:
                print((s + " is a palindrome.") if palindrome_check(s) else (s + " is a not a palindrome."))
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
        
if __name__ == "__main__":
   main()