import time

<<<<<<< HEAD
# 1. Entrada de numeros en mb
=======
# Entrada de datos
>>>>>>> ba25d737a7b49aaf8a39be110b12c178e4d20105
tamaño = int(input("Ingrese el tamaño del archivo (MB): "))
tiempo_total = int(input("Ingrese el tiempo de carga (segundos): "))

print(f"\nIniciando subida de {tamaño} MB...")

<<<<<<< HEAD
#  intervalos de 10% (10 pasos en total)
=======

>>>>>>> ba25d737a7b49aaf8a39be110b12c178e4d20105
pasos = 10
tiempo_por_paso = tiempo_total / pasos

for i in range(1, pasos + 1):
<<<<<<< HEAD
    # Espera del tiempo 
=======
    # Espera de tiempo 
>>>>>>> ba25d737a7b49aaf8a39be110b12c178e4d20105
    time.sleep(tiempo_por_paso)
    
    # Calcula porcentaje y barra
    porcentaje = i * 10
    barra = "#" * i + "-" * (pasos - i)
    

    print(f"[{barra}] {porcentaje}%")

# Mensaje final
print(f"\n¡Archivo de {tamaño} MB subido con éxito!")



