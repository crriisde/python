print (" ")
print("Cristian David Salas De La O 3-W")
print (" ")
# Solicitar al usuario una palabra
palabra = input("Introduce una palabra: ").strip().lower()

# Verificar si la palabra es un palíndromo
if palabra == palabra[::-1]:
    print(f"'{palabra}' es un palíndromo.")
else:
    print(f"'{palabra}' no es un palíndromo.")