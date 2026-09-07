
def añadir(nombres, capacidad):
    if len(nombres)>=capacidad:
        print("la pila ya está llenita")
    else:
        nom=input("Ingrese el caracter a añadir: ")
        nombres.append(nom)

def imprimir(nombres):
  for i in range(len(nombres)):
        print(nombres[i], end=" ")
def quitar(nombres):
    nombres.pop()

def main():
    capacidad =int(input("Ingresa la capadidad de la pila "))
    nombres=[]
    opcion=0
    while opcion != 4: 
        print("Opcion 1: añadir elemento")
        print("Opcion 2: quitar elemento")
        print("Opcion 3: imprimir pila")
        print("Opcion 4: salir")

        opcion=int(input("opcion: "))

        if opcion == 1:
            añadir(nombres, capacidad)
        elif opcion == 2:
            quitar(nombres)
        elif opcion == 3:
            imprimir(nombres)
        else:
            break 

if __name__== "__main__":
    main()