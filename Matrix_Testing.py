import random
import MatrixTest as Matrix


def func(i,j):
    return (i ** j - (i ** 2) ) + (-1) ** j
def func_r(i,j):
    return int(random.random() * 2)
def func_i(i,j):
    if(i == j):
        return 1
    else:
        return 0

m = Matrix.Matrix(3,3)
m.generate(func)
#m.print()
#print(Matrix.Matrix_Det(m))
m2 = Matrix.Matrix(3,3)
m2.generate(func_r)
print("m2\n")
print(m2)
#print(Matrix.Matrix_Det(m2))
m3 = m - m2
print("m3\n")
print(m3)
#print(Matrix.Matrix_Det(m3))
mi = Matrix.Matrix(3,3)
#mi.generate(func_i)
#mi.print()
#print(Matrix.Matrix_Det(mi))
m4 = m3 * mi
print("m4\n")
print(m4)
#m4.print()
#print(Matrix.Matrix_Det(m4))
m4 = m4 ** -1.0
print("m4\n")
print(m4)
#m4.print()
#print(Matrix.Matrix_Det(m4))
m5 = Matrix.Matrix(5,5)
m5.generate(func_i)
print("m5\n")
print(m5)
#m5.print()
#print(Matrix.Matrix_Det(m5))
m6 = Matrix.Matrix(2,2)
m6.content = [
    [8, 5],
    [13, 8]
]
#m6.print()
#m7 = Matrix.Matrix_Rec(m4)
#if(isinstance(m7,Matrix.Matrix)):
    #m7.print()
m9 = Matrix.Matrix_Rec(m)
if(isinstance(m9,Matrix.Matrix)):
    m9.print()
m10 = m6 * ~m6
print(m10)