input_numero=int(input("Ingrese el numero: "))
input_accion=input("Ingrese la accion: ")
if(input_accion=="adelante"):
    for i in range(1,11):
        print(i+input_numero)
else: 
    if(input_accion=="atras"):
        for i in range(1,11):
            print(input_numero-i)