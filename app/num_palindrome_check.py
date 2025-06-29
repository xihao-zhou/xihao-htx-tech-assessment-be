import sys
import argparse
import math

"""Main function to run file independtently"""
def main(args):
    try:
        print(num_palindrome_check(args.input))
    except Exception as e:
        print(f"You have entered an invalid number. {e}")

"""
Funtion to perform palindrome check given input number x
Step 1: Convert input to int (try catch block acts as type validation and will raise expection if conversion cannot be performed)
Step 2: Valid number length between between -2^31 and (2^31 - 1)
Step 3: Perform palindrome check
Return True if input is palindrome else return False
"""
def num_palindrome_check(x):
    if type(x) != int:
        raise TypeError("Ensure that input is an integer.")
    if (-2**31 > x or x > (2**31)-1):
        raise ValueError("Ensure that input length is is between -2^31 and (2^31 - 1).")
    else:
        """
        Check if number is negative, negative number will always be non-palindrome
        Check if number is single digit (0 to 9), single digit number number will always be palindrome
        """
        if x < 0:
            return False
        elif x >= 0 and x < 10:
            return True
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
                    return False
    
    return True

def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--input", type=int, nargs="?", 
        help="Enter a number to perform palindrome check.")
    
    return parser.parse_args(argv)

if __name__ == "__main__":
    main(parse_arguments(sys.argv[1:]))