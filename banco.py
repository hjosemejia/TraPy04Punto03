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

class CLiente():
    def __init__(self):
        varia = int(len(lbanco))
        x = 0
        print("******** INGRESAR CLIENTE ********")
        print("")
        if varia == 0:
            self.iden = int(input("IDENTIFICACION DEL CLIENTE => "))
            self.nombre = input("NOMBRE DEL CLIENTE => ")  
            self.cantidad =  int(input("DINERO PARA ABRIR LA CUENTA => $"))
            tbanco = (self.iden, self.nombre, self.cantidad)
            banco = list(tbanco)
            lbanco.append(banco)
        else:
            iden  = int(input("IDENTIFICACION DEL CLIENTE => "))
            while x < varia:
                tbanco = lbanco[x]
                self.iden  = tbanco[0]
                if iden == self.iden:
                    print("YA EXISTE ESTA IDENTIFICACION ")
                    x = varia + 1
                    romper = 1
                else:
                    x += 1
                    romper = 0
            if  romper == 0:
                self.iden = iden
                self.nombre = input("NOMBRE DEL CLIENTE => ")
                self.cantidad =  int(input("DINERO PARA ABRIR LA CUENTA => $"))
                tbanco = (self.iden, self.nombre, self.cantidad)
                banco = list(tbanco)
                lbanco.append(banco)


class Banco(CLiente):
    def __init__(self):
        super().__init__()



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
            banco = Banco()
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