import matrices
import string

example = """x + y + z = 6
2y + 5z = -4
2x + 5y - z = 27"""

class LinearEquation:
    def __init__(self, s, vars):
        self.text = s
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
                var = substr[-1]
                if var in vars:
                    coeffs[var] = sign * 1 if len(substr) <= 1 else sign * int(substr[:-1])
                sign = 1
                last = i+1
            elif s[i] == '-':
                substr = s[last:i].strip()
                var = substr[-1]
                if var in vars:
                    coeffs[var] = sign * 1 if len(substr) <= 1 else sign * int(substr[:-1])
                sign = -1
                last = i+1
            elif s[i] == '=':
                substr = s[last:i].strip()
                var = substr[-1]
                if var in vars:
                    coeffs[var] = sign * 1 if len(substr) <= 1 else sign * int(substr[:-1])
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
                equation = LinearEquation(line, self.variables)
                self.coefficients.append(equation.coefficients)
                self.results.append(equation.result)
        except Exception as err:
            print("Error parsing equations: " + str(err))

    def solve(self):
        if matrices.hasinverse(self.coefficients):
            coeff_inv = matrices.inv(self.coefficients)
            return matrices.mul(coeff_inv, self.results)
        return None

def main():
    system = System(example)
    print("System of linear equations:")
    print(example)
    print("Coefficients matrix")
    print(system.coefficients)
    print("Variables matrix")
    print(system.variables)
    print("Results matrix")
    print(system.results)
    solution = system.solve()
    matrices.printm("Solution: ", solution)

if __name__ == "__main__":
    main()
