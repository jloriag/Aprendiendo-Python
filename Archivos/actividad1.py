import os
input_numero=input("Ingrese un nuevo numero: ")
string_guardar=""
while(input_numero!="0"):
    string_guardar+=input_numero
    input_numero=input("Ingrese un nuevo numero: ")
    string_guardar+=" "

with open("archivo.txt", "w") as archivo:
    archivo.write(string_guardar)