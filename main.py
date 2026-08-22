#Ejercicio 3

def numeros_impares_juntos(entrada):
    impares = []
    for numero in entrada:
        if numero % 2 != 0:
            impares.append(str(numero))
    return ", ".join(impares)

print(numeros_impares_juntos([1, 2, 3, 4, 5, 6, 7, 22,31]))

#Ejercicio 4
def  lista_elementos_en_comun(lista1, lista2):
    elementos_comunes = []
    for elemento in lista1:
        if elemento in lista2 and elemento not in elementos_comunes:
            elementos_comunes.append(elemento)
    for elemento in elementos_comunes:
        print(elemento)        
lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 3, 6, 7, 8]
lista_elementos_en_comun(lista1, lista2)

#Ejercicio 6
def persona_mayor_de_edad(edad):
    return edad >= 18
print(persona_mayor_de_edad(20))
print(persona_mayor_de_edad(15))


    