"""
****************** TRABAJO SOBRE PYTHON ******************
"""

import os
global dbanco
global tbanco
global lbanco
global dban
global prueba
dbanco = {}
tbanco = ()
lbanco = []
dban = {}

def presentacion():
    os.system("cls")
    print("****************************************")
    print("|** TRABAJO DE BASE DE DATOS AVANZADA **")
    print("|                                      |")
    print("|          JORGE ACOSTA PERTUZ         |")
    print("|           HECTOR MEJIA BUENO         |")
    print("|          MOISES RAMIREZ MARIN        |")
    print("|                                      |")
    print("|     ING. JAIDER QUINTERO MENDOZA     |")
    print("|               DOCENTE                |")
    print("|                                      |")
    print("|             UNIGUAJIRA               |")
    print("|       FACULTAD DE INGENIERIA         |")
    print("|        PROGRAMA DE SISTEMAS          |")
    print("|        DISTRITO DE RIOHACHA          |")
    print("|                2020                  |")
    print("|______________________________________|")



def menu():
    presentacion()
    os.system("pause")
    os.system("cls")
    while (True):
        print("****************************************")
        print("|************ __ M E N U __ ***********|")
        print("| 1. INGRESAR NEUVO CLIENTE            |")
        print("| 2. IMPRIMIR LOS CLIENTES             |")
        print("| 3. DEPOSITO DE DINERO                |")
        print("| 4. RETIRO DE DINERO                  |")
        print("| 5. SALIR DEL PROGRAMA                |")
        print("|______________________________________|")
        print("")
        opc = int(input("DIGITE LA OPCION QUE DESEA: "))
        if  opc == 1:
            pass
        elif    opc == 2:
            pass
        elif    opc == 3:
            pass
        elif    opc == 4:
            pass
        elif    opc == 5:
            print("GRACIAS POR VISITAR NUESTRO SOFTWARE")
            break
        os.system("pause")
        os.system("cls")

def main():
    menu()

if __name__ == "__main__":
    main()