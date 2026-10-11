# ==============================================================================
# SISTEMA BÁSICO DE GESTIÓN DE PRODUCTOS
# ==============================================================================

# Estructura principal de datos:
# 'productos' es una lista que contendrá sublistas de 3 elementos: [nombre, categoria, precio]
productos = []

# Bucle principal que mantiene el programa en ejecución continua hasta seleccionar 'Salir'
while True:
    # --------------------------------------------------------------------------
    # Menú de opciones principal
    # --------------------------------------------------------------------------
    print("\n" + "=" * 40)
    print("Sistema de gestión básica de productos")
    print("=" * 40)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("=" * 40)

    opcion = input("Seleccione una opción (1-5): ").strip()

    # --------------------------------------------------------------------------
    # OPCIÓN 1: Agregar producto
    # --------------------------------------------------------------------------
    if opcion == "1":
        print("\n--- AGREGAR PRODUCTO ---")

        # Validación del campo Nombre (no vacíos)
        nombre = input("Ingrese el nombre del producto: ").strip()
        while nombre == "":
            print("Error: El nombre del producto no puede estar vacío.")
            nombre = input("Ingrese el nombre del producto: ").strip()

        # Validación del campo Categoría (no vacíos)
        categoria = input("Ingrese la categoría del producto: ").strip()
        while categoria == "":
            print("Error: La categoría no puede estar vacía.")
            categoria = input("Ingrese la categoría del producto: ").strip()

        # Validación del Precio (debe ser un número entero válido y positivo)
        precio_valido = False
        precio = 0

        while not precio_valido:
            precio_input = input(
                "Ingrese el precio (entero, sin centavos): "
            ).strip()

            # Verificamos si la cadena contiene únicamente dígitos números positivos
            if precio_input.isdigit():
                precio = int(precio_input)
                if precio >= 0:
                    precio_valido = True
                else:
                    print("Error: El precio debe ser igual o mayor a cero.")
            else:
                print(
                    "Error: Ingrese un valor numérico entero válido (sin centavos o letras)."
                )

        # Se agrega el producto como sublista [nombre, categoria, precio] a la lista principal
        producto_nuevo = [nombre, categoria, precio]
        productos.append(producto_nuevo)

        print(f"\n¡Producto '{nombre}' agregado exitosamente!")

    # --------------------------------------------------------------------------
    # OPCIÓN 2: Mostrar productos
    # --------------------------------------------------------------------------
    elif opcion == "2":
        print("\n--- PRODUCTOS REGISTRADOS ---")

        # Verificamos si la lista contiene elementos
        if len(productos) == 0:
            print("No hay productos registrados en el sistema.")
        else:
            # Recorremos la lista mediante enumerate para obtener la posición (índice + 1)
            for i, prod in enumerate(productos, start=1):
                nombre_prod = prod[0]
                categoria_prod = prod[1]
                precio_prod = prod[2]

                print(
                    f"{i}. Nombre: {nombre_prod} | Categoría: {categoria_prod} | Precio: ${precio_prod}"
                )

    # --------------------------------------------------------------------------
    # OPCIÓN 3: Buscar producto
    # --------------------------------------------------------------------------
    elif opcion == "3":
        print("\n--- BUSCAR PRODUCTO ---")

        if len(productos) == 0:
            print("El sistema no cuenta con productos para realizar búsquedas.")
        else:
            busqueda = (
                input("Ingrese el nombre del producto a buscar: ")
                .strip()
                .lower()
            )

            while busqueda == "":
                print("Error: El texto de búsqueda no puede estar vacío.")
                busqueda = (
                    input("Ingrese el nombre del producto a buscar: ")
                    .strip()
                    .lower()
                )

            coincidencias = 0

            # Recorremos la lista comparando nombres
            for i, prod in enumerate(productos, start=1):
                # .lower() permite realizar la búsqueda sin diferenciar mayúsculas/minúsculas
                if busqueda in prod[0].lower():
                    print(
                        f"Coincidencia #{i} -> Nombre: {prod[0]} | Categoría: {prod[1]} | Precio: ${prod[2]}"
                    )
                    coincidencias += 1

            if coincidencias == 0:
                print(
                    f"No se encontraron resultados para la búsqueda: '{busqueda}'."
                )

    # --------------------------------------------------------------------------
    # OPCIÓN 4: Eliminar producto
    # --------------------------------------------------------------------------
    elif opcion == "4":
        print("\n--- ELIMINAR PRODUCTO ---")

        if len(productos) == 0:
            print("No hay productos registrados para eliminar.")
        else:
            # Primero mostramos la lista actual para facilitarle el número al usuario
            print("Lista actual de productos:")
            for i, prod in enumerate(productos, start=1):
                print(f"{i}. {prod[0]} (Categoría: {prod[1]})")

            # Validación de la selección de posición a eliminar
            posicion_valida = False

            while not posicion_valida:
                pos_input = input(
                    "\nIngrese el número (posición) del producto a eliminar: "
                ).strip()

                if pos_input.isdigit():
                    num_posicion = int(pos_input)

                    # Comprobamos que el número ingresado corresponda a un índice existente
                    if 1 <= num_posicion <= len(productos):
                        # Convertimos el número a índice de Python (restando 1)
                        indice_a_eliminar = num_posicion - 1
                        producto_eliminado = productos.pop(indice_a_eliminar)

                        print(
                            f"\n¡El producto '{producto_eliminado[0]}' (Número {num_posicion}) fue eliminado correctamente!"
                        )
                        posicion_valida = True
                    else:
                        print(
                            f"Error: El número debe estar entre 1 y {len(productos)}."
                        )
                else:
                    print("Error: Debe ingresar un número entero válido.")

    # --------------------------------------------------------------------------
    # OPCIÓN 5: Salir del programa
    # --------------------------------------------------------------------------
    elif opcion == "5":
        print("\nGracias por utilizar el sistema de gestión. ¡Hasta luego!")
        break  # Rompe el bucle while True y finaliza la ejecución

    # --------------------------------------------------------------------------
    # Manejo de opciones inválidas del menú
    # --------------------------------------------------------------------------
    else:
        print(
            "\nOpción inválida. Por favor seleccione un número del 1 al 5 según el menú."
        )