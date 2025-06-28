import sys
import argparse

def main(args):
    num_palindrome_check(args.input)

def num_palindrome_check(x):
    print(x)
    
    return

def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--input", type=str, nargs="?", 
        help="Enter a number to perform palindrome check.")
    
    return parser.parse_args(argv)

main(parse_arguments(sys.argv[1:]))