#numero_actual=anterio u preanterior
anterior=1
preanterior=1
numero_actual=0
i=2
print(anterior,end=" ")
print(preanterior,end=" ")
while(i<5):
    numero_actual=anterior+preanterior
    preanterior=anterior
    anterior=numero_actual
    i=i+1
    print(numero_actual, end=" ")