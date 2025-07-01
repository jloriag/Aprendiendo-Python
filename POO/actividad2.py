import math

class Persona:
    
    altura=0
    peso=0
    imc=0

    def __init__(self,altura,peso):
        self.altura=altura
        self.peso=peso
        self.imc=self.calcular_imc()
    
    def calcular_imc(self):
        return self.peso/ math.pow(self.altura,2)

class Hombre(Persona):
    sexo="masculino"

    def __init__(self,altura,peso):
        super().__init__(altura,peso)


class Mujer(Persona):
    sexo="femenino"

    def __init__(self,altura, peso):
        super().__init__(altura, peso)

Juan=Hombre(1.70,75)
Elena=Mujer(1.60,50)

print(Juan.imc)
print(Elena.imc)