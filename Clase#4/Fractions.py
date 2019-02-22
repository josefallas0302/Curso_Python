class Fraction:
    def __init__(self,numerador,denominador):

        self.num = numerador
        self.den = denominador

    def imprimir(self):
        print(str(self.num) + "/" + str(self.den))

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)

F1 = Fraction(8,9)
F2 = Fraction(8,9)
F1.imprimir()
F2.imprimir()
Result = F1+F2
Result.imprimir()