import re

class Matrix:
    def __init__ (self,dx,dy):
        self.dx = dx
        self.dy = dy
        self.content = []
        for i in range(dy):
            self.content.append([])
            for j in range(dx):
                self.content[i].append(0)
    def print(self):
        for i in range(self.dy):
            print("[ ", end='')
            for j in range(self.dx):
                print(self.content[i][j], end='')
                if(j < self.dx-1):
                    print("," , end='')
            print(" ]")
        print()
    def print_string(self):
        return_string = ""
        for i in range(self.dy):
            return_string += "[ "
            for j in range(self.dx):
                return_string += str(self.content[i][j])
                if(j < self.dx-1):
                    return_string += ","
            return_string += " ]\n"
        return_string += "\n"
        return return_string
    def generate(self,func):
        for i in range(self.dy):
            for j in range(self.dx):
                self.content[i][j] = func(i,j)
    def __str__(self):
        return self.print_string()
    def __add__(self, other):
        return Matrix_Add(self,other)
    def __sub__(self, other):
        return Matrix_Sub(self,other)
    def __mul__(self, other):
        if(isinstance(other,int) or isinstance(other,float)):
            return Matrix_Sca(self,other)
        elif(isinstance(other,Matrix)):
            return Matrix_Multiply(self,other)
    def __eq__(self, other):
        return Matrix_Equal(self,other)
    def __pow__(self, power, modulo=None):
        return Matrix_Sca(self,power)
    def __invert__(self):
        return Matrix_Tra(self)
def Matrix_Equal(A,B):
    if (not isinstance(A, Matrix)):
        print("Error: A is not a Matrix object")
        return -1;
    elif (not isinstance(B, Matrix)):
        print("Error: B is not a Matrix object")
        return -2;
    else:
        if (A.dx == B.dx and A.dy == B.dy):
            for i in range(A.dy):
                for j in range(A.dx):
                    if(not A.content[i][j] == B.content[i][j]):
                        return False
            return True
        else:
            print("Different dimentions")
            return False
def Matrix_Add(A,B):
    if(not isinstance(A,Matrix)):
        print("Error: A is not a Matrix object")
        return -1;
    elif(not isinstance(B,Matrix)):
        print("Error: B is not a Matrix object")
        return -2;
    else:
        if(A.dx == B.dx and A.dy == B.dy):
            N = Matrix(A.dx,A.dy)
            for i in range(A.dy):
                for j in range(A.dx):
                    N.content[i][j] = A.content[i][j] + B.content[i][j]
            return N;
        else:
            print("Error: A and B have not equal size")
            return -3;
def Matrix_Sub(A,B):
    if(not isinstance(A,Matrix)):
        print("Error: A is not a Matrix object")
        return -1;
    elif(not isinstance(B,Matrix)):
        print("Error: B is not a Matrix object")
        return -2;
    else:
        if(A.dx == B.dx and A.dy == B.dy):
            N = Matrix(A.dx,A.dy)
            for i in range(A.dy):
                for j in range(A.dx):

                    N.content[i][j] = A.content[i][j] - B.content[i][j]
            return N;
        else:
            print("Error: A and B have not equal size")
            return -3;
def Matrix_Multiply(A,B):
    if(not isinstance(A,Matrix)):
        print("Error: A is not a Matrix object")
        return -1;
    elif(not isinstance(B,Matrix)):
        print("Error: B is not a Matrix object")
        return -2;
    else:
        if(A.dx == B.dy):
            N = Matrix(B.dx,A.dy)
            for i in range(N.dy):
                for j in range(N.dx):
                    sum = 0
                    for n in range(A.dx):
                        sum += A.content[i][n] * B.content[n][j]
                    N.content[i][j] = sum
            return N;
        else:
            print("Error: A and B have not equal size")
            return -3;
def Matrix_Sca(A,alfa):
    if (not isinstance(A, Matrix)):
        print("Error: A is not a Matrix object")
        return -1
    elif (not type(alfa) is float and not type(alfa) is float):
        print("Error: alfa is not a number")
        return -2;
    else:
        N = Matrix(A.dx, A.dy)
        for i in range(A.dy):
            for j in range(A.dx):
                N.content[i][j] = A.content[i][j] * alfa
        return N
def Matrix_Tra(A):
    if (not isinstance(A, Matrix)):
        print("Error: A is not a Matrix object")
        return -1
    else:
        N = Matrix(A.dy,A.dx)
        for i in range(N.dy):
            for j in range(N.dx):
                N.content[i][j] = A.content[j][i]
        return N
def Matrix_Cut(A,Y,X):
    if (not isinstance(A, Matrix)):
        print("Error: A is not a Matrix object")
        return -1
    elif (not type(X) is int or not type(Y) is int):
        print("Error: X or Y are not a number")
        return -2
    else:
        N = Matrix(A.dx-1,A.dy-1)
        for i in range(N.dy):
            for j in range(N.dx):
                i_add = 0
                j_add = 0
                if(i >= Y):
                    i_add = 1
                if(j >= X):
                    j_add = 1
                N.content[i][j] = A.content[i+i_add][j+j_add]
        return N
