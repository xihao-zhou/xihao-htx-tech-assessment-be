import sys
import argparse

"""Main function to run file independtently"""
def main(args):
    try:
        if 1 > len(args.input) or len(args.input) > 2000:
            print("You have entered an invalid input, ensure that input length is at lease 1 character and no longer then 2000 characters.\n")
        else:
            print(palindrome_check(args.input))
    except Exception as e:
        print("You have entered an invalid input.")
        
"""
Funtion to perform palindrome check given input string s
Step 1: Remove all non-alphanumeric characters from input
Step 2: Convert input to lower case
Step 3: Check if trimmed input is a palindrome
Return True if input is palindrome else return False
"""
def palindrome_check(s):
    s = ''.join(c for c in s if c.isalnum())
    s = s.lower()
    print(s)
    
    is_palindrome = True
    
    """
    Iterate through the sting, check if the first and the last character matches and move the pointer towards the center.
    If a mismatch is found, stop the loop and set is_palindrome to false
    """
    for i in range(len(s)):
        # print("\n"+ s[i] + " : " + s[len(s)-i-1] +"\n")
        if s[i] != s[len(s)-i-1]:
            is_palindrome = False
            break
        
    return is_palindrome

"""Funtion to parse arguments when file is run independtently"""
def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--input", type=str, nargs="?", 
        help="Enter a string to perform palindrome check.")
    
    return parser.parse_args(argv)

if __name__ == "__main__":
    main(parse_arguments(sys.argv[1:]))