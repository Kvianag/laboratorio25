# Determinar si un número es par o impar
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")

# Iterar sobre lista de números e imprimir cuadrados
numeros = [1, 2, 3, 4, 5]
print("\nCuadrados de los números:")
for num in numeros:
    cuadrado = num ** 2
    print(f"El cuadrado de {num} es {cuadrado}")

# Bucle while para entrada repetida
print("\nIngresa números positivos. Para terminar, ingresa un número negativo.")
while True:
    entrada = int(input("Ingresa un número: "))
    if entrada < 0:
        print("Has ingresado un número negativo. Programa terminado.")
        break
    print(f"Has ingresado: {entrada}")
