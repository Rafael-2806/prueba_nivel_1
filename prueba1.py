
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        print(f"Clase: Vehículo\nColor: {self.color}\nRuedas: {self.ruedas}")


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        super().__str__()
        print(f"Velocidad: {self.velocidad}\nCilindrada: {self.cilindrada}")


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        super().__str__()
        print(f"Carga: {self.carga}")



# Crear objetos de cada subclase
coche = Coche("Azul", 4, "120 km/h", "2000 cc")
camioneta = Camioneta("Blanco", 4, "100 km/h", "2500 cc", "500 kg")



# Agregar los objetos a una lista
lista_vehiculos = [coche, camioneta]

# Definir la función catalogar
def catalogar(lista):
    for vehiculo in lista:
        vehiculo.__str__()
        print("\n")

# Llamar a la función catalogar para mostrar la información de los vehículos
catalogar(lista_vehiculos)
