# 1. Definimos la lista de clientes a procesar (incluye un nombre vacío para la prueba)
clientes = ["Ana", "juan", "", "Marta", "cARLOS", "  "]

print("--- PROCESAMIENTO DE LISTA DE CLIENTES ---\n")

# 2. Recorremos la lista usando `range(len(clientes))` para obtener el índice y la posición
for i in range(len(clientes)):
    # .strip() elimina espacios invisibles para validar correctamente cadenas vacías
    nombre_limpio = clientes[i].strip()
    
    # 3. Validamos si el nombre está vacío
    if nombre_limpio == "":
        # Mostramos una alerta si la posición está vacía
        print(f"Cliente {i + 1}: [ALERTA] Nombre no válido")
    else:
        # Parte 2 (Bonus): Aplicamos .capitalize() para formatear correctamente (Ej: "mArla" -> "Marla")
        nombre_formateado = nombre_limpio.capitalize()
        
        # Mostramos el número de cliente (posición i + 1) y el nombre corregido
        print(f"Cliente {i + 1}: {nombre_formateado}")

print("\n--- FIN DEL PROCESAMIENTO ---")