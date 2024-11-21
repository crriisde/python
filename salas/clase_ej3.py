print (" ")
print("Cristian David Salas De La O 3-W")
print (" ")
from ej3 import CuentaJoven
# Uso de la clase
if __name__ == "__main__":
    # Crear un titular como diccionario con nombre y edad
    titular = {"nombre": "Ana López", "edad": 20}

    # Crear una cuenta joven
    cuenta_joven = CuentaJoven(titular, cantidad=1000, bonificacion=10)

    # Mostrar los datos de la cuenta
    print(cuenta_joven.mostrar())

    # Intentar retirar dinero con titular válido
    cuenta_joven.retirar(200)
    print(cuenta_joven.mostrar())

    # Cambiar la edad del titular a uno inválido y volver a intentar retirar
    cuenta_joven.titular["edad"] = 30
    cuenta_joven.retirar(100)
    print(cuenta_joven.mostrar())