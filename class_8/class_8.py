# 1. Crear un diccionario vacío llamado 'productos'
# donde la clave será el nombre del producto (string) y el valor será el precio (float/int).
productos = {}

print("--- REGISTRO DE PRODUCTOS Y PRECIOS ---")

# Bucle infinito para permitir el ingreso continuo de datos hasta que el usuario decida finalizar
while True:
    print("\nIngresá los datos del producto (o dejá el nombre vacío y presioná Enter para salir):")
    
    # Solicitamos el nombre del producto
    nombre = input("Nombre del producto: ").strip().capitalize()
    
    # Condición de salida: si el usuario no ingresa nada en el nombre, rompemos el bucle
    if nombre == "":
        print("\nFinalizando el registro de productos...")
        break
    
    # Control de errores para asegurar que el precio ingresado sea un número válido
    try:
        precio = float(input(f"Precio de '{nombre}': $"))
        
        # Validamos que el precio no sea negativo
        if precio < 0:
            print("El precio no puede ser negativo. Inténtalo nuevamente.")
            continue
            
    except ValueError:
        print("Entrada inválida. Debe ingresar un número válido para el precio.")
        continue # Vuelve al inicio del bucle para pedir nuevamente los datos

    # Guardamos o actualizamos la clave (nombre) con su valor (precio) en el diccionario
    productos[nombre] = precio
    print(f"-> ¡'{nombre}' registrado exitosamente!")

    # Mostrar el contenido del diccionario después de cada operación
    print("\n[Estado actual del inventario]:")
    for prod, prec in productos.items():
        print(f" - {prod}: ${prec:.2f}")

# Muestra final al terminar el programa
print("\n=== RESUMEN FINAL DE PRODUCTOS ===")
if productos:
    for prod, prec in productos.items():
        print(f" - {prod}: ${prec:.2f}")
else:
    print("No se registraron productos.")