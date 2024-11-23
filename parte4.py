import random

def calculadora():
    print("\n=== Calculadora Básica ===")
    while True:
        print("\nOperaciones disponibles:")
        print("1. Suma")
        print("2. Resta") 
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion = input("\nSelecciona una operación (1-5): ")
        
        if opcion == "5":
            print("¡Hasta luego!")
            break
            
        if opcion not in ["1", "2", "3", "4"]:
            print("Opción no válida. Intenta de nuevo.")
            continue
            
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            
            if opcion == "1":
                print(f"Resultado: {num1} + {num2} = {num1 + num2}")
            elif opcion == "2":
                print(f"Resultado: {num1} - {num2} = {num1 - num2}")
            elif opcion == "3":
                print(f"Resultado: {num1} × {num2} = {num1 * num2}")
            elif opcion == "4":
                if num2 == 0:
                    print("Error: No se puede dividir entre cero")
                else:
                    print(f"Resultado: {num1} ÷ {num2} = {num1 / num2}")
        except ValueError:
            print("Error: Por favor ingresa números válidos")

def juego_adivinanza():
    print("\n=== Juego de Adivinanza ===")
    numero_secreto = random.randint(1, 100)
    intentos = 0
    
    print("\nHe pensado en un número entre 1 y 100.")
    
    while True:
        try:
            intentos += 1
            numero = int(input("\nAdivina el número: "))
            
            if numero == numero_secreto:
                print(f"¡Felicitaciones! ¡Has adivinado el número en {intentos} intentos!")
                break
            elif numero < numero_secreto:
                print("El número es mayor. ¡Sigue intentando!")
            else:
                print("El número es menor. ¡Sigue intentando!")
        except ValueError:
            print("Por favor, ingresa un número válido")
            intentos -= 1

# Menú principal
while True:
    print("\n=== Menú Principal ===")
    print("1. Calculadora")
    print("2. Juego de Adivinanza")
    print("3. Salir")
    
    opcion = input("\nSelecciona una opción (1-3): ")
    
    if opcion == "1":
        calculadora()
    elif opcion == "2":
        juego_adivinanza()
    elif opcion == "3":
        print("¡Gracias por usar el programa!")
        break
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")
