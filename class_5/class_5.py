# Inicializamos las variables principales
MESES_TOTALES = 6
mes_actual = 1
total_acumulado = 0.0

print("--- REGISTRO DE INGRESOS MENSUALES ---")

# 1. Bucle while para registrar los ingresos durante 6 meses
while mes_actual <= MESES_TOTALES:
    # Solicitamos la entrada al usuario
    entrada = input(f"Ingrese el ingreso correspondiente al mes {mes_actual}: ")
    
    # Manejo de excepciones para evitar que el programa falle si el usuario ingresa texto
    try:
        ingreso = float(entrada)
        
        # Validamos que el ingreso sea un número positivo (o cero)
        if ingreso < 0:
            print("❌ Error: El valor no es válido. Los ingresos no pueden ser negativos.\n")
            continue  # Salta al siguiente intento del bucle sin avanzar de mes
        
        # Acumulamos el ingreso válido en la variable correspondiente
        total_acumulado += ingreso
        
        # Avanzamos al siguiente mes
        mes_actual += 1

    except ValueError:
        print("❌ Error: Por favor, ingrese un número válido.\n")

# 2. Cálculo del promedio mensual
promedio_mensual = total_acumulado / MESES_TOTALES

# Presentación de los resultados finales
print("\n" + "="*40)
print("             RESUMEN FINANCIERO         ")
print("="*40)
print(f"Total acumulado (6 meses): ${total_acumulado:,.2f}")
print(f"Promedio mensual:          ${promedio_mensual:,.2f}")
print("="*40)

# Explicación breve del flujo

# Validación de positivos: Si el usuario ingresa un valor negativo, 
# la sentencia continue ignora el resto del bloque y vuelve a pedir la entrada del mismo mes.  

# Control de bucle: La variable mes_actual solo se incrementa en 1 cuando el dato ingresado es un número 
# válido y mayor o igual a cero.  

# Cálculos: Al finalizar la iteración de los 6 meses, se obtiene el total mediante el acumulador 
# total_acumulado y se calcula el promedio dividiendo entre 6.  