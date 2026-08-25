#1.2.3.4.5.6.7.8.9.10

import impresiones

'''
1. Escribir un procedimiento realizar_calculo(). El mismo debe solicitar al 
usuario seleccionar por consola la operación matemática deseada 
(opciones: suma, resta, multiplicación, y división). Luego, debe solicitar 
que se ingresen 2 números. Por último, debe imprimir el resultado. 
Asumir que los valores ingresados son del tipo de datos correcto. 
'''
def realizar_calculo():

    print(f'1 SUMA\n2 RESTA\n3 MULTIPLICACION\n4 DIVISION')
    opcion = int(input(f'Ingrese la opcion matematica deseada: '))
    n1 = int(input(f'Ingrese un numero: '))
    n2 = int(input(f'Ingrese un numero: '))

    if opcion == 1:
        print(f'Operacion elegida: SUMA\nEl resultado es: {n1 + n2}')
    elif opcion == 2:
        print(f'Operacion elegida: RESTA\nEl resultado es: {n1 - n2}')
    elif opcion == 3:
        print(f'Operacion elegida: MULTIPLICACION\nEl resultado es: {n1 * n2}')
    elif opcion == 4:
        print(f'Operacion elegida: DIVISION\nEl resultado es: {n1 / n2}')

print(f'\n----EJERCICIO 1----\n')
realizar_calculo()


'''2. Escribir una función numero_en_orden_ascendente (numero) que retorne 
True si los dígitos del número están ordenados de menor a mayor, y False 
en caso contrario. '''

def numero_en_orden_ascendente(numero):

    numero = str(numero) #lo convierto a cadena para poder analizar item por tiem
    for i in range(1, len(numero)): #aca recorro el arreglo desde el segundo numero
        if numero[i] < numero [i-1]:#aca comparo el seugundo numero con el primero
            return False
    return True

print(f'\n----EJERCICIO 2----\n')
print(numero_en_orden_ascendente(2))
#numero_en_orden_ascendente()


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


'''5. Escribir una función clave_valida(clave) que devuelva True en caso de superar 
las siguientes validaciones sobre la clave proporcionada por el usuario: 
a. Longitud entre 6 y 20 caracteres. 
b. Debe contener al menos un número. 
c. No puede contener espacios. '''

def clave_valida(clave):

    clave = str(clave)
    if (len(clave) >= 6 and len(clave) <= 20) and (any(i.isdigit() for i in clave)) and (" " not in clave):
        return True

print(f'\n----EJERCICIO 5----\n')
print(clave_valida('hola123'))
#print(clave_valida('je12'))


#Ejercicio 6

print(f'\n----EJERCICIO 6----\n')

def persona_mayor_de_edad(edad):
    return edad >= 18

print(persona_mayor_de_edad(20))
print(persona_mayor_de_edad(15))


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


'''9. Escribir una función cuenta_regresiva(entero_positivo) que imprima números 
enteros empezando por el valor pasado por parámetro y llegando hasta 0. 
Asumir que el número pasado por parámetro es un número entero positivo. 
Utilizar recursividad para desarrollar la solución. 
Ejemplo de salida para cuenta_regresiva(4): 
4 
3 
2 
1 
0'''

def cuenta_regresiva(entero_positivo):
    print(entero_positivo)
    entero_positivo -= 1
    if entero_positivo < 0:
            return
    cuenta_regresiva(entero_positivo)

print(f'\n----EJERCICIO 9----\n')
cuenta_regresiva(4)
cuenta_regresiva(9)


'''
10. Simplificar la siguiente expresion:
(a and b) or True

'''
print(f'\n----EJERCICIO 10----\n')

print('(a and b) or True se simplifica a: True')