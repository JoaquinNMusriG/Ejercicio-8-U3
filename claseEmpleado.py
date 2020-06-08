class Empleado:
    __Dni = ''
    __Nombre = ''
    __Direccion = ''
    __Telefono = ''

    def __init__ (self,dni,nombre,direccion,telefono):
        self.__Dni = dni
        self.__Nombre = nombre
        self.__Direccion = direccion
        self.__Telefono = telefono

    def __str__(self):
        return 'Dni = {} Nombre = {} Direccion = {} Telefono = {}'.format(self.__Dni,self.__Nombre,self.__Direccion,self.__Telefono)

    def getDni (self):
        return self.__Dni

    def getNombre (self):
        return self.__Nombre

    def getDireccion (self):
        return self.__Direccion

    def getTelefono (self):
        return self.__Telefono
