from claseEmpleado import Empleado
from claseContratado import Contratado
from claseExterno import Externo
from clasePlanta import Planta
import numpy as np
import csv
from datetime import date
from zope.interface import implementer
from claseITesorero import ITesorero
from claseIGerente import IGerente

@implementer (ITesorero)
@implementer (IGerente)
class Coleccion:
    __dimension = 0
    __actual = 0
    __empleados = None

    def __init__(self, dimension=10):
        self.__empleados = np.empty(dimension, dtype=Empleado)
        self.__dimension = dimension
        self.__actual = 0
        if self.__actual < self.__dimension:
            archivo = open('planta.csv')
            reader = csv.reader(archivo, delimiter = ';')
            lim = 0
            for row in reader:
                lim += 1
            i = 0
            archivo.seek(0)
            while (self.__actual < self.__dimension) & (i < lim):
                list = next(reader)
                unEmpleado = Planta(list[0],list[1],list[2],list[3],float(list[4]),int(list[5]))
                self.__empleados[self.__actual] = unEmpleado
                self.__actual += 1
                i += 1
            if self.__actual < self.__dimension:
                archivo = open('contratado.csv')
                reader = csv.reader(archivo, delimiter = ';')
                lim = 0
                for row in reader:
                    lim += 1
                i = 0
                archivo.seek(0)
                while (self.__actual < self.__dimension) & (i < lim):
                    list = next(reader)
                    unEmpleado = Contratado(list[0],list[1],list[2],list[3],date.fromisoformat(list[4]),date.fromisoformat(list[5]),int(list[6]))
                    self.__empleados[self.__actual] = unEmpleado
                    self.__actual += 1
                    i += 1
                if self.__actual < self.__dimension:
                    archivo = open('externo.csv')
                    reader = csv.reader(archivo, delimiter = ';')
                    lim = 0
                    for row in reader:
                        lim += 1
                    i = 0
                    archivo.seek(0)
                    while (self.__actual < self.__dimension) & (i < lim):
                        list = next(reader)
                        unEmpleado = Externo(list[0],list[1],list[2],list[3],list[4],date.fromisoformat(list[5]),date.fromisoformat(list[6]),float(list[7]),float(list[8]),float(list[9]))
                        self.__empleados[self.__actual] = unEmpleado
                        self.__actual += 1
                        i += 1

    def mostrar (self):
        for empleado in self.__empleados:
            print(empleado)

    def registrarH (self, dni):
        band = False
        indice = 0
        while (indice < self.__actual) & (not band):
            if (self.__empleados[indice].getDni() == dni):
                band = True
            else:
                indice += 1
        if indice < self.__actual:
            if isinstance(self.__empleados[indice],Contratado):
                hora = input('Ingrese la cantidad de horas trabajadas a agregar.')
                if hora.isdigit():
                    self.__empleados[indice].actualizarHora(int(hora))
                else:
                    print('Cantidad inválida, se cancela la solicitud de registro de hora.')
            else:
                print('El empleado no es un empleado CONTRATADO.')
        else:
            print('NO hay informacion de un empleado CONTRATADO con ese dni.')

    def montoTarea(self,tarea):
        band = False
        indice = 0
        while (indice < self.__actual) & (not band):
            if isinstance(self.__empleados[indice],Externo):
                if self.__empleados[indice].getTarea() == tarea.lower():
                    band = True
                else:
                    indice += 1
            else:
                indice += 1
        if indice < self.__actual:
            if self.__empleados[indice].getFechaFin() >= date.today():
                print('El monto a pagar de la tarea es = {}'.format(self.__empleados[indice].getCosto()))
            else:
                print('Esta tarea ya ah finalizado.')
        else:
            print('NO hay informacion de un empleado EXTERNO haciendo esa tarea.')

    def Ayuda (self):
        print('Listado de empleados que les corresponde la ayuda: ')
        i = 0
        for i in range(self.__actual):
            if (self.__empleados[i].getSueldo() < 25000):
                print('Nombre: {}\nDirección: {}\nDni: {}'.format(self.__empleados[i].getNombre(),self.__empleados[i].getDireccion(),self.__empleados[i].getDni()))
                print('-----')
            i += 1

    def mostrarEmpleados (self):
        print('Listado de empleados: ')
        i = 0
        for i in range(self.__actual):
            print('\nNombre: {}\nTelefono: {}\nSueldo= {}'.format(self.__empleados[i].getNombre(),self.__empleados[i].getTelefono(),self.__empleados[i].getSueldo()))
            print('-----')
            i += 1

    def gastosSueldoPorEmpleado (self, dni):
        i = 0
        resultado = None
        while (i < self.__actual) & (self.__empleados[i].getDni() != dni):
            i += 1
        if i < self.__actual:
            resultado = self.__empleados[i].getSueldo()
        return resultado

    def modificarBasicoEPlanta(self, dni, nuevoBasico):
        i = 0
        resultado = False
        while (i < self.__actual) & (self.__empleados[i].getDni() != dni) & (type(self.__empleados[i]) == Planta):
            i += 1
        if i < self.__actual:
            self.__empleados[i].SetBasico(nuevoBasico)
            resultado = True
        return resultado

    def modificarViaticoEExterno(self, dni, nuevoViatico):
        i = 0
        resultado = False
        while (i < self.__actual) & (self.__empleados[i].getDni() != dni):
            i += 1
        if i < self.__actual:
            if isinstance(self.__empleados[i],Externo):
                self.__empleados[i].SetViatico(nuevoViatico)
                resultado = True
        return resultado

    def modificarValorEPorHora(self, nuevoValorHora):
        Contratado.setValorHora(nuevoValorHora)
        return True
