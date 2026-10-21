# Lista global para almacenar los productos.
# Cada producto será un diccionario con las claves 'nombre' y 'precio'.
productos = []

def agregar_producto():
    """Permite al usuario ingresar un producto con su nombre y precio,
    y lo añade a la lista de productos."""
    print("\n--- Agregar Nuevo Producto ---")
    # Solicitamos el nombre y usamos .capitalize() para estandarizar el formato
    nombre = input("Ingresá el nombre del producto: ").capitalize()
    
    # Manejo de excepciones para asegurar que el usuario ingrese un número válido
    try:
        precio = float(input(f"Ingresá el precio de '{nombre}': $"))
        
        # Creamos un diccionario para el nuevo producto
        nuevo_producto = {
            "nombre": nombre,
            "precio": precio
        }
        
        # Agregamos el diccionario a nuestra lista global de productos
        productos.append(nuevo_producto)
        print(f"¡Producto '{nombre}' agregado con éxito!\n")
        
    except ValueError:
        # Si el usuario no ingresa un número en el precio, muestra un error
        print("Error: El precio ingresado no es válido. Intentalo de nuevo.\n")

def consultar_productos():
    """Muestra en la consola todos los productos almacenados en la lista 
    junto con sus respectivos precios."""
    print("\n--- Lista de Productos Disponibles ---")
    
    # Verificamos si la lista tiene elementos
    if productos:
        # Usamos enumerate para listar los productos con un índice ordenado (empezando en 1)
        for i, prod in enumerate(productos, start=1):
            # Accedemos a los valores del diccionario usando sus claves correspondientes
            print(f"{i}. Producto: {prod['nombre']} | Precio: ${prod['precio']:.2f}")
    else:
        print("La lista de productos está vacía.")
    print()

def eliminar_producto():
    """Busca un producto por su nombre en la lista y lo elimina si existe."""
    print("\n--- Eliminar Producto ---")
    
    if not productos:
        print("La lista está vacía. No hay productos para eliminar.\n")
        return # Salimos de la función de forma anticipada si no hay productos
        
    nombre_buscar = input("Ingresá el nombre del producto que querés eliminar: ").capitalize()
    encontrado = False
    
    # Recorremos la lista para buscar el producto por su nombre
    for prod in productos:
        if prod["nombre"] == nombre_buscar:
            # Si coincide el nombre, removemos el diccionario completo de la lista
            productos.remove(prod)
            print(f"¡El producto '{nombre_buscar}' fue eliminado con éxito!\n")
            encontrado = True
            break # Rompemos el bucle ya que encontramos y eliminamos el elemento
            
    if not encontrado:
        print(f"El producto '{nombre_buscar}' no se encuentra en la lista.\n")

def mostrar_menu():
    """Muestra el menú interactivo en pantalla y gestiona las acciones del usuario."""
    while True:
        print("=== MENÚ DE GESTIÓN DE PRODUCTOS ===")
        print("1. Agregar un producto")
        print("2. Consultar la lista de productos")
        print("3. Eliminar un producto")
        print("4. Salir del programa")
        
        opcion = input("Elegí una opción (1-4): ")
        
        # Evaluamos la opción seleccionada y llamamos a la función correspondiente
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            consultar_productos()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            print("\n¡Gracias por usar el programa de TalentoLab! ¡Chau!")
            break # Rompe el ciclo while para cerrar el programa de forma limpia
        else:
            print("Opción no válida. Por favor, ingresá un número del 1 al 4.\n")

# =====================================================================
# Llamada inicial para ejecutar el programa principal
# =====================================================================
mostrar_menu()
