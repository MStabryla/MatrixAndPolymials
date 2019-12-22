import copy

class Polymial:
    def __init__(self):
        self.monomials = []
        self.operations = []

    def __str__(self):
        if len(self.operations) < ( len(self.monomials) - 1):
            return "Wrong polymial"
        else:
            return_str = ""
            for i in range(0,len(self.monomials)):
                if i != len(self.monomials) - 1:
                    return_str += str(self.monomials[i]) + " " + str(self.operations[i]) + " "
                else:
                    return_str += str(self.monomials[i])
            return return_str

    def merge(self):
        symbols_array = []
        temp_monomials = []
        for elem in self.monomials:
            if not any(elem.symbol == s.symbol and elem.power == s.power for s in symbols_array):
                elem_mono = Monomial(1, elem.symbol, elem.power)
                symbols_array.append(elem_mono)
        for elem in symbols_array:
            scalar = 0
            for mono in self.monomials:
                if mono.symbol == elem.symbol and mono.power == elem.power:
                    scalar += mono.scalar
            new_mono = Monomial(scalar, elem.symbol, elem.power)
            temp_monomials.append(new_mono)
        self.monomials = temp_monomials
        self.operations = []
        for j in range(len(self.monomials) - 1):
            self.operations.append('+')

    def __add__(self, other):
        new_polymial = copy.deepcopy(self)
        if isinstance(other, Polymial):
            for i in range(0, len(other.monomials)):
                new_polymial.monomials.append(other.monomials[i])
                new_polymial.operations.append('+')
            for i in range(0, len(other.operations)):
                new_polymial.operations.append(other.operations[i])
        elif isinstance(other, Monomial):
            new_polymial.operations.append('+')
            new_polymial.monomials.append(other)
        elif isinstance(other, float) or isinstance(other, int):
            other_mon = Monomial(other, "", 1)
            new_polymial.operations.append('+')
            new_polymial.monomials.append(other_mon)
        new_polymial.merge()
        new_polymial.sort()
        return new_polymial

    def __sub__(self, other):
        new_polymial = copy.deepcopy(self)
        if isinstance(other, Polymial):
            for i in range(0, len(other.monomials)):
                other.monomials[i].scalar *= -1
                new_polymial.monomials.append(other.monomials[i])
                new_polymial.operations.append('+')
            for i in range(0, len(other.operations)):
                new_polymial.operations.append(other.operations[i])
        elif isinstance(other, Monomial):
            new_polymial.operations.append('+')
            other.scalar *= -1
            new_polymial.monomials.append(other)
        new_polymial.merge()
        new_polymial.sort()
        return new_polymial

    def sort(self):
        for i in range(self.monomials.__len__()-1,0,-1):
            for j in range(i):
                if self.monomials[j].power < self.monomials[j+1].power:
                    temp_mon = self.monomials[j]
                    self.monomials[j] = self.monomials[j+1]
                    self.monomials[j+1] = temp_mon
    
    def getVariableSymbol(self):
        symbol = ""
        for mon in self.monomials:
            if mon.symbol != "":
                if symbol == "":
                    symbol = mon.symbol
                elif symbol != mon.symbol:
                    print("Error: Polymial have multiple variables")
                    return ""
        return symbol     

    def degree(self):
        _degree = 0
        for mon in self.monomials:
            if mon.symbol != "" and mon.power > _degree:
                _degree = mon.power
        return _degree

    def countOfVariables(self):
        _variables = []
        for mon in self.monomials:
            if mon.symbol != "" and not _variables.__contains__(mon.symbol):
                _variables.append(mon.symbol)
        return _variables.__len__()


