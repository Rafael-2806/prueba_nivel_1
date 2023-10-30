
#Implementar un método de ruedas (get ruedas)
#Hacemos la función catalogar (PREGUNTA 2), e implementamos el método get ruedas 
def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        vehiculos_filtrados = [vehiculo for vehiculo in vehiculos if vehiculo.ruedas == ruedas]
        print("Se han encontrado {} vehículos con {} ruedas:".format(len(vehiculos_filtrados), ruedas))
        for vehiculo in vehiculos_filtrados:
            print("{} - {}".format(vehiculo.__class__.__name__, vehiculo))
    else:
        print("Catálogo de vehículos:")
        for vehiculo in vehiculos:
            print("{} - {}".format(vehiculo.__class__.__name__, vehiculo))
print(camion.__str__())
catalogar(vehiculos, ruedas = 2)