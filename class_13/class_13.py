import sqlite3

def inicializar_base_de_datos():
    """
    Se conecta a la base de datos 'productos.db'. Si no existe, la crea de forma automática.
    También genera la tabla 'productos' si no se ha creado previamente.
    """
    # Establecemos la conexión con el archivo de la base de datos
    conexion = sqlite3.connect("productos.db")
    
    # Creamos un objeto cursor para poder ejecutar comandos SQL
    cursor = conexion.cursor()
    
    # Definimos la estructura de la tabla según lo solicitado
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL
        )
    ''')
    
    # Confirmamos los cambios en la base de datos y cerramos la conexión
    conexion.commit()
    conexion.close()

def registrar_producto():
    """
    Solicita al usuario el nombre y el precio de un producto,
    aplica las validaciones básicas requeridas y lo guarda en la base de datos.
    """
    print("\n--- Registrar Nuevo Producto ---")
    
    # 1. Solicitar y validar el nombre del producto
    nombre = input("Ingrese el nombre del producto: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return # Regresa al menú principal sin guardar nada

    # 2. Solicitar y validar el precio del producto
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio <= 0:
            print("Error: El precio debe ser un número mayor que cero.")
            return # Regresa al menú si no es mayor a cero
    except ValueError:
        print("Error: Por favor, ingrese un número válido para el precio.")
        return # Regresa al menú si el usuario escribe texto en lugar de un número

    # 3. Guardar el producto validado en la base de datos
    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()
    
    # Usamos marcadores de posición '?' por seguridad contra inyecciones SQL
    cursor.execute('''
        INSERT INTO productos (nombre, precio) 
        VALUES (?, ?)
    ''', (nombre, precio))
    
    conexion.commit()
    conexion.close()
    print(f"¡Producto '{nombre}' registrado exitosamente!")

def mostrar_productos():
    """
    Consulta todos los registros almacenados en la tabla 'productos'
    y los muestra de manera prolija en la pantalla.
    """
    print("\n--- Lista de Productos Almacenados ---")
    
    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()
    
    # Ejecutamos la consulta para traer todos los registros
    cursor.execute("SELECT id, nombre, precio FROM productos")
    # Guardamos todos los resultados encontrados en una lista
    lista_productos = cursor.fetchall()
    
    conexion.close()
    
    # Verificamos si la base de datos está vacía
    if not lista_productos:
        print("No hay productos registrados en la base de datos.")
        return

    # Iteramos la lista e imprimimos cada fila formateada
    for prod in lista_productos:
        # prod[0] es el id, prod[1] es el nombre y prod[2] es el precio
        print(f"ID: {prod[0]} | Nombre: {prod[1]} | Precio: ${prod[2]:.2f}")

def menu_principal():
    """
    Controla el flujo de la aplicación mediante un menú interactivo en la consola.
    """
    # Nos aseguramos de que la base de datos y la tabla existan al iniciar el programa
    inicializar_base_de_datos()
    
    while True:
        print("\n================================")
        print("      GESTIÓN DE PRODUCTOS      ")
        print("================================")
        print("1. Registrar un producto")
        print("2. Mostrar todos los productos")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1-3): ").strip()
        
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elija 1, 2 o 3.")

# El programa comienza a ejecutarse aquí
if __name__ == "__main__":
    menu_principal()
