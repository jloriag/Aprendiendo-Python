import random
def llenarMatrizNumerosAleatorios(cant_filas, cant_columnas):
    matriz=[]
    for i in range(cant_filas):
        arreglo=[]
        for j in range(cant_columnas):
            arreglo.append(random.randint(1,100))
        matriz.append(arreglo)
    return matriz  

def imprimeEnFormatoTabla(matriz):
    print("Imprimiendo matriz en formato tabla")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]}", end=" ")
        print() 

def esta_el_valor_en_matriz(valor,matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if(valor==matriz[i][j]):
                print( f"esta en la fila: {i+1} y en la columna: {j+1} ")
                return
    print ("No se encontró el valor")
matriz=llenarMatrizNumerosAleatorios(3,3)
imprimeEnFormatoTabla(matriz)
input_valor_matriz=int(input("Ingrese una valor a buscar en la matriz: "))
esta_el_valor_en_matriz(input_valor_matriz,matriz)
