import random

def matriz_3_x_3_nun_aleatorios():
    matriz=[]
    for i in range(3):
        arreglo=[]
        for j in range (3):
            arreglo.append(random.randint(1,10))
        matriz.append(arreglo)
    return matriz

def imprime_matriz_formato_tabla(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()

def calcula_determinante(matriz):
    a=matriz[0][0]
    b=matriz[0][1]
    c=matriz[0][2]
    d=matriz[1][0]
    e=matriz[1][1]
    f=matriz[1][2]
    g=matriz[2][0]
    h=matriz[2][1]
    i=matriz[2][2]
    return det(a,b,c,d,e,f,g,h,i)

def det(a,b,c,d,e,f,g,h,i):
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)



# Nuestras pruebas
matriz=matriz_3_x_3_nun_aleatorios()
imprime_matriz_formato_tabla(matriz)

print(calcula_determinante(matriz))