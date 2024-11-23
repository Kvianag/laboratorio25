# Imprimir mensaje en consola
print("¡Bienvenido al programa de práctica de Python!")

# Declarar variables de diferentes tipos
numero_entero = 10
numero_decimal = 3.14
texto = "Python"

# Realizar operaciones matemáticas
suma = numero_entero + 5
multiplicacion = numero_decimal * 2
division = numero_entero / 2

# Mostrar resultados de operaciones
print(f"\nOperaciones matemáticas:")
print(f"Suma: {numero_entero} + 5 = {suma}")
print(f"Multiplicación: {numero_decimal} × 2 = {multiplicacion}")
print(f"División: {numero_entero} ÷ 2 = {division}")

# Concatenación de cadenas
lenguaje = "Python"
version = "3"
mensaje = lenguaje + " " + version
print(f"\nConcatenación de cadenas: {mensaje}")

# Uso de input()
nombre = input("\nPor favor, ingresa tu nombre: ")
print(f"¡Hola {nombre}! Gracias por usar este programa.")
