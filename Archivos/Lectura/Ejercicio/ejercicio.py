import os
os.chdir("C:\\Users\\jlori\\Documents\\Coding\\Python\\Archivos\\Lectura\\Ejercicio")
f=open("prueba.txt","r")
linea=f.readline()
while linea:
    print(linea)
    linea=f.readline()
f.close()