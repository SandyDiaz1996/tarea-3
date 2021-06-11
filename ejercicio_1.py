class Condicion:
    contador = 0

    def __init__(self, num1=0, num2=0):
        self.numero1 = num1
        self.numero2 = num2
        # numero = num1 + num2
        self.numero3 = num1
    
    def usoIf(self):
        if self.numero1 == self.numero2:
            print("numero1: {}, numero2: {}; Son Iguales.".format(self.numero1, self.numero2))
        elif self.numero1 == self.numero3:
            print("numero1: {}, numero3: {}; Son Iguales.".format(self.numero1, self.numero3))
        else:
            print("No son iguales.")    


# condicion1 = Condicion()
# print(condicion1.numero1)
# print(condicion1.numero2)

condicion2 = Condicion(30, 30)
condicion2.usoIf()
print(condicion2.numero1)
