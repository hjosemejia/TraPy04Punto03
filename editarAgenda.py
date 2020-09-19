"""
****************** TRABAJO SOBRE PYTHON ******************
"""

import os
global dagenda
global tagenda
global lagenda
global dagen
global prueba
dagenda = {}
tagenda = ()
lagenda = []
dagen = {}
prueba = 0

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

class Agenda():
    def __init__(self):
        varia = int(len(lagenda))
        x = 0
        print("********** INGRESAR CONTACTOS **********")
        print("")
        if varia == 0:
            self.nombre = input("NOMBRE DEL CONTACTO => ")
            self.telefono = int(input("CELULAR => "))
            self.email = input("E - MAIL => ")
            tagenda = (self.nombre, self.telefono, self.email)
            agenda = list(tagenda)
            lagenda.append(agenda)
        else:
            name  = input("NOMBRE DEL CONTACTO => ")
            while x < varia:
                tagenda = lagenda[x]
                self.nombre  = tagenda[0]
                if name in self.nombre:
                    print("NOMBRE YA EXISTE")
                    x = varia + 1
                    romper = 1
                else:
                    x += 1
                    romper = 0
            if  romper == 0:
                self.nombre = name
                self.telefono = int(input("CELULAR => "))
                self.email = input("E - MAIL => ")
                tagenda = (self.nombre, self.telefono, self.email)
                agenda = list(tagenda)
                lagenda.append(agenda)
    
        
    
    def EditarAgenda(self, prueba):
        Agenda.ConsultarAgenda(self)
        tagenda = lagenda[prueba]
        self.nombre = tagenda[0]
        var1 = input(f"DESEA EDITAR EL NOMBRE {self.nombre} s/n =>")
        if  (var1 == "s" or var1 == "S"):
            self.nombre = input("NOMBRE DEL CONTACTO => ")
            self.telefono = tagenda[1]
            self.email = tagenda[2]
            tagenda = (self.nombre, self.telefono, self.email)
            agenda = list(tagenda)
            lagenda[prueba] = agenda
        var2 = input(f"DESEA EDITAR EL CELULAR {self.nombre} s/n =>")
        if  (var2 == "s" or var2 == "S"):
            self.nombre = tagenda[0]
            self.telefono = int(input("CELULAR DEL CONTACTO => "))
            self.email = tagenda[2]
            tagenda = (self.nombre, self.telefono, self.email)
            agenda = list(tagenda)
            lagenda[prueba] = agenda
        var3 = input(f"DESEA EDITAR EL E - MAIL {self.nombre} s/n =>")
        if  (var3 == "s" or var3 == "S"):
            self.nombre = tagenda[0]
            self.telefono = tagenda[1]
            self.email = input("E - MAIL DEL CONTACTO => ")
            tagenda = (self.nombre, self.telefono, self.email)
            agenda = list(tagenda)
            lagenda[prueba] = agenda
        
        
def menu():
    presentacion()
    os.system("pause")
    os.system("cls")
    while (True):
        print("****************************************")
        print("|************ __ M E N U __ ***********|")
        print("| 1. INGRESAR NEUVO CONTACTO           |")
        print("| 2. IMPRIMIR LOS CONTACTOS            |")
        print("| 3. CONSULTAR ALGUN CONTACTO          |")
        print("| 4. EDITAR ALGUN CONTACTO             |")
        print("| 5. SALIR DEL PROGRAMA                |")
        print("|______________________________________|")
        print("")
        opc = int(input("DIGITE LA OPCION QUE DESEA: "))
        if  opc == 1:
            agenda = Agenda()
        elif    opc == 2:
            pass
        elif    opc == 3:
            pass
        elif    opc == 4:
            agenda.EditarAgenda(prueba)
        elif    opc == 5:
            print("GRACIAS POR VISITAR NUESTRO SOFTWARE")
            break
        os.system("pause")
        os.system("cls")

def main():
    menu()

if __name__ == "__main__":
    main()