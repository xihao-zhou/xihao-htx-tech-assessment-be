import sys
import argparse

def main(args):
    palindrome_check(args.input)

def palindrome_check(s):
    print(s)
    
    return

# Funtion to parse arguments when file is run independtently
def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--input", type=str, nargs="?", 
        help="Enter a string to perform palindrome check.")
    
    return parser.parse_args(argv)

main(parse_arguments(sys.argv[1:]))