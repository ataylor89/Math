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
    M1 = [[6,1,1], [4,-2,5],[2,8,7]]
    M2 = [[3,0,-1],[2,-5,4],[-3,1,3]]
    M3 = [[2,-3,1],[4,2,-1],[-5,3,-2]]
    M4 = [[5,1,-2],[-1,0,4],[2,-3,3]]
    M5 = [[2,0,-1],[3,5,2],[-4,1,4]]
    M6 = [[2,-1,0],[3,-5,2],[1,4,-2]]
    M7 = [[5,-7,2,2],[0,3,0,-4],[-5,-8,0,3],[0,5,0,-6]]
    matrices = [M1, M2, M3, M4, M5, M6, M7]
    for M in matrices:
        print(M)
        print("Determinant: %d" %det(M))

if __name__ == "__main__":
    main()
