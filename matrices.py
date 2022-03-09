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
        if hasinverse(self.coefficients):
            coeff_inv = inv(self.coefficients)
            return mul(coeff_inv, self.results)
        return None

def dotproduct(a, b):
    if len(a) == len(b):
        sum = 0
        for i in range(len(a)):
            sum += a[i] * b[i]
        return sum
    return None

def dim(A):
    if not A:
        return None
    elif len(A) == 0:
        return (0, 0)
    elif isinstance(A[0], list):
        return (len(A), len(A[0]))
    return (1, len(A))

def nrows(A):
    return dim(A)[0]

def ncols(A):
    return dim(A)[1]

def getcol(A, col):
    return [row[col] for row in A]

def mul(A, B):
    nrowsA, ncolsA = nrows(A), ncols(A)
    nrowsB, ncolsB = nrows(B), ncols(B)
    if nrowsA < 1 or nrowsB < 1:
        return None
    elif nrowsA == 1 and nrowsB == 1:
        return dotproduct(A, B)
    elif nrowsA == 1 and nrowsB > 1:
        return [dotproduct(A, getcol(B, col)) for col in range(ncolsB)]
    elif nrowsA > 1 and nrowsB == 1:
        return [dotproduct(row, B) for row in A]
    else:
        return [[dotproduct(row, getcol(B, col)) for col in range(ncolsB)] for row in A]

def issquare(A):
    dimA = dim(A)
    return dimA[0] == dimA[1]

def det(A):
    if not issquare(A):
        return None
    elif len(A) == 1:
        return A[0]
    elif len(A) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    else:
        dim = len(A)
        D = 0
        for j in range(dim):
            coeff = A[0][j] * (-1)**j
            submatrixj = submatrix(A, 0, j)
            D += coeff * det(submatrixj)
        return D

def hasinverse(A):
    D = det(A)
    return D and D != 0

def submatrix(A, i, j):
    dimA = len(A)
    return [[A[row][col] for col in range(dimA) if col != j] for row in range(dimA) if row != i]

def minors(A):
    dim = len(A)
    return [[det(submatrix(A, row, col)) for col in range(dim)] for row in range(dim)]

def cofactors(A):
    dim = len(A)
    return [[(-1)**(row+col) * A[row][col] for col in range(dim)] for row in range(dim)]

def adjugate(A):
    dim = len(A)
    return [[A[col][row] for col in range(dim)] for row in range(dim)]

def inv(A):
    if hasinverse(A):
        dimA = len(A)
        D = det(A)
        A = minors(A)
        A = cofactors(A)
        A = adjugate(A)
        A = [[A[row][col] * 1/D for col in range(dimA)] for row in range(dimA)]
        return A
    return None

def printm(label, matrix, precision=1):
    if dim(matrix)[0] == 1:
        matrix = ["{val:.{p}f}".format(p=precision, val=val) for val in matrix]
    elif dim(matrix)[0] > 1:
        matrix = [["{val:.{p}f}".format(p=precision, val=val) for val in row] for row in matrix]
    print("%s%s" %(label, str(matrix)))

def main():
    M0 = [[6,1,1], [4,-2,5],[2,8,7]]
    M1 = [[3,0,-1],[2,-5,4],[-3,1,3]]
    M2 = [[2,-3,1],[4,2,-1],[-5,3,-2]]
    M3 = [[5,1,-2],[-1,0,4],[2,-3,3]]
    M4 = [[2,0,-1],[3,5,2],[-4,1,4]]
    M5 = [[2,-1,0],[3,-5,2],[1,4,-2]]
    M6 = [[5,-7,2,2],[0,3,0,-4],[-5,-8,0,3],[0,5,0,-6]]
    M7 = [3, 4, 2]
    M8 = [[3, 4, 2], [4, 5, 3]]
    M9 = [[13, 9, 7, 15], [8, 7, 4, 6], [6, 4, 0, 3]]
    M10 = [[3,0,2],[2,0,-2],[0,1,1]]
    matrices = [M0, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10]
    for i in range(len(matrices)):
        M = matrices[i]
        printm(f"Matrix {i}: ", M)
    printm("M7 x M9 = ", mul(M7, M9))
    printm("M8 x M9 = ", mul(M8, M9))
    invM10 = inv(M10)
    printm("M10: ", M10)
    print("det(M10): %d" %det(M10))
    printm("Inverse of M10: ", invM10)
    printm("M10 x invM10: ", mul(M10, invM10))
    printm("invM10 x M10: ", mul(invM10, M10))
    system = System(example)
    print("System of linear equations:")
    print(example)
    printm("Coefficients matrix: ", system.coefficients)
    print("Variables matrix: ", system.variables)
    print("Results matrix: ", system.results)
    solution = system.solve()
    printm("Solution: ", solution)

if __name__ == "__main__":
    main()
