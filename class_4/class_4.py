# 1. Ingreso y formateo de nombre y apellido
nombre = input("Ingrese su nombre: ").strip().title()
apellido = input("Ingrese su apellido: ").strip().title()

# 2. Ingreso y validación del correo electrónico
email = input("Ingrese su correo electrónico: ").strip().replace(" ", "")

# Validamos que el correo tenga exactamente una '@'
if email.count("@") != 1:
    print("\n[Advertencia] El correo ingresado no es válido (debe contener exactamente una '@').")

# 3. Ingreso de edad y clasificación por rango etario
edad = int(input("Ingrese su edad: "))

if edad < 15:
    rango_etario = "Niño/a"
elif 15 <= edad <= 18:
    rango_etario = "Adolescente"
else:
    rango_etario = "Adulto/a"

# Salida de resultados con formato
print("\n--- DATOS DEL CLIENTE ---")
print(f"Nombre completo: {apellido}, {nombre}")
print(f"Correo electrónico: {email}")
print(f"Rango etario: {rango_etario}")

##E-MAIL robusto
email = input("Ingrese su correo electrónico: ").strip().replace(" ", "")

# Separamos el correo en usuario y dominio usando la '@'
# if email.count("@") == 1:
#   usuario, dominio = email.split("@")
    
    # Validamos que el usuario no esté vacío y que el dominio contenga al menos un punto
#    if usuario and "." in dominio and not dominio.startswith(".") and not dominio.endswith("."):
#        print("Correo válido registrado correctamente.")
#    else:
#        print("\n[Error] El dominio o el usuario no son válidos.")
#        print("Sugerencia: Ingrese una estructura válida como 'usuario@dominio.com'.")
# else:
#    print("\n[Error] Formato de correo incorrecto.")
#    print("Sugerencia: El correo debe tener la estructura 'usuario@dominio.com' (con exactamente un '@').")


## Explicación:
## email.split("@"): Divide la cadena en dos variables: usuario (lo que está antes de la @) y 
## dominio (lo que está después).

## usuario: Evalúa que no sea una cadena vacía (evita correos como @dominio.com).

## "." in dominio: Asegura que la sección del dominio tenga al menos un punto.

## not dominio.startswith(".") y not dominio.endswith("."): Evita casos como usuario@.com o 
## usuario@dominio..