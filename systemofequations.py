import sys
import numpy

class ParseTree:

    def __init__(self, s):
        self.coefficients = []
        self.variables = []
        self.result = []
        self.parse(s)

    def parse(self, s):
        try:
            equations = s.split("\n")
            equations = list(filter(None, equations))
            sides = equations[0].split("=")
            terms = sides[0].split(" ")
            terms = list(filter(lambda x : x and x not in ('+', '-'), terms))
            for term in terms:
                self.variables.append(term[-1])
            for equation in equations:
                sides = equation.split("=")
                terms = sides[0].split(" ")
                terms = list(filter(lambda x : x and x not in ('+', '-'), terms))
                coeffs = []
                for term in terms:
                    coeff = float(term[:-1])
                    coeffs.append(coeff)
                self.coefficients.append(coeffs)
                res = float(sides[1].strip())
                self.result.append(res)
        except:
            print("Error parsing equations")

def solve(coefficients, variables, result):
    coeff_inv = numpy.linalg.inv(coefficients)
    return numpy.matmul(result, coeff_inv)

def main():
    if len(sys.argv) < 2:
        print("Usage: python %s <filename>" %sys.argv[0])
    filename = sys.argv[1]
    with open(filename) as file:
        s = file.read()
        pt = ParseTree(s)
        print(pt.coefficients)
        print(pt.variables)
        print(pt.result)
        solution = solve(pt.coefficients, pt.variables, pt.result)
        print(solution)

if __name__ == "__main__":
    main()
