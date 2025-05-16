# TP 1 - Estructuras Secuenciales - UTN a distancia

# 1- Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

# 2- Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo 
# usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe 
# imprimir por pantalla “Hola Marcos!”
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3- Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años 
# y vivo en Argentina”.
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4- Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
# su perímetro.
import math
radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"Área: {area:.2f}, Perímetro: {perimetro:.2f}")

# 5- Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
# cuántas horas equivale.
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"Equivale a {horas:.2f} horas")

# 6- Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
# multiplicar de dicho número.
numero = int(input("Ingrese un número: "))
print(f"Tabla del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# 7- Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1 = int(input("Ingrese el primer número (distinto de 0): "))
num2 = int(input("Ingrese el segundo número (distinto de 0): "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division:.2f}")

# 8- Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su 
# índice de masa corporal
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

# 9- Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla 
# su equivalente en grados Fahrenheit. 
temp_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temp_fahrenheit = (9/5) * temp_celsius + 32
print(f"La temperatura en Fahrenheit es: {temp_fahrenheit:.2f}°F")

# 10- Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de 
# dichos números.
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))
promedio = (n1 + n2 + n3) / 3
print(f"El promedio es: {promedio:.2f}")
