#ejercicio de entrenamieto con funcionalidades, condicionales, ciclos 
# MASTER2000

#lista para guardar las notas en global
notas = []
notas_apro = []
notas_repro = []

#funcion de ingresar notas de la cantidad del usuario
def ingresar_notas() : 
    notas.clear()
    notas_apro.clear()
    notas_repro.clear()
    try:
        print("--------------------------------")
        print("--------OPCIÓN-DE-NOTAS---------")
        print("--------------------------------")
        cant_notas = int(input("---INGRESAR-CANTIDAD-DE-NOTAS---: \n "))

        for i in range(1, cant_notas + 1):
            while True:
                try:
                    notita = int(input(f"-INGRESE NOTA N°{i} (DEL 1 AL 100)-: \n"))
                    if 1 <= notita <= 100:
                        notas.append(notita)
                        break  
                    else:
                        print("--LA NOTA DEBE ESTAR ENTRE 1 AL 100--:")
                except ValueError:
                    print("----ERROR-INSERTE-UN-NÚMERO------")
    except ValueError:
        print("----ERROR-INSERTE-UN-NÚMERO------")

#funcion para determinar la aprobacion de las notas
def aprobacion_notas(): 
    print("--------------------------------")
    print("----NOTAS-INGRESADAS-SON--------")
    print("--------------------------------")
    
    for i in range(len(notas)):
        if notas[i] >= 60:
            print(f"Nota {i + 1}: {notas[i]} Aprobado")
            notas_apro.append(notas[i])
        else:
            print(f"Nota {i + 1}: {notas[i]} Reprobado")
            notas_repro.append(notas[i])

#funcion para calcular el promedio de las notas
def promedio_notas():
    if len(notas) == 0:
        print("No hay notas ingresadas.")
        return
    suma = sum(notas)
    promedio = suma / len(notas)
    print(f"El promedio de las notas es: {promedio}")

#notas aprobadas y reprobadas
def notas_apro_repro():
    print("--------------------------------")
    print("-----NOTAS-APROBADAS-SON--------")
    print("--------------------------------")
    print(f"Total aprobadas: {len(notas_apro)}")
    for nota in notas_apro:
        print(nota)
    
    print("--------------------------------")
    print("----NOTAS-REPROBADAS-SON-------")
    print("--------------------------------")
    print(f"Total aprobadas: {len(notas_repro)}")
    for nota in notas_repro:
        print(nota)


#funcion verificar y contar nota especificas
def nota_espe ():
    try:
        print("--------------------------------")
        print("--------NOTAS-ESPECIFICA--------")
        print("--------------------------------")
        buscar = int(input("-INGRESE NOTA PARA SABER SI ESTA EN LAS NOTAS INGRESADAS ANTERIORMENTE"))
        if 1 <= buscar < 100:
            for nota in notas:
                if nota == buscar:
                    contador +=1 

        print(f"---LA-NOTA-ESPECIFICA-ESTA: {contador}-VECES")
    except ValueError:
        print("----ERROR-INSERTE-UN-NÚMERO------")

#Función para que el usuario seleccione la funcion dependiendo la opción
def menu ():
    while True: 
        print("/////////////////////////////////") 
        print("----BIENVENIDO-SERÑOR-USUARIO----") 
        print("/////////////////////////////////") 
        print("------SELECCIONE-UNA-OPCIÓN------") 
        print("1.--------INGRESAR-NOTAS--------:") 
        print("2.-------APROBACION-NOTAS-------:") 
        print("3.--------PROMEDIO-NOTAS--------:") 
        print("4.NOTAS-APROBADAS-&-NO-APROBADAS:") 
        print("5.--------NOTA-EXPECIFICA-------:") 
        print("6.-----------FINALIZAR----------:")
        print("/////////////////////////////////") 
        opcion = input("-------INGRESE UNA OPCION--------")
        return opcion
    
while True:
    try:
        opcion = menu()
        if opcion == "1":
            ingresar_notas()
        elif opcion == "2":
            aprobacion_notas()
        elif opcion == "3":
            promedio_notas()
        elif opcion == "4":
            notas_apro_repro()
        elif opcion == "5":
            nota_espe()
        elif opcion == "6":
            break
        else:
            print("Opción no válida.")
    except ValueError:
        print("Error: ingrese una opción válida.")