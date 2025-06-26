import random

input_num_filas_m1=int(input("Ingrese el numero de filas de la matriz #1: "))
input_num_columnas_m1=int(input("Ingrese el numero de columnas de la matriz #1 "))

def llenarMatriz(cant_filas,cant_columnas):
    matriz=[]
    for i in range(cant_filas):
        arreglo=[]
        for j in range(cant_columnas):
            arreglo.append(int(input(f"Ingrese el valor de la fila: {i}, columna {j}: ")))
        matriz.append(arreglo)
    return matriz

def llenarMatrizNumerosAleatorios(cant_filas, cant_columnas):
    matriz=[]
    for i in range(cant_filas):
        arreglo=[]
        for j in range(cant_columnas):
            arreglo.append(random.randint(1,100))
        matriz.append(arreglo)
    return matriz    

def imprimeMatriz(matriz):
    print("Imprimiendo matriz")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"El valor de la fila: {i}, columna {j} es: {matriz[i][j]}")

def imprimeEnFormatoTabla(matriz):
    print("Imprimiendo matriz en formato tabla")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]}", end=" ")
        print()   

def sumaMatrices(matriz_1,matriz_2):
    matriz_resultante=[]
    if(len(matriz_1)==len(matriz_2)):
        for i in range(len(matriz_1)):
            arreglo_Temp=[]
            for j in range(len(matriz_2)):
                arreglo_Temp.append(matriz_1[i][j]+matriz_2[i][j])
            matriz_resultante.append(arreglo_Temp)
    return matriz_resultante

matriz_1=llenarMatrizNumerosAleatorios(input_num_filas_m1,input_num_columnas_m1)
matriz_2=llenarMatrizNumerosAleatorios(input_num_filas_m1,input_num_columnas_m1)

imprimeEnFormatoTabla(sumaMatrices(matriz_1,matriz_2))