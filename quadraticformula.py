# This Python program asks the user for a quadratic equation.
# Then it searches the string for expressions A, B, C and D, to get values for a, b and c.

import math
import re

regexA = re.compile(r'([+-])?\s*(\d+)?x\^2')
regexB = re.compile(r'([+-])?\s*(\d+)?x[^^]')
regexC = re.compile(r'^([+-])?\s*(\d+)[\s+-=]')
regexD = re.compile(r'([+-])?\s*[^^](\d+)[\s+-=]')

equation = input('Enter a quadratic equation: ')
a = 0
b = 0
c = 0

try:
    match = regexA.search(equation)
    if match:
        a = match.group(1) if match.group(1) else ''
        a += match.group(2) if match.group(2) else '1'
        a = int(a)

    match = regexB.search(equation)
    if match:
        b = match.group(1) if match.group(1) else ''
        b += match.group(2) if match.group(2) else '1'
        b = int(b)

    match = regexC.search(equation)
    if match:
        c = match.group(1) if match.group(1) else ''
        c += match.group(2) 
        c = int(c)
    else:  
        match = regexD.search(equation)
        c = match.group(1) if match.group(1) else ''
        c += match.group(2) 
        c = int(c)

    print("a = %d" %a)
    print("b = %d" %b)
    print("c = %d" %c)

    if a != 0 and b**2 - 4*a*c >= 0:
        x1 = (-1 * b + math.sqrt(b**2 - 4*a*c))/(2*a)
        x2 = (-1 * b - math.sqrt(b**2 - 4*a*c))/(2*a)
        print("x = {%.2f, %.2f}" %(x1, x2))
except:
    print('Error parsing quadratic equation. Equation must be of the form ax^2 + bx + c = 0, where a, b and c are integers.')