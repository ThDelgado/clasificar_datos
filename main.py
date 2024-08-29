import string 

  

matriz = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]] 

  
#funcion para seleccion la listas quen o tengan cero al comienzo
def seleccionar_Lista(a:list):   
    mi_list = []
    
    for lista in a: 
        if lista[0] == 0: 
            continue 
        else: 
            lista
            mi_list.append(lista)
    return(mi_list)
print("Las listas sin cero al comienzo son: ")
print(seleccionar_Lista(matriz))
print("*****************************")

# funcion para seleccionar los numeros sin cero
def seleccinar_sin_cero(a:list):
    numeros_sin_cero = []
    for lista in a:
        for numero in lista: 
            if numero == 0: 
                continue 
            else: 
               numeros_sin_cero.append(numero)
    return(numeros_sin_cero)

print("Los numeros sin cero son: ")
print(seleccinar_sin_cero(matriz))
print("**************************")




# obtener las primera 9 letras del alfabeto 

keys = string.ascii_uppercase[:4] 

  

values = matriz 

  

def convertirDiccionario (a:str, b:list): 

    diccionario = dict(zip(keys, values)) 

    return diccionario 

  

print("El diccionario es: ") 

print(convertirDiccionario(keys, values)) 