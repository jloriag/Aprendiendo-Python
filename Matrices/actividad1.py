matriz_tamano_i=3
matriz_tamano_j=3
matriz=[]

for i in range(matriz_tamano_i):
    for j in range(matriz_tamano_j):
       input_str="Introduzca el elemento fila: "+ str(i)+ " y columna: "+ str(j)+" : "
       input_valor = input(input_str)
       if(j==0):
            vector=[]
            vector.append(input_valor)
       elif(j==matriz_tamano_j-1):
            vector.append(input_valor)
            matriz.append(vector)
       else:
           vector.append(input_valor)
           

for k in range(matriz_tamano_i):
    for l in range(matriz_tamano_j):
        output_str="Imprimieno el elemento en fila: " + str(k) + "y columna: "+str(l)+" : "+matriz[k][l]
        print(output_str)