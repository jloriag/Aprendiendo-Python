import juegosazar

for i in range(15):
    print("Tirando el dado iteración numero: ",i+1)
    print("Resultado de la tirada es: ", juegosazar.lanzarDado())
    print("Tirando la moneda iteración numero: ", i+1)
    print("Resultado de la tirada es: ", juegosazar.lanzarMoneda())
    print("Tirando de la ruleta iteración numero:", i+1)
    print("Resultado de la tirada es: ", juegosazar.lanzarRuleta())
    print("------------------------------------------------")