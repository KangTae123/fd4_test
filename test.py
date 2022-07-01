from sympy import Matrix

matrixA = Matrix([[0,3,-6,6,4,-5],[3,-7,8,-5,8,9],[3,-9,12,-9,6,15]])
print(matrixA)

matrix_rref = matrixA.rref()
print(matrix_rref)
