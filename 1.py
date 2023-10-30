
#EJERCICIO PRUEBA DE NIVEL 

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Vehículo - Color: {}, Ruedas: {}".format(self.color, self.ruedas)
#Vehículo es la clase súper 

#La clase Coche hereda de la clase Vehículo.
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "Coche - Color: {}, Ruedas: {}, Velocidad: {} km/h, Cilindrada: {}cc".format(self.color, self.ruedas, self.velocidad, self.cilindrada)

#Camión hereda de la clase Coche
class Camion(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return "Camión - Color: {}, Ruedas: {}, Velocidad: {} km/h, Cilindrada: {}cc, Carga: {} kg".format(self.color, self.ruedas, self.velocidad, self.cilindrada, self.carga)

#Bicicleta hereda de la clase Vehículo
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return "Bicicleta - Color: {}, Ruedas: {}, Tipo: {} ".format(self.color, self.ruedas, self.tipo)

#Motocicleta hereda de la clase Bicicleta 
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "Motocicleta - Color: {}, Ruedas: {}, Tipo: {} , Velocidad: {} km/h, Cilindrada: {}cc".format(self.color, self.ruedas, self.tipo, self.velocidad, self.cilindrada)

#Una vez creadas las clases y subclases realizamos las preguntas propuestas por el profesor:
#Creamos objetos de las subclases: (PREFUNTA 1)
coche = Coche("Negro", 4, 170, 2000)
coche1 = Coche("Azul", 4, 200, 1500)
camion = Camion("Azul", 6, 120, 6000, 10000)
bicicleta = Bicicleta("Rosa", 2, "Urbana")
bicicleta1 = Bicicleta("Dorado", 2, "Deportiva")
motocicleta = Motocicleta("Negra", 2, "Deportiva", 100, 1000)


# Agregamos los objetos a la lista "vehiculos"
vehiculos = [coche, coche1, camion, bicicleta, bicicleta1, motocicleta]

def catalogar(lista, ruedas):
    for i in vehiculos:
        if i.ruedas==ruedas:
            print(i.__class__.__name__, i.__str__())
        else:
            pass
        
print(catalogar(vehiculos,4))