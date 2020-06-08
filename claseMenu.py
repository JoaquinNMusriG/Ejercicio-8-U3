from claseColeccion import Coleccion
from claseITesorero import ITesorero
from claseIGerente import IGerente

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 0:self.salir,
                            1:self.registrarHora,
                            2:self.totalTarea,
                            3:self.ayudaEmpleados,
                            4:self.calcularSueldo,
                            5:self.ingresarUsuario,
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op,empleados):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(empleados)
    def salir(self,empleados):
        print('Salir')

    def registrarHora(self,empleados):
        dni = input('Ingrese el dni del empleado CONTRATADO del cual quiere registrar hora: ')
        if dni.isdigit():
            empleados.registrarH(dni)
        else:
            print('Dni inválido.')

    def totalTarea(self,empleados):
        tarea = input('Ingrese la tarea de la que quiere saber el monto: ')
        if tarea.isalpha():
            empleados.montoTarea(tarea)
        else:
            print('Tarea inválida.')

    def ayudaEmpleados(self,empleados):
        empleados.Ayuda()

    def calcularSueldo(self,empleados):
        empleados.mostrarEmpleados()

    def Gerente(self,empleados):
        salir = False
        while not salir:
            print("""
                  0 Salir
                  1 Modificar sueldo basico de empleado de planta
                  2 Modificar monto viatico de empleado externo
                  3 Modificar valor por hora de empleado contratado""")
            op = int(input('Ingrese una opcion: '))
            if (op == 1) or (op == 2):
                dni = input('Ingrese el dni del empleado: ')
                if dni.isdigit():
                    if op == 1:
                        nuevoBasico = input('Ingrese el nuevo valor de sueldo basico: ')
                        try:
                            nuevoBasico = float(nuevoBasico)
                            if empleados.modificarBasicoEPlanta(dni,nuevoBasico):
                                print("Sueldo basico actualizado.")
                            else:
                                print("No hay empleado de planta con ese dni.")
                        except ValueError:
                            print('Sueldo basico inválido.')
                    elif op == 2:
                        nuevoViatico = input('Ingrese el nuevo valor del monto viatico: ')
                        try:
                            nuevoViatico = float(nuevoViatico)
                            if empleados.modificarViaticoEExterno(dni, nuevoViatico):
                                print("Monto Viatico actualizado.")
                            else:
                                print("No hay empleado externo con ese dni.")
                        except ValueError:
                            print('Monto viatico inválido.')
                else:
                    print('Dni inválido.')
            if op == 3:
                nuevoValorHora = input('Ingrese el nuevo valor de hora: ')
                try:
                    nuevoValorHora = float(nuevoValorHora)
                    if empleados.modificarValorEPorHora(nuevoValorHora):
                        print("Valor de hora Actualizado")
                except ValueError:
                    print('Valor de hora inválido.')        
            salir = op == 0

    def Tesorero(self,empleados):
        salir = False
        while not salir:
            print("""
                  0 Salir
                  1 Ver sueldo de empleado por dni""")
            op = int(input('Ingrese una opcion: '))
            if op == 1:
                dni = input('Ingrese el dni del empleado a ver el gasto del sueldo: ')
                if dni.isdigit():
                    rta = empleados.gastosSueldoPorEmpleado(dni)
                    if rta != None:
                        print('El sueldo del empleado es: {}'.format(rta))
                    else:
                        print('No se encontró un empleado con ese dni.')
                else:
                    print('Dni inválido.')
            salir = op == 0


    def ingresarUsuario (self,empleados):
        usuario = input("Ingrese Usuario: ")
        contraseña = input("Ingrese Contraseña: ")
        if (usuario == "uTesorero") & (contraseña == "ag@74ck"):
            self.Tesorero(ITesorero(empleados))
        elif (usuario == "uGerente") & (contraseña =="ufC77#!1"):
            self.Gerente(IGerente(empleados))
        else:
            print("Credenciales incorrectas")
