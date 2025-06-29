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
            
            try:
                print((f"{s} is a palindrome.") if palindrome_check(s) else (f"{s} is a not a palindrome."))
                print("\n")
            except Exception as e:
                print(f"You have entered an invalid input. {e}\n")
        
        elif choice == "2":
            print("\nPalindrome Nuumber Check\n")
            x = input("Please enter a number: ")
            
            try:
                x = int(x)
                print((f"{x} is a palindrome.") if num_palindrome_check(x) else (f"{x} is a not a palindrome."))
                print("\n")
            except Exception as e:
                print(f"You have entered an invalid number. {e}\n")
            
        elif choice == "0" or choice == "End" or choice == "end" or choice == "Stop" or choice == "stop":
            break
        else:
            print("\nYou have entered an invalid choice, please choose again.\n")
        
if __name__ == "__main__":
   main()