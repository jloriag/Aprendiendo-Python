import random
vector_temperaturas=[]
vector_frio_calor=[]
for i in range(30):
    vector_temperaturas.append(random.randint(10,30))
    if(vector_temperaturas[i]<20):
        vector_frio_calor.append("frio")
    else:
        vector_frio_calor.append("calor")
    print("Temperatura en las posición: ",i, vector_temperaturas[i]," Ademas hace: ",vector_frio_calor[i])
