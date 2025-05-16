"""
TP 4 - Estructuras Repetitivas
Tecnicatura Universitaria en Programación

Agustina Grille
Programacion I
"""

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for numero in range(101):
    print(numero)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = input("Ingrese un número entero: ")
print(f"Cantidad de dígitos: {len(numero)}")

# 3) ) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))
suma = 0
for numero in range(inicio + 1, fin):
    suma += numero
print(f"La suma es: {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

acumulador = 0
while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    acumulador += numero
print(f"Total acumulado: {acumulador}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
numeroSecreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adiviná el número (entre 0 y 9): "))
    intentos += 1
    if intento == numeroSecreto:
        print(f"¡Correcto! Lo lograste en {intentos} intentos.")
        break

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente

for numero in range(100, -1, -1):
    if numero % 2 == 0:
        print(numero)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

limite = int(input("Ingrese un número entero positivo: "))
suma = 0
for numero in range(limite + 1):
    suma += numero
print(f"La suma total es: {suma}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cantidadNumeros = 100  
pares = impares = positivos = negativos = 0
for i in range(cantidadNumeros):
    numero = int(input(f"Ingrese el número {i+1}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero >= 0:
        positivos += 1
    else:
        negativos += 1
print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).


cantidadNumeros = 100  
sumaTotal = 0
for i in range(cantidadNumeros):
    numero = int(input(f"Ingrese el número {i+1}: "))
    sumaTotal += numero
media = sumaTotal / cantidadNumeros
print(f"La media es: {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingrese un número para invertir: ")
numeroInvertido = numero[::-1]
print(f"Número invertido: {numeroInvertido}")
