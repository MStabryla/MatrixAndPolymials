import MatrixTest as Matrix

m = Matrix.Matrix(2,2)
m.content = [
    [1, 0],
    [1, 2]
]
m2 = Matrix.Matrix(2,2)
m2.content = [
    [ 0, 2],
    [-1, 0]
]
m3 = Matrix.Matrix(3,2)
m3.content = [
    [1, 0, -1],
    [-1, 2, 0]
]
m4 = Matrix.Matrix_Tra(m)
m4.print()
m5 = m4 - m2
m5.print()
m6 = Matrix.Matrix_Multiply(m5,m3)
m6.print()