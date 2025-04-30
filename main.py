#ejercicio de entrenamieto con funcionalidades, condicionales, ciclos 
# MASTER2000

#lista para guardar las notas en global
notas = []

#funcion de pedir notas de la cantidad del usuario
def pedir_notas() : 
    try:
        print("--------OPCIÓN-DE-NOTAS--------")
#       print("--------------------------------")
#        print("--------------------------------")
        cant_notas = (int(input("Ingrese cantidad de notas que desea ingresar")))
        i = 1
        for i in range (cant_notas) :
            notita =input(f"Ingrese la nota {i} del 1 al 100: ")
            notas.append(notita) 
    except ValueError:
        print("Señor@ usuario por favor ingrese sus notas validas")

#Función para que el usuario seleccione la funcion dependiendo la opción
def menu ():
    while True: 
        print("----Bienvenido señor usuario----") 
        print("--------------------------------") 
        print("1. ingresar notas ") 
#        print("") 
#        print("") 
        print("6. finalizar") 
        opcion = input("Ingrese opción")
        return opcion
    
while True:
    try:
        opcion = menu()
        if opcion == "1":
            pedir_notas()
        elif opcion == "3":
            print(notas)
        elif opcion == "6":
            break
        else:
            print("Señor usuario opcion no valida por favor ingrese una opcion valida")
    except ValueError:
        print("Señor usuario ingrese una opcion valida")