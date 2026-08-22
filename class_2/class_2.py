# Solicitar datos al cliente
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
edad = int(edad)
email = input("Ingresa tu email: ")

# Unir nombre y apellido para presentar juntos
nombre_completo = f"{nombre} {apellido}"

# Mostrar los datos organizados como tarjeta de presentación
print("\n" + "=" *40)
print(f"{'TARJETA DE PRESENTACIÓN':^40}")
print("=" * 40)
print(f" Nombre completo: {nombre_completo}")
print(f" Edad           : {edad} años")
print(f" Correo         : {email}")
print("=" * 40)

# f"{...} permite insertar las variables en forma limpia.
# "=" * 40 imprime una línea de 40 caracteres para el crear el marco visual. Se puede multiplicar el texto por un número.
# :^40 centra el título dentro del marco de 40 espacios