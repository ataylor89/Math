# This program approximates pi by calculating the area of an n-sided regular polygon inscribed in a unit circle
# The larger the value of n, the better the approximation
import math

# Returns the area of an n-sided regular polygon inscribed in a unit circle as an approximation of pi
def approximate_pi(n):
    A = n * math.sin(math.pi/n) * math.cos(math.pi/n)
    return A

# Prints a table of areas for n-sided regular polygons inscribed in a unit circle
def table(begin, end, step):
    for n in range(begin, end, step):
        # The expression %-10d tells the print function to left-justify the integer by ten spaces
        # The expression %.20f tells the print function to display 20 decimal places of the float
        # This formatting syntax was adopted by Python from the C programming language
        print("%-10d %.20f" %(n, approximate_pi(n)))

# Prints a table of areas for n-sided regular polygons inscribed in a unit circle
# The limit of the area of an n-sided regular polygon as n approaches infinity is pi
# In limit notation, lim n->inf n*sin(pi/n)*cos(pi/n) = pi 
def main():
    print("Area of a regular n-sided polygon inscribed in a unit circle (approximation of pi)")
    print("==================================================================================")
    print("%-10s %s" %("n", "A"))
    print("==================================================================================")
    table(3, 20, 1)
    table(20, 100, 10)
    table(100, 1000, 100)
    table(1000, 10000, 1000)
    table(10000, 100000, 10000)

# This code will only run if it's the top-level environment.
# https://docs.python.org/3/library/__main__.html
# If the file is imported, the code will not be run.
# The special variable __name__ is set to "__main__" when the file is the top-level environment (the main entry point to the application).
# Otherwise, the special variable __name__ is set to the module name.
if __name__ == "__main__":
    main()