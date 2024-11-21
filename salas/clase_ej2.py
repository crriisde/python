print (" ")
print("Cristian David Salas De La O 3-W")
print (" ")
# Archivo Cuenta.py
from ej2 import Cuenta

# Crear una cuenta
cuenta = Cuenta("Juan Pérez")

# Mostrar datos de la cuenta
print(cuenta.mostrar())

# Ingresar dinero
cuenta.ingresar(500)
print(cuenta.mostrar())

# Retirar dinero
cuenta.retirar(200)
print(cuenta.mostrar())

# Retirar más dinero (quedará en números rojos)
cuenta.retirar(400)
print(cuenta.mostrar())
