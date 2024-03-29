# This module generates a trigonometric table using the half-angle identities for sine and cosine

import math

table = {
    0: {
        'sine': 0.0, 
        'cosine': 1.0
    },
    30: {
        'sine': 0.5, 
        'cosine': math.sqrt(3)/2
    },
    45: {
        'sine': math.sqrt(2)/2,
        'cosine': math.sqrt(2)/2
    },
    60: {
        'sine': math.sqrt(3)/2,
        'cosine': 0.5
    },
    90: {
        'sine': 1.0,
        'cosine': 0.0
    }
}

def generate(start, depth):
    theta = start
    for i in range(0, depth):
        angle = theta/2
        table[angle] = {}
        table[angle]['sine'] = math.sqrt((1-cosine(theta))/2)
        table[angle]['cosine'] = math.sqrt((1+cosine(theta))/2)
        theta = angle
    
def sine(theta):
    if theta in table:
        return table[theta]['sine']
    return None

def cosine(theta):
    if theta in table:
        return table[theta]['cosine']
    return None

def print_table():
    print("%-10s %-20s %s" %("angle", "sine", "cosine"))
    for angle in sorted(table):
        print("%-10s %-20s %s" %(angle, table[angle]['sine'], table[angle]['cosine']))

def main():
    generate(45, 3)
    generate(30, 3)
    print_table()

if __name__ == "__main__":
    main()