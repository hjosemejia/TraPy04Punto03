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
        print("********** INGRESAR CLIENTE **********")
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
    
    
    def RetiroDinero(self):
        print("**********  RETIRO DE DINERO **********")
        print("")
        varia = int(len(lbanco))
        x = 0
        iden = int(input("IDENTIFICACION DEL CLIENTE => "))
        while x < varia:
            tbanco = lbanco[x]
            self.iden = tbanco[0]
            self.nombre = tbanco[1]
            self.cantidad = tbanco[2]
            if iden == self.iden:
                print(f"IDENTIFICACION => {self.iden}")
                print(f"CLIENTE => {self.nombre}")
                print(f"SALDO => ${self.cantidad}")
                print("")
                cant =  int(input("CANTIDAD DE DINERO A RETIRAR => $"))
                retir = self.cantidad - cant
                if retir < 0:
                    print("SALDO INSUFICIENTE")
                    self.cantidad = tbanco[2]
                else:
                    self.cantidad = retir
                    print(f"NUEVO SALDO => ${self.cantidad}")
                x += varia
            else:
                print("IDENTIFICACION NO ENCONTRADA")
                x += 1
        
class Banco(CLiente):
    def __init__(self):
        super().__init__()
    
    def ImprimirBanco(self):
        super().ImprimirCliente()
    
    def DepositoBanco(self):
        super().DepositoDinero()
    
    def RetiroBanco(self):
        super().RetiroDinero()
    


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
        print("| 4. EDITAR ALGUN CONTACTO             |")
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
            banco.RetiroBanco()
        elif    opc == 5:
            print("GRACIAS POR VISITAR NUESTRO SOFTWARE")
            break
        os.system("pause")
        os.system("cls")

def main():
    menu()

if __name__ == "__main__":
    main()