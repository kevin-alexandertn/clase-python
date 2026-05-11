

# 1. Sin parámetros y Sin retorno: Solo muestra información.
def mostrar_bienvenida():
    print("=======================================")
    print("  =================================")
    print("  = ¡BIENVENIDO A PYTHON COFFEE SHOP! =  ")
    print("=======================================")
    print("   =================================")
    print("Menú de hoy:") 
    print(" Pequeño: $2.00")
    print(" Mediano: $3.00")
    print(" Grande:  $4.00")
    print("---------------------------------------")

#  Sin parámetros y Con retorno: Captura un dato y lo envía fuera.
def pedir_tamaño():
    eleccion = input("¿Qué tamaño de café prefieres? (Pequeño,Mediano,Grande): ")
    return eleccion.lower()

#  Con parámetros y Con retorno: Procesa datos y devuelve un cálculo.
def calcular_precio(tamaño_elegido):
    # Definimos el precio base según el tamaño
    if tamaño_elegido == "pequeño":
        precio_base = 2.00
    elif tamaño_elegido == "mediano":
        precio_base = 3.00
    elif tamaño_elegido == "grande":
        precio_base = 4.00
    else:
        precio_base = 0.00
        print("Tamaño no reconocido, se asignará precio base de $0.00")

    # Calcula un impuesto del 10%
    impuesto = precio_base * 0.10
    total = precio_base + impuesto
    return total

#  Con parámetros y Sin retorno: Recibe datos y realiza una acción (imprimir).
def confirmar_pedido(tamaño, total_final):
    
    print("\n---------------------------------------")
    print( "FACTURA")
    print(f"¡Pedido confirmado!")
    print(f"Café tamaño: {tamaño.capitalize()}")
    print(f"Total a pagar (con impuestos): ${total_final:.2f}")
    print("¡Gracias por visitarnos, vuelve pronto!")
    print("---------------------------------------")



# FLUJO PRINCIPAL PROGRAMA

# Paso 1 Mostrar el menú
mostrar_bienvenida()

# Paso 2 Obtener la elección del usuario y guardarla en una variable
mi_cafe = pedir_tamaño()

# Paso 3 Calcular el precio enviando el tamaño elegido
precio_con_iva = calcular_precio(mi_cafe)

# Paso 4 Mostrar el ticket final
confirmar_pedido(mi_cafe, precio_con_iva)
    
