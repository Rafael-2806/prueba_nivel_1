class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def mostrar_informacion(self):
        print(f"Clase: {self.__class__.__name__}\nColor: {self.color}\nRuedas: {self.ruedas}")


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Velocidad: {self.velocidad}\nCilindrada: {self.cilindrada}")


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Carga: {self.carga}")


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init(color, ruedas)
        self.tipo = tipo

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Tipo: {self.tipo}")


class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Velocidad: {self.velocidad}\nCilindrada: {self.cilindrada}")


# Crear objetos de cada subclase
vehiculo_generico = Vehiculo("Rojo", 4)
coche = Coche("Azul", 4, "120 km/h", "2000 cc")
camioneta = Camioneta("Blanco", 4, "100 km/h", "2500 cc", "500 kg")
bicicleta = Bicicleta("Verde", 2, "Montaña")
motocicleta = Motocicleta("Negro", 2, "Deportiva", "180 km/h", "1000 cc")

# Agregar los objetos a una lista
lista_vehiculos = [vehiculo_generico, coche, camioneta, bicicleta, motocicleta]

# Definir la función catalogar
def catalogar(lista):
    for vehiculo in lista:
        vehiculo.mostrar_informacion()
        print("\n")

# Llamar a la función catalogar para mostrar la información de los vehículos
catalogar(lista_vehiculos)
