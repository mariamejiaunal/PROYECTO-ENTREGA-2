import sys  
print("¿Estas preparado para buscar minas recluta?")  #Decimos darle una ambientación al juego como si fueras un recluta del ejercito 
print("Bienvenido al Juego de Buscaminas")
print("Identificate recluta ")
nom=input("Nombre: ") 
# El while lo utilizamos para que en caso tal de que el usuario se equivoque en las entradas que solicitamos, el programa no solo termine si no que muestre un mensaje de error y vuelva a pedir los datos
while nom=="":
    print("JAJAJA ¡No sabia que tenia un fantasma frente a mi! ¡PON TU NOMBRE RECLUTA!")  
    exit()
    nom=input("Nombre: ")

#este while es para que no hayan filas menor o iguales que cero, en otras palabras, que no existan 
print("Di el amplio de tu lugar de entrenamiento recluta")
fila=int(input("Vertical: "))
while fila<0:
    print("JAJAJA ¿Te crees gracioso recluta? ¡PON UNA CANTIDAD VALIDA!")
    exit()
    fila=int(input("Vertical: "))
# este while es igual que el de fila pero para las columnas
colu=int(input("Horizontal: "))
while colu<0:
    print("JAJAJA ¿Te crees gracioso recluta? ¡PON UNA CANTIDAD VALIDA!")
    exit()
    colu=int(input("Horizontal: "))

print("¿Que tanto quieres sufrir recluta? Indica la cantidad de minas")
minas=int(input("Minas= "))
# este while lo dicidimos hacer porque las minas no pueden ser mayores a todo el tablero o que no existan
while (minas<0)or((fila*colu)<minas):
    print("JAJAJA ¿Te crees gracioso recluta? ¡PON UNA CANTIDAD VALIDA!")
    exit()
    minas=int(input("Minas: "))

print(f"Bienvenido al entrenamiento recluta {nom} ")

print("  1  2  3 ")
print(" + - - - +")
print("1| . . . |")
print("2| . . . |")
print("3| . . . |")
print(" + - - - +")

print("¿Donde crees que se encuentra la mina recluta?")
selfila=int(input("Fila: "))
#estos dos while son
# para que la seleccion de la busqueda de la mina no se salga del tablero del juego 
while selfila>fila:
    print("JAJAJA ¿Te llamó tu mami recluta? ¡Elige una fila dentro de el campo de entrenamiento")
    exit()
    selfila=int(input("Fila: "))

selcolu=int(input("Columna: "))
while selcolu>colu:
    print("JAJAJA ¿Te llamó tu mami recluta? ¡Elige una columna dentro de el campo de entrenamiento")
    exit()
    selcolu=int(input("Columna: "))
    
#Como en la guia del trabajo decia que debiamos asumir que el usuario siempre iba a ingresar filas=columans=3, entonces utilizamos un if para poner todos los casos posibles en los que puede seleccionar el usuario su primer mina dentro del tableto 3x3. luego avanzariamos en hacerlo con un bucle for
if (selfila==1)and(selcolu==1):
    print("  1  2  3 ")
    print(" + - - - +")
    print("1| X . . |")
    print("2| . . . |")
    print("3| . . . |")
    print(" + - - - +")

elif (selfila==1)and(selcolu==2):
    print("  1  2  3 ")
    print(" + - - - +")
    print("1| . . . |")
    print("2| X . . |")
    print("3| . . . |")
    print(" + - - - +")
    
elif (selfila==1)and(selcolu==3):
    print("  1  2  3 ")
    print(" + - - - +")
    print("1| . . . |")
    print("2| . . . |")
    print("3| X . . |")
    print(" + - - - +")

elif (selfila==2)and(selcolu==1):
    print("  1  2  3 ")
    print(" + - - - +")
    print("1| . X . |")
    print("2| . . . |")
    print("3| . . . |")
    print(" + - - - +")

elif (selfila==2)and(selcolu==2):
    print("  1  2  3 ")
    print(" + - - - +")
    print("1| . . . |")
    print("2| . X . |")
    print("3| . . . |")
    print(" + - - - +")

elif (selfila==2)and(selcolu==3):
    print("  1  2  3 ")
    print(" + - - - +")
    print("1| . . . |")
    print("2| . . . |")
    print("3| . X . |")
    print(" + - - - +")

elif (selfila==3)and(selcolu==1):
    print("  1  2  3 ")
    print(" + - - - +")
    print("1| . . X |")
    print("2| . . . |")
    print("3| . . . |")
    print(" + - - - +")

elif (selfila==3)and(selcolu==2):
    print("  1  2  3 ")
    print(" + - - - +")
    print("1| . . . |")
    print("2| . . X |")
    print("3| . . . |")
    print(" + - - - +")


elif (selfila==3)and(selcolu==3):
    print("  1  2  3 ")
    print(" + - - - +")
    print("1| . . . |")
    print("2| . . . |")
    print("3| . . X |")
    print(" + - - - +")
