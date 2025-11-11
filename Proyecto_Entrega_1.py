import random  # esta libreria es para llamar la función random.randint


#Esta es la introducción al juego 
print("¿Estás preparado para buscar minas, recluta?")
print("Bienvenido al entrenamiento de Buscaminas del ejército")
print("Identifícate, soldado.")


#pedimos el nombre del jugador para que sea mas interactivo 
nombre = input("Nombre: ")
while nombre == "":
    print("JAJAJA ¡No sabía que tenía un fantasma frente a mí! ¡PON TU NOMBRE, RECLUTA!")
    nombre = input("Nombre: ")

print(f"Bienvenido al entrenamiento, recluta {nombre}.")
print("Di el tamaño de tu campo de entrenamiento (máximo 9x9).")

# se valida la cantidad de filas que el jugador va a ingresar, si el jugador ingresar una cantidad incorrecta, entonces, el juego le regaña 
filas = int(input("Vertical (número de filas): "))
while filas <= 0 or filas > 9:
    print("JAJAJA ¿Te crees gracioso, recluta? ¡PON UNA CANTIDAD VÁLIDA ENTRE 1 Y 9!")
    filas = int(input("Vertical (número de filas): "))
    
# Se valida la cantidad de columnas que el jugador va a ingresar, si el jugador ingresa una cantidad incorrecta, entonces, el juego le regaña
columnas = int(input("Horizontal (número de columnas): "))
while columnas <= 0 or columnas > 9:
    print("JAJAJA ¿Te crees gracioso, recluta? ¡PON UNA CANTIDAD VÁLIDA ENTRE 1 Y 9!")
    columnas = int(input("Horizontal (número de columnas): "))
    
    

# Aqui se valida la cantidad de minas que va a ingresar el usuario, ya que no puede exceder el tamaño del tablero, si no se ingresar un numero valido, el juego vuelve a preguntar y regña al usuario 
minas = int(input("¿Qué tanto quieres sufrir, recluta? Indica la cantidad de minas: "))
while minas <= 0 or minas >= filas * columnas:
    print("JAJAJA ¿Te crees gracioso, recluta? ¡PON UNA CANTIDAD VÁLIDA DE MINAS!")
    minas = int(input("¿Qué tanto quieres sufrir, recluta? Indica la cantidad de minas: "))

print(f"\nBienvenido al campo de entrenamiento, recluta {nombre}!\n")

#Aqui se crea un tablero vacio para uso interno en los calculos o memoria de las minas y ubicacion de estas o seleccion del jugador y lo mas importante para la creacion del tablero visible
tablero = [['0' for _ in range(columnas)] for _ in range(filas)]

# esto es para poner las minas en lugares aleatorios del programa 
for i in range(minas):
    while True:
        Fila = random.randint(0, filas - 1) #la funcion random.randint nos ayuda a generar las minas aleatorias entre el rango de las filas y las columnas
        Columna = random.randint(0, columnas - 1)
        if tablero[Fila][Columna] != '*':
            tablero[Fila][Columna] = '*'
            break

# estos for nos ayudan a calcular los numeros que indican cuantas minas hay al rededor de la casilla seleccionada 
for Fila in range(filas):
    for Columna in range(columnas):
        if tablero[Fila][Columna] == '*':
            continue
        contador = 0
        for i in range(Fila - 1, Fila + 2):
            for j in range(Columna - 1, Columna + 2):
                if 0 <= i < filas and 0 <= j < columnas:
                    if tablero[i][j] == '*':
                        contador += 1
        tablero[Fila][Columna] = contador

# este seria el tablero que ve el jugador mientras juega, ya modificado con las casillas, los numeros  y las minas 
visible = [['.' for _ in range(columnas)] for _ in range(filas)]

# esta funcion es para que se pueda mostrar el tablero, la hicimos para que no tuvieramos que repetir el mismo bloque de codigo cada vez que se tuviera que actualizar 
def mostrar(tab):
    print("   ", end="")
    for Columna in range(1, columnas + 1):
        print(Columna, end=" ")
    print()
    print("  + " + "- " * columnas + "+")
    for Fila in range(filas):
        print(f"{Fila + 1}| ", end="")
        for Columna in range(columnas):
            print(tab[Fila][Columna], end=" ")
        print("|")
    print("  + " + "- " * columnas + "+")

# Aqui ya comienza el juego como tal
print("Este es tu campo, recluta. ¡Evita las minas y sobrevive!\n")
mostrar(visible)


while True:
    # Esta parte del codigo es para elegir la casilla que va a jugar  y verificar que si este dentro del campoo 
    seleccion_columna = int(input("Elige una columna para inspeccionar: ")) - 1
    seleccion_fila = int(input("Elige una fila para inspeccionar: ")) - 1

    if not (0 <= seleccion_columna < columnas and 0 <= seleccion_fila < filas):
        print("JAJAJA ¿Te llamó tu mami, recluta? ¡Elige una posición dentro del campo!")
        continue
    

    # aqui s ehacen las comprobaciones de si elegio una mina o si no, en el caso de que si haya elegido una mina
    # se le dira al jugador y ademas se le mostrara el campo visible donde se encontraban todas las minas y si no toca una minas
    # se actualiza el tablero mostrando el contador, osea  cuantas minas hay alrededor de la casilla o si no hay ninguna mina
    if tablero[seleccion_fila][seleccion_columna] == '*':
        print("\n ¡BOOM! Tocaste una mina, recluta. ")
        print("Este era el campo completo:")
        mostrar(tablero)
        print(f"\n Has fallado, {nombre}. El entrenamiento terminó.")
        break
    else:
        visible[seleccion_fila][seleccion_columna] = tablero[seleccion_fila][seleccion_columna]
        print("\n Campo actualizado:")
        mostrar(visible)

    # Esta parte del codigo verifica la cantidad de minas por la cantidad de casillas, y si el jugador selecciono la cantidad de casillas sin minas
    # El juego le dara la victoria
    ganado = True
    for Fila in range(filas):
        for Columna in range(columnas):
            if visible[Fila][Columna] == '.' and tablero[Fila][Columna] != '*':
                ganado = False

    if ganado:
        print("\n¡FELICIDADES, RECLUTA! Has superado el entrenamiento")
        mostrar(tablero)
        break

