import sys
import argparse

"""Main function to run file independtently"""
def main(args):
    try:
        print(palindrome_check(args.input))
    except Exception as e:
        print(f"You have entered an invalid input.{e}")
        
"""
Funtion to perform palindrome check given input string s
Step 1: Remove all non-alphanumeric characters from input
Step 2: Convert input to lower case
Step 3: Check if trimmed input is a palindrome
Return True if input is palindrome else return False
"""
def palindrome_check(s):
    
    is_palindrome = True
    
    if 1 > len(s) or len(s) > 2000:
        raise Exception("Ensure that input length is at lease 1 character and no longer then 2000 characters.\n")
    else:
        s = ''.join(c for c in s if c.isalnum())
        s = s.lower()
        
        if s != "":
            """
            Iterate through the sting, check if the left most and the right most character matches and move the pointer towards the center.
            If a mismatch is found, stop the loop and set is_palindrome to false
            """
            for i in range((len(s)//2) + 1):
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