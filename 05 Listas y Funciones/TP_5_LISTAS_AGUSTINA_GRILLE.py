"""
TP 5 - Listas
Tecnicatura Universitaria en Programación

Agustina Grille
Programacion I
"""

# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. utilizar la funcion range.

multiplesDeCuatro = list(range(4, 101, 4))  # Uso de la funcion range. sumo como fin del rango el 101 para excluirlo e incluir el 100. 
# Uso paso 4 para que solo se impriman los múltiplos de 4.
print("Ejercicio 1:", multiplesDeCuatro)

# 2)  Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!

gustos = ["musica", "michis", "anime", "viajes", "lluvia"]
print("Ejercicio 2 (penúltimo):", gustos[-2])  # En este caso, utilizo indexing con número negativo. 

"""
NOTA - Breve explicacion de Indexing Negativo:
Teniendo en cuenta que el indexing negativo analiza el orden de una lista de forma inversa, sin tomar en cuenta la posición "0" (ya que no 
existe el -0 como un numero Real) defino -2 siento la anteultima (o mejor dicho penultima) del array positivo, pero, siendo la segunda ejecución desde atrás
hacia adelante, en un orden de idex negativo. 
"""

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. 

palabras = [] #Creo la lista vacía
#Proceso a sumar palabras con metodo append:
palabras.append("sol") 
palabras.append("luna") 
palabras.append("estrella")
#Fin de sumatoria de palabras
print("Ejercicio 3:", palabras) #Impresion de resultado de la lista final

# 4)  Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente.

animales = ["gato", "iguana", "carpincho", "nutria"]
animales[1] = "loro"       # Selecciono el segundo elemento, tomando en cuenta indice positivo.
animales[-1] = "oso"       # Reutilizando indexing negativo, determino con la posicion -1 el valor del ultimo indice.
print("Ejercicio 4:", animales)

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza. (Imagen del programa en el archivo .PDF)

"""
Ejecutando linea por linea la explicacion seria:


1- Este programa incia definiendo una lista llamada numeros, dentro coloca los valores [8, 15, 3, 22, 7]
2- Con la funcion MAX aplicada en numeros, definimos el valor mas alto dentro del array. En esta misma linea, tambien removemos ese valor alto con el método REMOVE
3- Finalmente PRINT imprimirá por consola el valor de la lista con el mayor eliminado.
4- En pantalla deberia imprimirse algo como esto: [8, 15, 3, 7]
"""

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.

listaSalteada = list(range(10, 31, 5)) #Creo lista con paso 5, imprimiendo numeros entre 10 a 30, la exclusion se realiza a partir del 31. por lo cual 30 entra.
print("Ejercicio 6 (dos primeros):", listaSalteada[:2]) #Imprimo los numeros hasta el segundo indice, por lo cual, solo se mostraran las posiciones 0 y 1.

# 7)  Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.

autos = ["gol", "fitito", "clio", "uno"] #Creo lista de autos
autos[1:3] = ["audi", "tesla"]  # Reemplazo indices 1 y 2
print("Ejercicio 7:", autos) #Imprimo lista final

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.

dobles = [] #Creo un array vacio
dobles.append(5 * 2) #Sumo el doble de 5
dobles.append(10 * 2) #Sumo el doble de 10
dobles.append(15 * 2) #Sumo el doble de 15
print("Ejercicio 8:", dobles) #Imprimo resultados finales

#Otro ejemplo para realizar esta tarea, aprovechando la utilizacion de ciclos repetitivos podría ser:

numerosBase = [5, 10, 15] #Creo una lista de numeros, los cuales básicamente serán los numeros que necesitamos obtener de ellos su doble.
dobles = [] #Creo el array vacio como en el primer paso del ejercicio anterior
#Inicio ciclo for para calculo y mapeo de dobles.
for i in numerosBase:
    dobles.append(i * 2)
#Cierro ciclo for
print("Ejercicio 8:", dobles) #Imprimo 


# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] #Sumo lista definida en la descripcion del ejercicio.
compras[2].append("jugo")              # A) Agrego "jugo" al listado del tercer cliente.
compras[1][1] = "tallarines"           # B) Remplazo "fideos" por "tallarines"
compras[0].remove("pan")               # C) Elimino pan del primer cliente
print("Ejercicio 9:", compras) #Imprimo el listado final

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los elementos definidos en el PDF.

listaAnidada = [15, True, [25.5, 57.9, 30.6], False] #Sumo cada elemento definido en la descripcion.
print("Ejercicio 10:", listaAnidada) #Imprimo lista final.
