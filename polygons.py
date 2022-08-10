# This module has a function for approximating pi, and a function that prints a table of approximations for pi.

import math
import sys

# This function approximates pi by calculating the area of an n-sided regular polygon inscribed in a unit circle. 
# The larger the value of n, the better the approximation.
#
# The limit of the area of an n-sided regular polygon inscribed in a unit circle, as n approaches infinity, is pi.
#
# In limit notation, lim n->inf n*sin(pi/n)*cos(pi/n) = pi 

def approximate_pi(n):
    A = n * math.sin(math.pi/n) * math.cos(math.pi/n)
    return A

# This function prints a table of approximations for pi.
#
# Notes on print formatting syntax:
#
# 1. The expression %-10d tells the print function to left justify the integer by ten spaces
# 2. The expression %.20f tells the print function to display 20 decimal places of the float
#
# This formatting syntax was adopted by Python from the C programming language.

def print_table(begin, end, step):
    print("Table of approximations for pi")
    print("=================================")
    print("%-10s %s" %("n", "A"))
    print("=================================")
    for n in range(begin, end+1, step):
        print("%-10d %.20f" %(n, approximate_pi(n)))

def main():
    if len(sys.argv) != 2:
        print("Usage: python %s [integer n such that 3 <= n <= 10^5]" %sys.argv[0])
        print("Example: python polygons.py 100")
        return

    try:
        n = int(sys.argv[1])

        if n < 3 or n > 10000:
            print("The argument must be an integer in the range [3, 10^5]")
            return

        print_table(3, n, 1)
    except:
        print("The argument must be an integer in the range [3, 10^5]")
        return

# This code will only run if it's the top-level environment. If the file is imported, the code will not be run.
# https://docs.python.org/3/library/__main__.html
#
# The special variable __name__ is set to "__main__" when the file is the top-level environment (the main entry point of the application).
# Otherwise, the special variable __name__ is set to the name of the module.

if __name__ == "__main__":
    main()
