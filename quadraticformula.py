import math
import re

regexA = re.compile(r'([+-])?\s*(\d+)?x\^2')
regexB = re.compile(r'([+-])?\s*(\d+)?x[^^]')
regexC = re.compile(r'([+-])?\s*[^^](\d+)[\s+-=]')

equation = input('Enter a quadratic equation: ')
a = 0
b = 0
c = 0

m = regexA.search(equation)
if m:
    a = m.group(1) if m.group(1) else ''
    a += m.group(2) if m.group(2) else '1'
    a = int(a)

m = regexB.search(equation)
if m:
    b = m.group(1) if m.group(1) else ''
    b += m.group(2) if m.group(2) else '1'
    b = int(b)

m = regexC.search(equation)
if m:
    c = m.group(1) if m.group(1) else ''
    c += m.group(2) 
    c = int(c)

print("a = %d" %a)
print("b = %d" %b)
print("c = %d" %c)

if a != 0 and b**2 - 4*a*c >= 0:
    x1 = (-1 * b + math.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-1 * b - math.sqrt(b**2 - 4*a*c))/(2*a)
    print("x = {%f, %f}" %(x1, x2))

# matcher = re.compile(r'(([+-])?(\d+)x\^2)?\s*(([+-])\s*(\d+)x)?\s*(([+-])\s*(\d+))?\s*=\s*0')
# equation = input('Enter a quadratic equation: ')
# m = matcher.match(equation)

# print("Matches: %d" %len(m.groups()))

# a = 0
# if m.group(1):
#     a = m.group(2) if m.group(2) else ''
#     a += m.group(3) if m.group(3) else '1'
#     a = int(a)

# b = 0
# if m.group(4):
#     b = m.group(5) if m.group(5) else ''
#     b += m.group(6) if m.group(6) else '1'
#     b = int(b)

# c = 0
# if m.group(7):
#     c = m.group(8) if m.group(8) else ''
#     c += m.group(9) if m.group(9) else '1'
#     c = int(c)

# print("a = %d" %a)
# print("b = %d" %b)
# print("c = %d" %c)

# if a != 0:
#     x1 = (-1 * b + math.sqrt(b**2 - 4*a*c))/(2*a)
#     x2 = (-1 * b - math.sqrt(b**2 - 4*a*c))/(2*a)
#     print("x = {%f, %f}" %(x1, x2))
# else:
#     print("Cannot use the quadratic formula because a = 0")
