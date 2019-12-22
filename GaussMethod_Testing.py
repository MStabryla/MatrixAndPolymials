import MatrixTest as Matrix

def func_g(i,j):
    return i**2 + j + 1
def loadMatrix(text):
    _file = open(text,"rt")
    _file_text = _file.read()
    _file.close()
    return Matrix.ReadMatrix(_file_text)
m = Matrix.Matrix(3,3)
m.generate(func_g)
m.print()
new_m = Matrix.GaussMethod(m)
new_m.print()
mat = loadMatrix("mat.txt")
Matrix.GaussMethod(mat)
mat.print()