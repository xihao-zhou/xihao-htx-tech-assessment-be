import sys
import argparse
import math

"""Main function to run file independtently"""
def main(args):
    try:
        if -2**31 > args.input or args.input > (2**31)-1:
            print("You have entered an invalid number, ensure that input length is is between -2^31 and (2^31 - 1).")
        else:
            print(num_palindrome_check(args.input))
    except Exception as e:
        print("You have entered an invalid number.")
        print(e)

"""
Funtion to perform palindrome check given input number x
Return True if input is palindrome else return False
"""
def num_palindrome_check(x):
    print(x)
    
    is_palindrome = True
    
    """Check if number is negative, negative number will always be non-palindrome"""
    if x < 0:
        is_palindrome = False
    else:
        """
        Iterate through the number, check if the left most and the right most number matches and move the pointer towards the center.
        If a mismatch is found, stop the loop and set is_palindrome to false
        """
        n = x
        x_len = int(math.log10(x))+1
        for i in range((x_len//2) + 1):
            first = (x // 10**(x_len-i-1)) % 10
            last = n % 10
            n = n // 10
            if first != last:
                is_palindrome = False
                break
    
    return is_palindrome

def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--input", type=int, nargs="?", 
        help="Enter a number to perform palindrome check.")
    
    return parser.parse_args(argv)

if __name__ == "__main__":
    main(parse_arguments(sys.argv[1:]))