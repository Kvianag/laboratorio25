# Crear y mostrar lista de estudiantes
estudiantes = ["María", "Carlos", "Ana", "José", "Laura"]
print("Lista de estudiantes:")
for estudiante in estudiantes:
    print(f"- {estudiante}")

# Crear y mostrar diccionario de contactos
contactos = {
    "María": "maria@email.com",
    "Carlos": "carlos@email.com",
    "Ana": "ana@email.com"
}

print("\nLista de contactos:")
for nombre, correo in contactos.items():
    print(f"Nombre: {nombre}, Correo: {correo}")

# Permitir al usuario agregar elementos
print("\n--- Gestión de datos ---")
while True:
    opcion = input("\n¿Qué deseas hacer?\n1. Agregar estudiante\n2. Agregar contacto\n3. Salir\nSelección: ")
    
    if opcion == "1":
        nuevo_estudiante = input("Ingresa el nombre del nuevo estudiante: ")
        estudiantes.append(nuevo_estudiante)
        print("Lista actualizada de estudiantes:")
        for estudiante in estudiantes:
            print(f"- {estudiante}")
    
    elif opcion == "2":
        nombre = input("Ingresa el nombre del contacto: ")
        correo = input("Ingresa el correo del contacto: ")
        contactos[nombre] = correo
        print("\nLista actualizada de contactos:")
        for nombre, correo in contactos.items():
            print(f"Nombre: {nombre}, Correo: {correo}")
    
    elif opcion == "3":
        print("¡Programa terminado!")
        break
    
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")
