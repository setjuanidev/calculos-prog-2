#1.2.5.9
"""
1. Escribir un procedimiento realizar_calculo(). El mismo debe solicitar al 
usuario seleccionar por consola la operación matemática deseada 
(opciones: suma, resta, multiplicación, y división). Luego, debe solicitar 
que se ingresen 2 números. Por último, debe imprimir el resultado. 
Asumir que los valores ingresados son del tipo de datos correcto. 
"""
def realizar_calculo():
    print(f'1 SUMA\n2 RESTA\n3 MULTIPLICACION\n4 DIVISION')
    opcion = int(input(f'Ingrese la opcion matematica deseada.'))
    n1 = int(input(f'Ingrese un numero'))
    n2 = int(input(f'Ingrese un numero'))

    if opcion == 1:
        print(f'Operacion elegida: SUMA\nEl resultado es: {n1 + n2}')
    elif opcion == 2:
        print(f'Operacion elegida: RESTA\nEl resultado es: {n1 - n2}')
    elif opcion == 3:
        print(f'Operacion elegida: MULTIPLICACION\nEl resultado es: {n1 * n2}')
    elif opcion == 4:
        print(f'Operacion elegida: DIVISION\nEl resultado es: {n1 / n2}')
realizar_calculo()