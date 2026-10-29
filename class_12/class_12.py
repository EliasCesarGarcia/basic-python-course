def mostrar_clientes_registrados():
    """
    Función que abre el archivo 'clientes.txt' en modo lectura,
    procesa cada línea y muestra los clientes de forma ordenada.
    """
    try:
        # Abrimos en modo lectura ("r")
        archivo = open("clientes.txt", "r", encoding="utf-8")
        
        print("\n=== Lista de Clientes Registrados ===")
        print(f"{'Nombre':<15} | {'Apellido':<15} | {'Correo':<30}")
        print("-" * 66)
        
        # Leemos línea por línea
        for linea in archivo:
            # Limpiamos saltos de línea y separamos los datos por la coma
            datos = linea.strip().split(",")
            if len(datos) == 3:
                nombre, apellido, correo = datos
                print(f"{nombre:<15} | {apellido:<15} | {correo:<30}")
                
        archivo.close()
        print("-" * 66)
        
    except FileNotFoundError:
        # Si el archivo aún no existe porque no se cargó ningún cliente
        print("\n[AVISO] No se encontraron clientes registrados (el archivo aún no existe).")
    except IOError:
        print("\n[ERROR] No se pudo leer la información del archivo.")


# --- Programa Principal ---

print("=== Sistema de Registro de Clientes ===")

while True:
    try:
        print("\nIngresá los datos del cliente:")
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        correo = input("Correo: ").strip()

        # Validaciones de datos
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if "@" not in correo:
            raise ValueError("El formato del correo electrónico no es válido (debe contener '@').")

        # Guardado de datos (Modo "a" para agregar)
        archivo = open("clientes.txt", "a", encoding="utf-8")
        archivo.write(f"{nombre},{apellido},{correo}\n")
        archivo.close()
        
        print("\nCliente registrado con éxito en clientes.txt")

    except ValueError as error_datos:
        print(f"\n[ERROR] Datos inválidos: {error_datos}")
    except IOError:
        print("\n[ERROR] No se pudo guardar la información.")

    # Preguntar al usuario si desea continuar o salir del bucle
    continuar = input("\n¿Deseás registrar otro cliente? (s/n): ").strip().lower()
    if continuar != 's':
        print("\nFinalizando la carga de datos...")
        break

# Llamamos a la función para mostrar el resultado final acumulado
mostrar_clientes_registrados()
print("Gracias por usar el sistema.")
