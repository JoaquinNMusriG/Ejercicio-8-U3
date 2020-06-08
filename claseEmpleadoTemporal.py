class EmpleadoTemporal:
    __FechaInicio = None
    __FechaFin = None

    def __init__ (self,fechaI,fechaF):
        self.__FechaInicio = fechaI
        self.__FechaFin = fechaF

    def getFechaI(self):
        return self.__FechaInicio

    def getFechaF(self):
        return self.__FechaFin
