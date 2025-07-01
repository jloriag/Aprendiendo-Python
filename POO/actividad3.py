import random

class Carta:
    numero=0
    palo=""

    def __init__(self,numero,palo):
        self.numero=numero
        self.palo=palo

class Baraja:
    cartas=[]

    def __init__(self):
        for i in range(12):
            self.cartas.append(Carta(i,"Corazon"))
            self.cartas.append(Carta(i,"Diamante"))
            self.cartas.append(Carta(i,"Pica"))
            self.cartas.append(Carta(i,"Trebol"))

    def imprimerCartas(self):
        for i in range(len(self.cartas)):
            print(f"La carta en la posición: {i} es de valor: {self.cartas[i].numero}, y tipo: {self.cartas[i].palo}")

    def mezclarBaraja(self):
        for i in range(200): # Se hace 200 veces
            num_1,num_2 = self.numeroAleatorioDistintos()
            self.cartas[num_1],self.cartas[num_2]=self.cartas[num_2],self.cartas[num_1]

    def numeroAleatorioDistintos(self):
        num_1=random.randint(0,47)
        num_2=random.randint(0,47)
        while(num_1==num_2):
            num_2=random.randint(0,47)
        return (num_1,num_2)
    
    def sacarCarta(self):
        num_azar=random.randint(0,len(self.cartas)-1)
        carta=self.cartas.pop(num_azar)
        return carta


baraja=Baraja()
baraja.mezclarBaraja()
baraja.imprimerCartas()

puntos_jugador_1=0
puntos_jugador_2=0
while(puntos_jugador_1<10 or puntos_jugador_2 < 10):
    carta=baraja.sacarCarta()
    print(f"El jugador #1 saca una carta, esta es {carta.numero}, y es de tipo {carta.palo}")
    puntos_jugador_1=puntos_jugador_1+carta.numero
    print(f"Puntos de jugador #1 son {puntos_jugador_1}")
    carta=baraja.sacarCarta()
    print(f"El jugador #2 saca una carta, esta es {carta.numero}, y es de tipo {carta.palo}")
    puntos_jugador_2=puntos_jugador_2+carta.numero
    print(f"Puntos del jugador #2 son {puntos_jugador_2}")
