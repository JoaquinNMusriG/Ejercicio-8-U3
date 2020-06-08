from claseEmpleado import Empleado
from claseEmpleadoTemporal import EmpleadoTemporal

class Externo(Empleado,EmpleadoTemporal):
    __Tarea = ''
    __MontoViatico = 0.0
    __CostoObra = 0.0
    __MontoSeguro = 0.0

    def __init__ (self,dni,nombre,direccion,telefono,tarea,fechaI,fechaF,montoV,costoO,montoS):
        Empleado.__init__(self,dni,nombre,direccion,telefono)
        EmpleadoTemporal.__init__(self,fechaI,fechaF)
        self.__Tarea = tarea
        self.__MontoViatico = montoV
        self.__CostoObra = costoO
        self.__MontoSeguro = montoS

    def __str__(self):
        print(super().__str__())
        return 'Tarea = {} Fecha Inicio = {} Fecha Fin = {} Monto Viatico = {} Costo Obra = {} Monto Seguro = {}'.format(self.__Tarea,self.getFechaI(),self.getFechaF(),self.__MontoViatico,self.__CostoObra,self.__MontoSeguro)

    def getTarea(self):
        return self.__Tarea.lower()

    def getFechaFin (self):
        return self.getFechaF()

    def getCosto (self):
        return self.__CostoObra

    def getSueldo(self):
        return self.__CostoObra - self.__MontoViatico - self.__MontoSeguro

    def SetViatico(self, nuevoV):
        self.__MontoViatico = nuevoV    
