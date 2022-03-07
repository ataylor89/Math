import sys
import numpy
import string

class Equation:
    def __init__(self, s, vars):
        self.coefficients = []
        self.variables = vars
        self.result = 0
        self.parse(s, vars)

    def parse(self, s, vars):
        sign = 1
        last = 0
        coeffs = {var : 0 for var in vars}
        for i in range(len(s)):
            if s[i] == '+':
                substr = s[last:i].strip()
                coeff = substr[:-1]
                var = substr[-1]
                if var in vars:
                    coeffs[var] = sign * int(coeff)
                sign = 1
                last = i+1
            elif s[i] == '-':
                substr = s[last:i].strip()
                coeff = substr[:-1]
                var = substr[-1]
                if var in vars:
                    coeffs[var] = sign * int(coeff)
                sign = -1
                last = i+1
            elif s[i] == '=':
                substr = s[last:i].strip()
                coeff = substr[:-1]
                var = substr[-1]
                if var in vars:
                    coeffs[var] = sign * int(coeff)
                substr = s[i+1:].strip()
                self.result = int(substr)
                break
        for k, v in sorted(coeffs.items()):
            self.coefficients.append(v)

class System:
    def __init__(self, s):
        self.coefficients = []
        self.variables = []
        self.results = []
        self.parse(s)

    def parse(self, s):
        try: 
            for i in range(len(s)):
                if s[i] in (string.ascii_lowercase + string.ascii_uppercase) and s[i] not in self.variables:
                    self.variables.append(s[i])
            self.variables.sort()
            lines = s.split("\n")
            lines = list(filter(None, lines))
            for line in lines:
                equation = Equation(line, self.variables)
                self.coefficients.append(equation.coefficients)
                self.results.append(equation.result)
        except Exception as err:
            print("Error parsing equations")

def solve(coefficients, variables, result):
    coeff_inv = numpy.linalg.inv(coefficients)
    return numpy.matmul(result, coeff_inv)

def main():
    if len(sys.argv) < 2:
        print("Usage: python %s <filename>" %sys.argv[0])
    filename = sys.argv[1]
    with open(filename) as file:
        s = file.read().strip()
        print("File")
        print(s)
        system = System(s)
        print("Coefficients matrix")
        print(system.coefficients)
        print("Variables matrix")
        print(system.variables)
        print("Results matrix")
        print(system.results)
        solution = solve(system.coefficients, system.variables, system.results)
        print("Solution")
        print(solution)

if __name__ == "__main__":
    main()
