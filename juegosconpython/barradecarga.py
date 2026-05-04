import time

# 1. Entrada de numeros en mb
tamaño = int(input("Ingrese el tamaño del archivo (MB): "))
tiempo_total = int(input("Ingrese el tiempo de carga (segundos): "))

print(f"\nIniciando subida de {tamaño} MB...")

#  intervalos de 10% (10 pasos en total)
pasos = 10
tiempo_por_paso = tiempo_total / pasos

for i in range(1, pasos + 1):
    # Espera del tiempo 
    time.sleep(tiempo_por_paso)
    
    # Calcula porcentaje y barra
    porcentaje = i * 10
    barra = "#" * i + "-" * (pasos - i)
    

    print(f"[{barra}] {porcentaje}%")

# Mensaje final
print(f"\n¡Archivo de {tamaño} MB subido con éxito!")



