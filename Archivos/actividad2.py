archivo_input=open("actividad2.txt", "r")
archivo_output=open("actividad2_duplicado.txt","w")
for linea in archivo_input:
    archivo_output.write(linea)
archivo_input.close()
archivo_output.close()