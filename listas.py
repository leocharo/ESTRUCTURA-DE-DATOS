from listas4e import BagNodo

m=BagNodo()                 

r="t"

while r=="t":
    print("------------------------------------------------------------------------------")
    print("                             1. Agregar nuevo valor                           ")
    print("                             2. Buscar valor                                  ")
    print("                             3. Mostrar la lista                              ")
    print("                             4.Sacar Promedio                                 ")
    print("                             5.Tamaño o numero de elementos                   ")
    print("                             6. Encontrar el minimo                           ")
    print("                             7. Sacar el Promedio                             ")
    print("                             9. Salir del programa                            ")
    print("------------------------------------------------------------------------------")

    option=input(                       "Introduce una opcion:                            ")
    match option:
        case"1":
            v=int(input(                "Introduce un valor:                             "))
            m.agregar(v)
        case"2":
            v=int(input(                "Introduce el valor a buscar: "                   ))
            if m.buscar(v):
                print("           *******************************************************************")
                print("                                  EL VALOR SI EXISTE                          ")
                print("           *******************************************************************")
            else:
                print("           *******************************************************************")
                print("                                  NO HAY NINGUN VALOR                         ")
                print("           *******************************************************************")
        case"3":
            m.mostrar()
        case "4":
            print("El promedio de la lista es de: ",m.promedio())  
        case "5":
            print("El tamaño del arreglo es de:",m.length())
        case"6":
            print("El valor minimo de la lista es: ",m.minimo())
        case"7":
            print("El promedio  de la lista es de: ",m.prom())

        case "9":
            r=input("presiona la letra que quieras para terminar :D   : ")