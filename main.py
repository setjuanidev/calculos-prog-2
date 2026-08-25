import impresiones

'''
7. Dado el siguiente script, escriba un procedimiento
declarar_comida_favorita(nombre_persona, nombre_comida) con el fin de
mejorar la legibilidad del mismo.

nombre = "Pablo"
comida_favorita = "pollo frito"
print("La comida favorita de " + nombre + " se llama: " + comida_favorita)
nombre = "Pedro"
comida_favorita = "canelones"
print("La comida favorita de " + nombre + " se llama: " + comida_favorita)
nombre = "Juan"
comida_favorita = "pizza"
print("La comida favorita de " + nombre + " se llama: " + comida_favorita)

'''
print(f'\n----EJERCICIO 7----\n')

def declarar_comida_favorita(nombre_persona, nombre_comida):
    print("La comida favorita de " + nombre_persona + " se llama: " + nombre_comida)

declarar_comida_favorita("Pablo", "pollo frito")
declarar_comida_favorita("Pedro", "canelones")
declarar_comida_favorita("Juan", "pizza")





'''
8. Extraer el procedimiento del ejercicio 7 a un archivo impresiones.py,
el cual debe ser importado para su utilizacion.

'''
print(f'\n----EJERCICIO 8----\n')

impresiones.declarar_comida_favorita("Pablo", "pollo frito")
impresiones.declarar_comida_favorita("Pedro", "canelones")
impresiones.declarar_comida_favorita("Juan", "pizza")





'''
10. Simplificar la siguiente expresion:
(a and b) or True

'''
print(f'\n----EJERCICIO 10----\n')

print('(a and b) or True se simplifica a: True')
#Ejercicio 3

def numeros_impares_juntos(entrada):
    impares = []
    for numero in entrada:
        if numero % 2 != 0:
            impares.append(str(numero))
    return ", ".join(impares)
print(f'\n----EJERCICIO 3----\n')
print(numeros_impares_juntos([1, 2, 3, 4, 5, 6, 7, 22,31]))

#Ejercicio 4
print(f'\n----EJERCICIO 4----\n')
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
print(f'\n----EJERCICIO 6----\n')
def persona_mayor_de_edad(edad):
    return edad >= 18
print(persona_mayor_de_edad(20))
print(persona_mayor_de_edad(15))


    