def Matrix_Det(A):
    if (not isinstance(A, Matrix)):
        print("Error: A is not a Matrix object")
        return -1
    else:
        if(not A.dx == A.dy):
            print("Error: A is not a square matrix")
            return -2;
        else:
            if(A.dx == 1):
                return A.content[0][0]
            if(A.dx == 2):
                return A.content[0][0] * A.content[1][1] - A.content[1][0] * A.content[0][1]
            elif (A.dx == 3):
                return A.content[0][0] * A.content[1][1] * A.content[2][2] + A.content[1][0] * A.content[2][1] * A.content[0][2] + A.content[2][0] * A.content[0][1] * A.content[1][2] - A.content[0][2] * A.content[1][1] * A.content[2][0] - A.content[1][2] * A.content[2][1] * A.content[0][0] - A.content[2][2] * A.content[0][1] * A.content[1][0]
            else:
                sum = 0
                for i in range(A.dx):
                    sum += A.content[0][i] * (-1 ** i) * Matrix_Det(Matrix_Cut(A,0,i))
                return sum
def Matrix_Rec(A):
    if (not isinstance(A, Matrix)):
        print("Error: A is not a Matrix object")
        return -1
    else:
        if(not A.dx == A.dy):
            print("Error: A is not a square matrix")
            return -2
        elif(Matrix_Det(A) == 0):
            print("Error: A have not an inverse matrix")
            return -3
        else:
            N = Matrix(A.dx,A.dy)
            I = Matrix(A.dx,A.dy)
            def func_i(i,j):
                if(i == j):
                    return 1
                else:
                    return 0
            I.generate(func_i)
            for i in range(N.dy):
                for j in range(N.dx):
                    A_cut_test = Matrix_Cut(A,i,j)
                    A_cut_det_test = Matrix_Det(A_cut_test)
                    N.content[i][j] = ((-1) ** (i+j+2)) * Matrix_Det(Matrix_Cut(A,i,j))
            #N.print()
            N_test = Matrix_Tra(N)
            N = Matrix_Sca(Matrix_Tra(N),1.0/Matrix_Det(A))

            if(Matrix_Equal(Matrix_Multiply(A,N),I)):
                return N
            else:
                print("Error: A * A^-1 != I")
                return -4
def Matrix_WriteToFile(A,file):
    if (not isinstance(A, Matrix)):
        print("Error: A is not a Matrix object")
        return -1
    else:
        wfile = open(file,"at")
        wfile.write(A.print_string())
        wfile.close()
        return 0
def ReadMatrix(matrix_str):
    matrix_x=0
    matrix_y=0
    matrix_content = []
    matrix_text_lines = matrix_str.split("\n")
    for i in matrix_text_lines:
        line = re.search("\[.*\]", i)
        if(line == None):
            break;
        matrix_y += 1;
        line_str = line.string.replace("[", "").replace("]", "")
        cells = line_str.split(",")
        if len(cells) > matrix_x:
            matrix_x = len(cells)
        matrix_next_row = []
        for elem in cells:
            matrix_next_row.append(int(elem))
        matrix_content.append(matrix_next_row)
    for elem in matrix_content:
        if(len(elem) < matrix_x):
            for i in range(len(elem),matrix_x):
                elem.append(0);
    m = Matrix(matrix_x,matrix_y)
    m.content = matrix_content
    return m
def GaussMethod(A):
    if (not isinstance(A, Matrix)):
        print("Error: A is not a Matrix object")
        return -1
    else:
        for i in range(A.dx):
            for j in range(i+1,A.dy):
                if(A.content[j][i] == 0):
                    continue
                scalar = A.content[j][i]/A.content[i][i]
                for x in range(i,A.dx):
                    A.content[j][x] -= A.content[i][x]*scalar
        return MatrixToFloat(A)
def MatrixToFloat(A):
    if (not isinstance(A, Matrix)):
        print("Error: A is not a Matrix object")
        return -1
    else:
        for i in range(A.dy):
            for j in range(A.dx):
                A.content[i][j] = float(A.content[i][j])
    return A
def Sort_Matrix(A):
    if (not isinstance(A, Matrix)):
        print("Error: A is not a Matrix object")
        return -1
    else:
        for i in range(A.dy-1,-1,-1):
            di = A.dy - i
            x = A.dx - di - 1
            for j in range(A.dy-2,-1,-1):
                if(A.content[j+1][x] > A.content[j][x]):
                    A = Rep_Row(A,j+1,j)
    return A
def Rep_Row(A,a,b):
    if (not isinstance(A, Matrix)):
        print("Error: A is not a Matrix object")
        return -1
    elif(not isinstance(a,int) or not isinstance(b,int) ):
        print("Error: a or b are not integers")
        return -2
    else:
        temp_row = A.content[a]
        A.content[a] = A.content[b]
        A.content[b] = temp_row
        return A
