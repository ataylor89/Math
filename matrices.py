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
    elif ncolsA != nrowsB:
        return None
    elif nrowsA == 1 and nrowsB == 1:
        return dotproduct(A, B)
    elif nrowsA == 1 and nrows(B) > 1:
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
    if dim(matrix)[0] > 1:
        matrix = [["{val:.{precision}f}".format(precision=precision, val=val) for val in row] for row in matrix]
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
        printm(f"Matrix {i}:", M)
    printm("M7 x M9 = ", mul(M7, M9))
    printm("M8 x M9 = ", mul(M8, M9))
    invM10 = inv(M10)
    printm("M10: ", M10)
    print("det(M10): ", det(M10))
    printm("Inverse of M10: ", invM10)
    M11 = mul(M10, invM10)
    printm("M10 x invM10: ", M11)
    a = [3,0,2]
    b = [0.2,0.3,-0.3]
    print("[3,0,2] dot [0.2,0.3,-0.3] %f" %dotproduct(a, b))

if __name__ == "__main__":
    main()
