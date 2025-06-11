input_numero=int(input("Ingrese el numero: "))
input_accion=input("Ingrese la accion: ")
input_cuantos_contar=int(input("Ingrese la cantidad que quieres contar: "))
if(input_accion=="adelante"):
    for i in range(1,input_cuantos_contar):
        print(i+input_numero)
else: 
    if(input_accion=="atras"):
        for i in range(1,input_cuantos_contar):
            print(input_numero-i)