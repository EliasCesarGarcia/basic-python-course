# Solicitar datos al cliente
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad_input = input("Ingresa tu edad: ")
email = input("Ingresa tu email: ")

# 2. Validar los datos según los requisitos
# - strip() elimina espacios en blanco al inicio y al final
    #Se usa .strip() para evitar que el usuario ingrese solo espacios en blanco.
# - isdigit() asegura que la edad sea un número entero válido antes de convertirlo
    #Se añadió .isdigit() para prevenir que el programa falle si el usuario escribe letras en la edad
if(
    nombre.strip() == ""
    or apellido.strip() == ""
    or email.strip() == ""
    or not edad_input.isdigit()
    or int (edad_input) <= 18
  ):
  # Si algún dato está en blanco o la edad no es mayor a 18, muestra ERROR!
  print ("ERROR!")  

else:
  # 3. Mostrar los datos en el orden que se ingresaron (si son válidos)
  # Mostrar los datos organizados como tarjeta de presentación
    print("\n" + "=" *40)
    print(f"{'TARJETA DE PRESENTACIÓN':^40}")
    print("=" * 40)

    edad = int(edad_input)
    print(f" Nombre:   {nombre}")
    print(f" Apellido: {apellido}")
    print(f" Edad:     {edad} años")
    print(f" Correo:   {email}")
    print("=" * 40)
