# This program approximates pi by calculating the area of an n-sided polygon inscribed in a unit circle
# The larger the value of n, the better the approximation

import math

def approximate_pi(n):
    A = n * math.sin(math.pi/n) * math.cos(math.pi/n)
    # The expression %-10d tells the print function to left-justify the integer by ten spaces
    # The expression %.20f tells the print function to display 20 decimal places of the float
    # This formatting syntax was adopted by Python from the C programming language
    print("n: %-10d A: %.20f" %(n, A))
    return A

def main():
    print("=======================================================================================")
    print("Approximating the area of an n-sided regular polygon inscribed in a unit circle.")
    print("The limit of this area as n goes to infinity approaches pi.")
    print("In limit notation, lim n->inf n*sin(pi/n)*cos(pi/n) = pi")
    print("=======================================================================================")
    for n in range(3, 20, 1):
        approximate_pi(n)
    for n in range(20, 100, 10):
        approximate_pi(n)
    for n in range(1000, 10000, 1000):
        approximate_pi(n)
    for n in range(10000, 100000, 10000):
        approximate_pi(n)
    for n in range(100000, 1000000, 100000):
        approximate_pi(n)

if __name__ == "__main__":
    main()