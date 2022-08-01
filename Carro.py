"""Crea una clase Carro que prenda direccionales dependiendo el giro, las luces, los faros antinieblas,
encender A/C, reproducir musica y prender y apagar el auto"""

class Carro():
    def encender_auto (self, opcion):
        self.opcion = opcion
        if self.opcion == "Encendido":
            print("El auto ha sido encendido")
        else:
            print("El auto ha sido apagado")
    
    def aireAcondicionado(self, opcion):
        self.opcion = opcion

        if self.opcion == "Encendido":
            print("El A/C ha sido encendido")
            temperatura = int(input("Ingrese la temperatura del A/C: "))
            print("La temperatura del A/C ha sido puesta en: {}".format(temperatura))
        else:
            print("El A/C ha sido apagado")

    def direccionales(self, giro):
        self.giro = giro.lower()

        if self.giro == "derecha":
            print("Las direccionales han sido encendidas en el lado derecho del auto")
        elif self.giro == "izquierda":
            print("Las direccionales han sido encendidas en el lado izquierdo")
        elif self.giro == "precaucion":
            print("Las direccionales han sido encendidas en el moto intermitente en ambos lados")
        else:
            self.giro("Las direccionales continuan apagadas")

    def luces(self):

        modo = int(input("Seleccione el modo que desea; 1-Apagadas, 2-Bajas, 3-Altas: "))
        if modo ==1:
            print("Las luces están apagadas")
        elif modo==2:
            print("Las luces están en el modo 2")
        elif modo==3:
            print("Las luces están en el modo 3")        

    def faros(self):
        niebla = input("Hay niebla?").lower()
        if niebla == "si":
            print("Los faros antiniebla han sido encendidos")
        else:
            print("Los faros antinieblas están apagados")


carro = Carro()
carro.encender_auto("Encendido")
carro.aireAcondicionado("Encendido")
carro.direccionales("Derecha")
carro.luces()
carro.faros()


