#print(---"convertir hora de 12 horas a 24 horas---")
#print("ingrese la hora en formato")

#hora_doce= "2:03PM"
#for i in range(len(hora_doce)):
#    print(hora_doce[i])



hora_doce = "01:03PM" # Ejemplo de hora en formato 12 horas

#print(len(hora_doce)) # Imprime la longitud de la cadena hora_doce  

if hora_doce[4] == "A" or hora_doce[5] == "A": # Verifica si la hora es AM
    print(hora_doce)
elif hora_doce[4] == "P" or hora_doce[5] == "P": # Verifica si la hora es PM
    if hora_doce[0] == "1": 
       hora_doce = "13"+hora_doce[1:] # Convierte la hora a formato 24 horas
    elif hora_doce[0] == "2": 
       hora_doce = "14"+hora_doce[1:] 
    elif hora_doce[0] == "3": 
       hora_doce = "15"+hora_doce[1:] 
    elif hora_doce[0] == "4": 
       hora_doce = "16"+hora_doce[1:] 
    elif hora_doce[0] == "5": 
       hora_doce = "17"+hora_doce[1:] 
    elif hora_doce[0] == "6": 
       hora_doce = "18"+hora_doce[1:] 
    elif hora_doce[0] == "7": 
       hora_doce = "19"+hora_doce[1:] 
    elif hora_doce[0] == "8": 
       hora_doce = "20"+hora_doce[1:] 
    elif hora_doce[0] == "9": 
       hora_doce = "21"+hora_doce[1:] 
    elif hora_doce[0] == "10": 
       hora_doce = "22"+hora_doce[1:]   
    elif hora_doce[0] == "11": 
       hora_doce = "23"+hora_doce[1:] 
    elif hora_doce[0] == "12": 
       hora_doce = "00"+hora_doce[1:]

print(hora_doce) 