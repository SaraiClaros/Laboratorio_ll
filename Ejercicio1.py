class Perro:
    def __init__(self, nombre, edad, raza, color, peso, propietario):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.color = color
        self.peso = peso
        self.propietario = propietario
        self.estado = 'NO ATENDIDO'
        self.tamano = 'Perro Grande' if self.peso >= 10 else 'Perro Pequeño'

    def registrar(self):
        self.estado = 'ATENDIDO'
        print("-------------------------------------------------------------------------------------")
        print(f"El perro {self.nombre} ha sido registrado como {self.tamano} y ahora está {self.estado}.")

def ingresar_datos_perro():
    print("Ingrese los datos del perro:")
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    raza = input("Raza: ")
    color = input("Color: ")
    peso = float(input("Peso (en kg): "))
    propietario = input("Nombre del propietario: ")
    
    return Perro(nombre, edad, raza, color, peso, propietario)

# Iniciar el proceso de registro
perro = ingresar_datos_perro()
perro.registrar()

# Mostrar la información registrada
print(f"\nInformación del perro registrado:")
print(f"Nombre: {perro.nombre}")
print(f"Edad: {perro.edad}")
print(f"Raza: {perro.raza}")
print(f"Color: {perro.color}")
print(f"Peso: {perro.peso} kg")
print(f"Tamaño: {perro.tamano}")
print(f"Estado: {perro.estado}")
print(f"Propietario: {perro.propietario}")
