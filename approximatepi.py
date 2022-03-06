import math
import sys

def f(x):
    return math.sqrt(1 - x**2)

def approximate_pi(n):
    dx = 1/n
    area = 0
    for i in range(n):
        x = i * dx
        area += f(x) * dx
    return 4 * area

if __name__ == "__main__":
    precision = int(sys.argv[1])
    n = int(sys.argv[2])
    print("Using %d rectangles to approximate Pi..." %n)
    approximation = approximate_pi(n)
    print("Ap: %0.*f" %(precision, approximation))
    print("Pi: %0.*f" %(precision, math.pi))
