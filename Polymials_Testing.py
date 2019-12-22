import Polynomial as Polymonial
import Equation as Equation

mono_1 = Polymonial.Monomial(2, "x", 1)
print(mono_1)
mono_2 = Polymonial.Monomial(3, "x", 1)
print(mono_2)
mono_3 = Polymonial.Monomial(1, "x", 2)
print(mono_3)
mono_4 = mono_1 + mono_2
print(mono_4)
poly_1 = mono_3 + mono_2
print(poly_1)
poly_2 = mono_3 + mono_1
print(poly_2)
poly_3 = poly_1 + poly_2
print(poly_3)
poly_4 = poly_3 - poly_1
print(poly_4)
poly_5 = poly_4 + 5
print(poly_5)
poly_6 = poly_5 + Polymonial.Monomial(1,"x",3)
print(poly_6)

poly_7 = mono_4 + 15
print(poly_7)
poly_8 = mono_1 - 23
print(poly_8)
#eq_1 = Equation.Equation(poly_7,poly_8)
#print(eq_1)
#eq_1.solve()
#print(eq_1)
mono_5 = Polymonial.Monomial(2,"x",1)
mono_6 = Polymonial.Monomial(1,"x",1)
poly_9 = mono_5 / mono_6
print(poly_9)