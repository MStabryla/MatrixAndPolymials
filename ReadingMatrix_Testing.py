import datetime
import re
import MatrixTest as Matrix

test = open("test.txt","rt")
test_text = test.read()
#print(test.name + "\n" + x)
test.close()
#test = open("test.txt","at")
#datact = str(datetime.datetime.now())
#test.write("\nOpened : " + datact)
#test.close()
matrix_ret = Matrix.ReadMatrix(test_text)
#lol = re.match(r"(.*\n)",y.string)
print(matrix_ret.print_string())
sorted_matrix_ret = Matrix.Sort_Matrix(matrix_ret)
print(sorted_matrix_ret)
gauss_matrix = Matrix.GaussMethod(sorted_matrix_ret)
print(gauss_matrix)
chart = "tre"