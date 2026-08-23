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

a = True
b = False
print(f'(a and b) or True  ->  {(a and b) or True}') 

a = False
b = False
print(f'(a and b) or True  ->  {(a and b) or True}') 