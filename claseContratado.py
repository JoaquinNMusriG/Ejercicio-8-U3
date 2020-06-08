from claseEmpleado import Empleado
from claseEmpleadoTemporal import EmpleadoTemporal

class Contratado(Empleado,EmpleadoTemporal):
    ValorHora = 250

    __CantHoras = 0

    @classmethod
    def getValorHora (cls):
        return cls.ValorHora

    @classmethod
    def setValorHora(cls, nuevoVH):
        cls.ValorHora = nuevoVH    

    def __init__(self,dni,nombre,direccion,telefono,fechaI,fechaF,cantH):
        Empleado.__init__(self,dni,nombre,direccion,telefono)
        EmpleadoTemporal.__init__(self,fechaI,fechaF)
        self.__CantHoras = cantH

    def __str__(self):
        print(super().__str__())
        return 'Fecha Inicio = {} Fecha Fin = {} Cant Horas = {}'.format(self.getFechaI(),self.getFechaF(),self.__CantHoras)

    def getSueldo(self):
        return Contratado.getValorHora()*self.__CantHoras

    def actualizarHora (self,h):
        self.__CantHoras += h
