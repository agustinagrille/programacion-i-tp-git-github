"""
TP 3 - Estructuras Condicionales
Tecnicatura Universitaria en Programación - UTN 

Agustina A. Grille
Programacion I

Descripción:
Este archivo resuelve cada ejercicio propuesto para el TP3 de estructuras condicionales.

"""

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

print("Ejercicio 1:")
edad = int(input("Ingresa tu edad: "))
if edad > 18:
    print("Es mayor de edad.")
print()

# 2)  Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

print("Ejercicio 2:")
nota = int(input("Ingresa tu nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
print()

# 3) ) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

print("Ejercicio 3:")
numero = int(input("Ingrese un número par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
print()

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece

print("Ejercicio 4:")
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")
print()

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

print("Ejercicio 5:")
password = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")
if 8 <= len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
print()

# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números

print("Ejercicio 6:")
import random
from statistics import mean, median, mode

numerosAleatorios = [random.randint(1, 100) for i in range(50)]
media = mean(numerosAleatorios)
mediana = median(numerosAleatorios)
modeVar = mode(numerosAleatorios)

print("Media:", media)
print("Mediana:", mediana)
print("ModeVar:", modeVar)

if media > mediana > modeVar:
    print("Sesgo positivo o a la derecha")
elif media < mediana < modeVar:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == modeVar:
    print("Sin sesgo")
print()

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

print("Ejercicio 7:")
frase = input("Ingrese una frase o palabra: ")
if frase[-1].lower() in "aeiou":
    print(frase + "!")
else:
    print(frase)
print()

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee

print("Ejercicio 8:")
nombre = input("Ingrese su nombre: ")
opcion = int(input("Elija una opción: 1-Mayúsculas, 2-Minúsculas, 3-Capitalizar: "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida")
print()

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla

print("Ejercicio 9:")
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve")
elif 3 <= magnitud < 4:
    print("Leve")
elif 4 <= magnitud < 5:
    print("Moderado")
elif 5 <= magnitud < 6:
    print("Fuerte")
elif 6 <= magnitud < 7:
    print("Muy fuerte")
else:
    print("Extremo")
print()

# 10)  Utilizando la información aportada en la siguiente tabla sobre las estaciones del año

print("Ejercicio 10:")
hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
mes = int(input("Ingrese el número de mes (1-12): "))
dia = int(input("Ingrese el día del mes: "))

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion = "Invierno" if hemisferio == "N" else "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion = "Primavera" if hemisferio == "N" else "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion = "Verano" if hemisferio == "N" else "Invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion = "Otoño" if hemisferio == "N" else "Primavera"
else:
    estacion = "Fecha inválida"

print("Estación:", estacion)
