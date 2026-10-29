import datetime

# Lista global para almacenar los productos.
# Cada producto se guarda como un diccionario con las claves 'nombre', 'precio' y 'fecha_compra'.
productos = []

def agregar_producto():
    """
    Solicita los datos de un producto y lo añade a la lista global.
    Estandariza el nombre, valida que el precio sea numérico y asigna 
    la fecha y hora actual de forma automática empleando el módulo datetime.
    
    Retorna:
        dict: El diccionario del producto recién agregado si fue exitoso.
        None: Si ocurrió un error en el ingreso de datos.
    """
    print("\n--- Agregar Nuevo Producto ---")
    nombre = input("Ingresá el nombre del producto: ").strip().capitalize()
    
    if not nombre:
        return None
        
    try:
        precio = float(input(f"Ingresá el precio de '{nombre}': $"))
        if precio < 0:
            return None
            
        # Obtenemos la fecha y hora exacta del sistema en este instante
        ahora = datetime.datetime.now()
        # Le damos un formato legible (Ejemplo: 27/10/2026 16:30)
        fecha_formateada = ahora.strftime("%d/%m/%Y %H:%M")
        
        nuevo_producto = {
            "nombre": nombre,
            "precio": precio,
            "fecha_compra": fecha_formateada  # Guardamos la marca de tiempo requerida
        }
        
        productos.append(nuevo_producto)
        return nuevo_producto
    except ValueError:
        return None

def consultar_productos():
    """
    Obtiene la lista actual de productos disponibles en el sistema.
    Retorna:
        list: La lista global de productos (puede estar vacía).
    """
    return productos

def eliminar_producto():
    """
    Busca un producto por su nombre en la lista global y lo remueve.
    Retorna:
        str: El nombre del producto eliminado si se encontró con éxito.
        None: Si el producto no existía o si la lista estaba vacía.
    """
    print("\n--- Eliminar Producto ---")
    if not productos:
        return None
        
    nombre_buscar = input("Ingresá el nombre del producto que querés eliminar: ").strip().capitalize()
    
    for prod in productos:
        if prod["nombre"] == nombre_buscar:
            productos.remove(prod)
            return nombre_buscar
            
    return None

def mostrar_menu():
    """
    Muestra el menú interactivo en la consola y gestiona el flujo del programa.
    Muestra la información de los productos incluyendo su fecha de registro.
    """
    while True:
        print("=== MENÚ DE GESTIÓN DE PRODUCTOS ===")
        print("1. Agregar un producto")
        print("2. Consultar la lista de productos")
        print("3. Eliminar un producto")
        print("4. Salir del programa")
        
        opcion = input("Elegí una opción (1-4): ").strip()
        
        if opcion == "1":
            producto_creado = agregar_producto()
            if producto_creado:
                print(f"¡Producto '{producto_creado['nombre']}' (${producto_creado['precio']:.2f}) agregado con éxito!")
                print(f"Registrado el: {producto_creado['fecha_compra']}\n")
            else:
                print("Error: Datos no válidos. No se pudo registrar el producto.\n")
                
        elif opcion == "2":
            lista_actual = consultar_productos()
            print("\n--- Lista de Productos Disponibles ---")
            if lista_actual:
                for i, prod in enumerate(lista_actual, start=1):
                    # Mostramos el nombre, precio y la fecha/hora recuperada del diccionario
                    print(f"{i}. Producto: {prod['nombre']} | Precio: ${prod['precio']:.2f} | Registrado: {prod['fecha_compra']}")
            else:
                print("La lista de productos está vacía.")
            print()
            
        elif opcion == "3":
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