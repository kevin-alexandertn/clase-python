import random
#1 funciones que no resiven parametros y no devuelven parametros
def mostrar_bienvenida():
    #no hay parametros de entrada entre los parentesis
    print("bienvenido a la funcion de bienvenida")
    print("por favor, selecciona una obcion del menu.")
    print("1. opcion 1")
    print("2. opcion 2")
    print("3. opcion 3")
    print("4.salir")

mostrar_bienvenida ()

#funcion que resive parametros pero no devuelve resultados

def saludar_persona (nombre,edad):
    #resive "nobre" y "edad" como parametros de entrada
    print(f"¡hola {nombre}, veo que tienes {edad} años!")
    #no tiene return, solo imprime en pantalla en mensaje
saludar_persona ("estrella",47)

# funciones que no reciben parametros y devuelve resultados


def tirar_dado():
    #no recibe parametros de entrada
    numero_obtenido = random.randint(1,6)
    return numero_obtenido
resultado = tirar_dado()
print (f"has tirado el dado y obtuviste:{resultado}")

#
def calcular_area_rectangulo(base,altura):
    area= base*altura
    return area


mi_area= calcular_area_
