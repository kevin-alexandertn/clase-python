"""
===============================================================================
TALLER AUTÓNOMO: EL ARTE DE LAS FUNCIONES EN PYTHON
===============================================================================
Autor: kevin alexander tarapues calpa
Materia: Fundamentos de Programación / Python
Propósito: Construcción de un script vivo que demuestra la teoría, reglas
           y aplicación práctica de las funciones en Python.
===============================================================================
"""

# =============================================================================
# 1. DEFINICIÓN BÁSICA Y LLAMADA
# =============================================================================
# Concepto: Una función es un bloque de código organizado y reutilizable que 
# se define con la palabra clave 'def' y solo se ejecuta cuando es invocada.

def saludar_comunidad():
    """
    Imprime un saludo básico en la consola.
    (Demostración de Docstring formal)
    """
    print("¡Hola! Bienvenidos al estudio de las funciones en Python.")

# Ejecución
saludar_comunidad()


# =============================================================================
# 2. PASO DE PARÁMETROS Y ARGUMENTOS
# =============================================================================
# Concepto: Los parámetros son las variables en la definición de la función. 
# Los argumentos son los valores reales que se pasan al invocarla, ya sea por 
# posición (orden estricto) o por nombre (keyword arguments), lo que da flexibilidad.

def describir_perfil(nombre, rol):
    # Demuestra el uso de parámetros dentro de una cadena formateada (f-string)
    print(f"El usuario {nombre} se desempeña en el rol de: {rol}.")

# Ejecución por posición (el orden importa)
describir_perfil("Carlos", "Diseñador Digital")

# Ejecución por nombre (el orden no importa gracias a las palabras clave)
describir_perfil(rol="Programador Python", nombre="Sofía")


# =============================================================================
# 3. SENTENCIA RETURN
# =============================================================================
# Concepto: La instrucción 'return' finaliza la ejecución de la función y 
# devuelve un valor o resultado al punto donde fue llamada, permitiendo guardar 
# o reutilizar dicho dato.

def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo a partir de su base y altura.
    Devuelve el resultado numérico.
    (Demostración de Docstring formal)
    """
    area = base * altura
    return area

# Ejecución: Guardamos el valor devuelto en una variable para usarlo después
resultado_area = calcular_area_rectangulo(5, 10)
print(f"El área calculada mediante el retorno de la función es: {resultado_area}")


# =============================================================================
# 4. PARÁMETROS POR DEFECTO (OPCIONALES)
# =============================================================================
# Concepto: Permiten asignar valores predeterminados a los parámetros. Si al 
# llamar a la función no se proporciona un argumento, se usará el valor por defecto.

def configurar_conexion(host, puerto=8080):
    # 'puerto' es opcional, si no se envía, toma el valor 8080
    print(f"Conectando a {host} a través del puerto: {puerto}")

# Ejecución usando el valor por defecto
configurar_conexion("localhost")

# Ejecución sobrescribiendo el valor por defecto
configurar_conexion("192.168.1.1", puerto=443)


# =============================================================================
# 5. VARIABLES LOCALES Y GLOBALES (SCOPE / ALCANCE)
# =============================================================================
# Concepto: El 'scope' determina la visibilidad de una variable. Las variables 
# globales se definen fuera de las funciones y son accesibles en todo el script. 
# Las locales se crean dentro de una función y mueren al finalizar esta.

# Variable Global
proyecto = "Desarrollo de Software en Roldanillo"

def mostrar_alcance():
    # Variable Local: Solo existe dentro de esta función
    version = "v1.0.2"
    print(f"Accediendo a Global desde la función: {proyecto}")
    print(f"Accediendo a Local dentro de la función: {version}")

# Ejecución de la función
mostrar_alcance()

# Demostración del Scope: Intentar imprimir 'version' aquí causaría un NameError 
# porque no existe en el ámbito global.
print(f"Accediendo a Global desde fuera: {proyecto}")


# =============================================================================
# 6. ARGUMENTOS VARIABLES (*args)
# =============================================================================
# Concepto: El parámetro '*args' permite que una función reciba un número 
# indeterminado de argumentos posicionales, los cuales se agrupan en una tupla 
# para poder iterar sobre ellos.

def listar_herramientas(*herramientas):
    # 'herramientas' se comporta como una tupla dentro de la función
    print("Listado de herramientas seleccionadas para el proyecto:")
    for herramienta in herramientas:
        print(f" - {herramienta}")

# Ejecución con 3 argumentos
listar_herramientas("Visual Studio Code", "Git", "GitHub")

# Ejecución con 2 argumentos diferentes demostrando la flexibilidad
listar_herramientas("Photoshop", "Illustrator")