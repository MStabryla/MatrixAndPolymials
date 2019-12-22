import MatrixTest as Matrix
import random

def func_r(i,j):
    return int(random.random() * 2)

m = Matrix.Matrix(3,5)
m.generate(func_r)
print(m)
m2 = m * random.random()
print(m2)
m3 = m2 * ~m
print(m3)