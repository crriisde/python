class Persona:
    def __init__(self, nombre="", edad=None, dni=""): #esta linea define el init
        self.nombre = nombre
        self.edad = edad if edad is not None else 0
        self.dni = dni

    # Getters y setters
    @property
    def nombre(self): #esta linea define el nombre 
        return self._nombre

    @nombre.setter
    def nombre(self, value): 
        self._nombre = value

    @property
    def edad(self): #esta linea define la edad 
        return self._edad

    @edad.setter
    def edad(self, value):
        if isinstance(value, int) and value >= 0:
            self._edad = value
        else:
            print("Edad inválida")

    @property
    def dni(self): #esta linea define self
        return self._dni

    @dni.setter
    def dni(self, value):
        if len(value) == 9 and value[:-1].isdigit() and value[-1].isalpha():
            self._dni = value
        else:
            print("DNI inválido")

    # Método mostrar()
    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}")

    # Método esMayorDeEdad
    def esMayorDeEdad(self):
        return self.edad >= 18
