# In this program we will approximate pi by calculating the area of an n-sided polygon inscribed in a circle of radius 1
# The larger our value of n, the better the approximation

import math

def approximate_pi(n):
    A = n * math.sin(math.pi/n) * math.cos(math.pi/n)
    print("n: %-10d A: %.20f" %(n, A))
    return A

def main():
    print("===========================================================")
    print("Approximating the area of an n-sided polygon with radius 1.")
    print("The limit of this area as n goes to infinity approaches pi.")
    print("===========================================================")
    for n in range(3, 20, 1):
        approximate_pi(n)
    for n in range(20, 100, 10):
        approximate_pi(n)
    for n in range(1000, 10000, 1000):
        approximate_pi(n)
    for n in range(100000, 1000000, 100000):
        approximate_pi(n)

if __name__ == "__main__":
    main()