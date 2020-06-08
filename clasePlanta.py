from claseEmpleado import Empleado

class Planta(Empleado):
    __SueldoBasico = 0.0
    __Antiguedad = 0

    def __init__ (self,dni,nombre,direccion,telefono,sueldoB,antiguedad):
        super().__init__(dni,nombre,direccion,telefono)
        self.__SueldoBasico = sueldoB
        self.__Antiguedad = antiguedad

    def __str__(self):
        print(super().__str__())
        return 'SueldoBasico = {} Antiguedad = {}'.format(self.__SueldoBasico,self.__Antiguedad)

    def getSueldo(self):
        return self.__SueldoBasico + 0.01*self.__SueldoBasico*self.__Antiguedad

    def SetBasico(self, nuevoSB):
        self.__SueldoBasico = nuevoSB
