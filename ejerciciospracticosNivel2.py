#6. Categoría de edad
#Enunciado: Pide la edad al usuario y clasifícalo según las siguientes categorías: 0-12 (Niño), 13-17 (Adolescente), 18-64 (Adulto), 65 o más (Adulto mayor).
#Conceptos: Operadores lógicos (and) o anidamiento de elif.

edad= int(input("escriba su edad:"))
if edad >=0 and edad <=12:
    print ("es un niño")
elif edad >= 13 and edad <= 17:
    print("Eres ADOLESCENTE.")
elif edad >= 18 and edad <= 64:
    print("Eres ADULTO.")
elif edad >= 65:
    print("Eres ADULTO MAYOR.")
else:
    print("Edad no válida.")

#7. Descuento en la tienda
#Enunciado: Una tienda ofrece descuentos según el monto de la compra. Si es menor a $50, no hay descuento. Si está entre $50 y $100, hay un 5% de descuento. Si es mayor a $100, el descuento es del 10%. Pide el total de la compra y muestra el total a pagar.
#Conceptos: Variables, if-elif-else, cálculos de porcentajes.

# Programa: Descuento en la tienda

# Solicitar 
compra = float(input("Ingrese el monto total de la compra: $"))

#  Calcular el descuento según el scr
if compra < 50:
    descuento = 0
elif compra >= 50 and compra <= 100:
    descuento = compra * 0.05   # 5% de descuento
else:
    descuento = compra * 0.10   # 10% de descuento

# Calcular el total a pagar
total = compra - descuento

#Mostrar resultados
print("Monto de la compra: $", compra)
print("Descuento aplicado: $", descuento)
print("Total a pagar: $", total)

#8. Año bisiesto
#Enunciado: Pide al usuario que ingrese un año. El programa debe determinar si es bisiesto o no (Un año es bisiesto si es divisible por 4, excepto si es divisible por 100, a menos que también sea divisible por 400).
#Conceptos: Operador módulo (%), operadores lógicos anidados (and, or).

# Programa: Año bisiesto

año = int(input("Ingresa un año: "))

# Verificar si es bisiesto
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("El año", año, "es BISIESTO.")
else:
    print("El año", año, "NO es bisiesto.")

#9. Calculadora de IMC (Índice de Masa Corporal)
#Enunciado: Pide al usuario su peso (en kg) y su altura (en metros). Calcula el IMC (peso/altura^2) y muestra en qué rango se encuentra: Bajo peso (<18.5), Normal (18.5 - 24.9), Sobrepeso (25 - 29.9) u Obesidad (>=30).
#Conceptos: Fórmulas matemáticas, if-elif-else.

peso= float(input("ingresar peso en kg:"))
altura=float(input("ingresar su altura en metros:"))
# 2. Calcular el IMC usando la fórmula: peso / altura^2
imc = peso / (altura ** 2)

# Clasificar el resultado según los rangos bajo n y o
if imc < 18.5:
    categoria = "Bajo peso"
elif imc >= 18.5 and imc <= 24.9:
    categoria = "Normal"
elif imc >= 25 and imc <= 29.9:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

#  Mostrar resultados
print("Su IMC es:", round(imc, 2))
print("Categoría:", categoria)


