import sys
print("¿Estas preparado para buscar minas recluta?")
print("Bienvenido al Juego de Buscaminas")
print("Identificate recluta ")
nom=input("Nombre: ")
while nom=="":
    print("JAJAJA ¡No sabia que tenia un fantasma frente a mi! ¡PON TU NOMBRE RECLUTA!")
    exit()
    nom=input("Nombre: ")


print("Di el amplio de tu lugar de entrenamiento recluta")
fila=int(input("Vertical: "))
while fila<0:
    print("JAJAJA ¿Te crees gracioso recluta? ¡PON UNA CANTIDAD VALIDA!")
    exit()
    fila=int(input("Vertical: "))

colu=int(input("Horizontal: "))
while colu<0:
    print("JAJAJA ¿Te crees gracioso recluta? ¡PON UNA CANTIDAD VALIDA!")
    exit()
    colu=int(input("Horizontal: "))

print("¿Que tanto quieres sufrir recluta? Indica la cantidad de minas")
minas=int(input("Minas= "))
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
while selfila>fila:
    print("JAJAJA ¿Te llamó tu mami recluta? ¡Elige una fila dentro de el campo de entrenamiento")
    selfila=int(input("Fila: "))

selcolu=int(input("Columna: "))
while selcolu>colu:
    print("JAJAJA ¿Te llamó tu mami recluta? ¡Elige una columna dentro de el campo de entrenamiento")
    selcolu=int(input("Columna: "))
    
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
