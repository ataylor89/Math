def dotproduct(a, b):
    if len(a) == len(b):
        sum = 0
        for i in range(len(a)):
            sum += a[i] * b[i] 
        return sum
    return None

def dim(A):
    if not A or len(A) == 0:
        return (0, 0)
    if isinstance(A[0], list):
        return (len(A), len(A[0]))
    return (1, len(A))

def nrows(A):
    return dim(A)[0]

def ncols(A):
    return dim(A)[1]

def getcol(A, i):
    if not A or len(A) == 0:
        return None
    elif isinstance(A[0], list):
        col = []
        for row in range(len(A)):
            col.append(A[row][i])
        return col
    return A[i]


def zeromatrix(m, n):
    return [[0 for _n in range(n)] for _m in range(m)]

def mul(A, B):
    nrowsA, ncolsA = nrows(A), ncols(A)
    nrowsB, ncolsB = nrows(B), ncols(B)

    if nrowsA < 1 or nrowsB < 1:
        return None

    elif nrowsA == 1 and nrowsB == 1:
        return dotproduct(A, B)

    elif nrowsA == 1 and nrows(B) > 1:
        result = []
        for col in range(ncolsB):
            b = getcol(B, col)
            Ab = dotproduct(A, b)
            result.append(Ab)
        return result
    
    elif nrowsA > 1 and nrowsB == 1:
        result = []
        for row in range(nrowsA):
            a = A[row]
            aB = dotproduct(a, B)
            result.append(aB)
        return result

    else:
        result = zeromatrix(nrowsA, ncolsB)
        for row in range(nrowsA):
            a = A[row]
            for col in range(ncolsB):
                b = getcol(B, col)
                ab = dotproduct(a, b)
                result[row][col] = ab
        return result

def issquare(A):
    dimA = dim(A)
    return dimA[0] == dimA[1] and dimA[0] > 1

def det(A):
    if A is None or len(A) < 2:
        return None
    if len(A) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    else:
        dim = len(A)
        D = 0
        for i in range(0, dim):
            coeff = A[0][i] * (-1)**i
            submatrix = []
            for row in range(1, dim):
                submatrix.append([])
                for col in range(0, dim):
                    if col != i:
                        submatrix[row-1].append(A[row][col])  
            # print("Coefficient: " + str(coeff))
            # print("Submatrix: " + str(submatrix))
            D += coeff * det(submatrix)
        return D

def main():
    M0 = [[6,1,1], [4,-2,5],[2,8,7]]
    M1 = [[3,0,-1],[2,-5,4],[-3,1,3]]
    M2 = [[2,-3,1],[4,2,-1],[-5,3,-2]]
    M3 = [[5,1,-2],[-1,0,4],[2,-3,3]]
    M4 = [[2,0,-1],[3,5,2],[-4,1,4]]
    M5 = [[2,-1,0],[3,-5,2],[1,4,-2]]
    M6 = [[5,-7,2,2],[0,3,0,-4],[-5,-8,0,3],[0,5,0,-6]]
    M7 = [3, 4, 2]
    M8 = [[13, 9, 7, 15], [8, 7, 4, 6], [6, 4, 0, 3]]
    matrices = [M0, M1, M2, M3, M4, M5, M6, M7, M8]
    for i in range(len(matrices)):
        M = matrices[i]
        print("Matrix %d: %s" %(i, str(M)))
        if issquare(M):
            print("Determinant: %d" %det(M))
    print("M7 x M8 = %s" %str(mul(M7, M8)))

if __name__ == "__main__":
    main()
