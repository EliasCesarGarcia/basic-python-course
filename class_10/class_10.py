# Lista global para almacenar los productos.
# Cada producto se guarda como un diccionario con las claves 'nombre' y 'precio'.
productos = []

def agregar_producto():
    """
    Solicita los datos de un producto y lo añade a la lista global.
    
    Estandariza el nombre del producto usando mayúscula inicial y 
    valida que el precio ingresado sea numérico.
    
    Retorna:
        dict: El diccionario del producto recién agregado si fue exitoso.
        None: Si el precio ingresado no fue válido.
    """
    print("\n--- Agregar Nuevo Producto ---")
    nombre = input("Ingresá el nombre del producto: ").capitalize()
    
    try:
        precio = float(input(f"Ingresá el precio de '{nombre}': $"))
        nuevo_producto = {
            "nombre": nombre,
            "precio": precio
        }
        productos.append(nuevo_producto)
        # Retornamos el objeto creado en lugar de imprimir el éxito aquí dentro
        return nuevo_producto
        
    except ValueError:
        # En caso de error numérico, retornamos None para que el menú lo gestione
        return None

def consultar_productos():
    """
    Obtiene la lista actual de productos disponibles en el sistema.
    
    Retorna:
        list: La lista global de productos (puede estar vacía).
    """
    # Retornamos la estructura de datos directamente para que sea procesada fuera
    return productos

def eliminar_producto():
    """
    Busca un producto por su nombre en la lista global y lo remueve.
    
    Solicita el nombre del producto a eliminar al usuario.
    
    Retorna:
        str: El nombre del producto eliminado si se encontró con éxito.
        None: Si el producto no existía en la lista o si la lista estaba vacía.
    """
    print("\n--- Eliminar Producto ---")
    
    if not productos:
        return None
        
    nombre_buscar = input("Ingresá el nombre del producto que querés eliminar: ").capitalize()
    
    # Buscamos el producto dentro de nuestra colección
    for prod in productos:
        if prod["nombre"] == nombre_buscar:
            productos.remove(prod)
            # Retornamos el nombre confirmado del producto eliminado
            return nombre_buscar
            
    # Si termina el bucle sin retornar, significa que no se encontró el producto
    return None

def mostrar_menu():
    """
    Muestra el menú interactivo en la consola y gestiona el flujo del programa.
    
    Recibe las respuestas de las funciones secundarias a través de 'return' 
    e imprime las confirmaciones y visualizaciones correspondientes al usuario.
    """
    while True:
        print("=== MENÚ DE GESTIÓN DE PRODUCTOS (ENFOQUE RETURN) ===")
        print("1. Agregar un producto")
        print("2. Consultar la lista de productos")
        print("3. Eliminar un producto")
        print("4. Salir del programa")
        
        opcion = input("Elegí una opción (1-4): ")
        
        if opcion == "1":
            # Guardamos el resultado devuelto por la función
            producto_creado = agregar_producto()
            if producto_creado:
                print(f"¡Producto '{producto_creado['nombre']}' con precio ${producto_creado['precio']:.2f} agregado con éxito!\n")
            else:
                print("Error: El precio ingresado no es válido. No se guardó el producto.\n")
                
        elif opcion == "2":
            # Recibimos la lista desde la función consultora
            lista_actual = consultar_productos()
            print("\n--- Lista de Productos Disponibles ---")
            if lista_actual:
                for i, prod in enumerate(lista_actual, start=1):
                    print(f"{i}. Producto: {prod['nombre']} | Precio: ${prod['precio']:.2f}")
            else:
                print("La lista de productos está vacía.")
            print()
            
        elif opcion == "3":
            # Evaluamos la eliminación según el retorno obtenido
            if not productos:
                print("La lista está vacía. No hay productos para eliminar.\n")
            else:
                producto_eliminado = eliminar_producto()
                if producto_eliminado:
                    print(f"¡El producto '{producto_eliminado}' fue eliminado con éxito!\n")
                else:
                    print("El producto no se encuentra en la lista.\n")
                    
        elif opcion == "4":
            print("\n¡Gracias por usar el programa de TalentoLab! ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingresá un número del 1 al 4.\n")

# =====================================================================
# Ejecución inicial del programa principal
# =====================================================================
mostrar_menu()
