class Cuenta: # Esta linea genera la clase  
    def __init__(self, titular, cantidad=0.0): #esta linea define init
        if not isinstance(titular, Persona):
            print("El titular debe ser una instancia de la clase Persona")
            return
        self.titular = titular
        self.cantidad = cantidad

    # Getters y setters
    @property
    def titular(self): #esta linea define el titular
        return self._titular

    @titular.setter
    def titular(self, value): #esta linea define el titular 
        if isinstance(value, Persona):
            self._titular = value
        else:
            print("El titular debe ser una instancia de Persona")

    @property
    def cantidad(self): #esta define el titular 
        return self._cantidad

    @cantidad.setter 
    def cantidad(self, value): #esta linea define la cantidad 
        if isinstance(value, (int, float)) and value >= 0:
            self._cantidad = value
        else:
            print("La cantidad debe ser un valor numérico positivo")

    # Método mostrar()
    def mostrar(self): #esta linea define el motrar 
        print(f"Titular: {self.titular.nombre}, Cantidad: {self.cantidad}")

    # Métodos de ingreso y retiro
    def ingresar(self, cantidad): #esta linea define el ingresasr de las cantidades
        if cantidad > 0:
            self.cantidad += cantidad
        else:
            print("La cantidad a ingresar debe ser positiva")

    def retirar(self, cantidad): #esta linea define el retirar 
        if cantidad > 0: 
            self.cantidad -= cantidad
        else:
            print("La cantidad a retirar debe ser positiva")
