var1=int(input("Ingrese la primera variable: "))
var2=int(input("Ingrese la segunda variable: "))
var3=int(input("Ingrese la tercera variable: "))
arreglo=[]
arreglo.append(var1)
arreglo.append(var2)
arreglo.append(var3)
varmax=0
for dato in arreglo:
    if(varmax<dato):
        varmax=dato
print("La variable mayor es: ",varmax)