class Monomial:
    def __init__(self, scalar, symbol, power):
        self.scalar = scalar
        self.symbol = symbol
        self.power = power
        self.symbol_value = None

    def __str__(self):
        if self.scalar == 0:
            return ""
        power_str = ""
        returned_str = ""
        if self.power != 1:
            power_str = "^(" + str(self.power) + ")"
        if self.scalar != 1:
            returned_str += str(self.scalar)
        returned_str += self.symbol + power_str
        return returned_str

    def __add__(self, other):
        returned_value = None
        if isinstance(other, Monomial):
            if other.symbol == self.symbol and other.power == self.power:
                returned_value = Monomial(self.scalar + other.scalar, self.symbol, self.power)
            else:
                returned_value = Polymial()
                returned_value.monomials.append(self)
                returned_value.monomials.append(other)
                returned_value.operations.append('+')
        elif isinstance(other, float) or isinstance(other, int):
            if self.symbol == "":
                returned_value = self.scalar + other
            else:
                returned_value = Polymial()
                returned_value.monomials.append(self)
                other_mon = Monomial(other, "",1)
                returned_value.monomials.append(other_mon)
                returned_value.operations.append('+')
        return returned_value

    def __sub__(self, other):
        returned_value = None
        if isinstance(other, Monomial):
            if other.symbol == self.symbol and other.power == self.power:
                returned_value = Monomial(self.scalar + -1 * other.scalar, self.symbol)
            else:
                returned_value = Polymial()
                returned_value.monomials.append(self)
                other.scalar *= -1
                returned_value.monomials.append(other)
                returned_value.operations.append('+')
        elif isinstance(other, float) or isinstance(other, int):
            if self.symbol == "":
                returned_value = self.scalar - other
            else:
                returned_value = Polymial()
                returned_value.monomials.append(self)
                other_mon = Monomial(-1 * other, "",1)
                returned_value.monomials.append(other_mon)
                returned_value.operations.append('+')
        return returned_value

    def __mul__(self, other):
        returned_value = None
        if isinstance(other, Monomial):
            if other.symbol == self.symbol:
                returned_value = Monomial(self.scalar * other.scalar, self.symbol, self.power + other.power)
            else:
                returned_value = Polymial()
        elif isinstance(other, float) or isinstance(other, int):
            if self.symbol == "":
                returned_value = self.scalar * other
            else:
                returned_value = Polymial()
                returned_value.monomials.append(self)
                other_mon = Monomial(other, "")
                returned_value.monomials.append(other_mon)
                returned_value.operations.append('*')
        return returned_value

    def __truediv__(self, other):
        returned_value = None
        if isinstance(other, Monomial):
            if other.symbol == self.symbol:
                returned_value = Monomial(self.scalar / other.scalar, self.symbol, self.power - other.power)
            else:
                returned_value = Polymial()
        elif isinstance(other, float) or isinstance(other, int):
            if self.symbol == "":
                returned_value = self.scalar / other
            else:
                returned_value = Polymial()
                returned_value.monomials.append(self)
                other_mon = Monomial(other, "",1)
                returned_value.monomials.append(other_mon)
                returned_value.operations.append('/')
        return returned_value


class ComplexMonomial:
    def __init__(self, scalar, symbols):
        self.scalar = scalar
        if isinstance(symbols, list):
            self.symbols = symbols
        elif isinstance(symbols, Monomial):
            self.symbols = []
            self.symbols.append(symbols)
        self.symbol_value = None

    def __add__(self, other):
        returned_value = None
        if isinstance(other, Monomial):
            if len(self.symbols) == 1 and other.symbol == self.symbols[0].symbol and other.power == self.symbols[0].power:
                returned_value = Monomial(self.scalar + -1 * other.scalar, self.symbols[0].symbol)
            else:
                returned_value = Polymial()
                returned_value.monomials.append(self)
                other.scalar *= -1
                returned_value.monomials.append(other)
                returned_value.operations.append('+')
        elif isinstance(other, float) or isinstance(other, int):
            if self.symbol == "":
                returned_value = self.scalar - other
            else:
                returned_value = Polymial
                returned_value.monomials.append(self)
                other_mon = Monomial(-1 * other, "")
                returned_value.monomials.append(other_mon)
                returned_value.operations.append('+')
        return returned_value
    def __str__(self):
        returned_string = str(self.scalar)
        for symbol in self.symbols:
            returned_string += str(symbol)
        return returned_string
