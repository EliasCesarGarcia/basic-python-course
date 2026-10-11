# 1. Creamos una lista vacía para almacenar los nombres de los clientes
clientes = []

print("=== Registro de Clientes de TalentoLab ===")
print("Ingresá los nombres uno a uno. Escribí 'fin' para terminar la carga.\n")

# Bucle principal para solicitar los datos continuamente
while True:
    # Solicitamos el nombre al usuario eliminando espacios en blanco innecesarios al inicio y final
    nombre = input("Ingresá el nombre del cliente: ").strip()

    # Evaluamos si la persona desea finalizar la carga de datos
    if nombre.lower() == "fin":
        break

    # Requisito 1: Validamos que el nombre ingresado no esté vacío
    if nombre == "":
        print("⚠️ Advertencia: El nombre no puede estar vacío. Por favor, intentá de nuevo.\n")
    else:
        # Requisito 2: Guardamos el nombre válido en la lista usando .append()
        clientes.append(nombre)
        print(f"✓ '{nombre}' ha sido agregado correctamente.\n")

# Requisito 4: Una vez finalizada la carga, ordenamos la lista alfabéticamente
clientes.sort()

# Mostramos los resultados finales mediante un bucle for
print("\n" + "=" * 40)
print("LISTA DE CLIENTES ORDENADA ALFABÉTICAMENTE:")
print("=" * 40)

if clientes:
    for i, cliente in enumerate(clientes, start=1):
        print(f"{i}. {cliente}")
else:
    print("No se ingresaron clientes en la lista.")

# Normalmente, un bucle for cliente in clientes: solo te da el nombre de cada cliente. 
# La función enumerate() te permite obtener dos valores a la vez en cada iteración:
# El número de posición (índice o contador).
# El elemento en sí (el nombre del cliente).
# start=1: Por defecto, los índices en Python empiezan en 0. 
# Al agregar start=1, le indicas a Python que el contador comience a numerar desde 1 para 
# que sea más legible y natural para el usuario final.