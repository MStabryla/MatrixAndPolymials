import Polynomial

class Equation:

    def __init__(self,left,right):
        if isinstance(left,Polynomial.Polymial):
            self.left = left
        if isinstance(right,Polynomial.Polymial):
            self.right = right

    def __str__(self):
        return str(self.left) + " = " + str(self.right)

    def solve(self):
        self.left = self.left - self.right
        print("TESTING self.left " + str(self.left))
        if self.left.countOfVariables() == 1:
            self.right = Polynomial.Polymial()
            self.right += Polynomial.Monomial(0,"",1)
            actEquation = self.left
            if actEquation.degree() == 1:
                _tempCalcResult = 0
                _tempMon = Polynomial.Monomial(0,actEquation.getVariableSymbol(),1)
                print("TESTING symbol " + actEquation.getVariableSymbol())
                for mon in actEquation.monomials:
                    if mon.symbol == "" and mon.scalar != 0:
                        self.left -= mon
                        self.right += mon
                    elif mon.symbol == actEquation.getVariableSymbol():
                        _tempMon = mon
                if _tempMon.scalar != 0:
                    _tempCalcResult /= _tempMon.scalar
                    self.left -= Polynomial.Monomial(_tempMon.scalar-1,_tempMon.symbol,1)
                    print(self.left)
                    self.right += Polynomial.Monomial(_tempCalcResult,"",1)
                    print(self.right)
                else:
                    print("Error: monomial with variable not found")
                    return -1