from claseColeccion import Coleccion
from claseMenu import Menu

if __name__ == '__main__':
    cant = input('Ingrese la cantidad de empleados a cargar: ')
    if cant.isdigit():
        empleados = Coleccion(int(cant))
        menu = Menu()
        salir = False
        while not salir:
            print("""
                  0 Salir
                  1 Registrar horas
                  2 Total de tarea
                  3 Ayuda
                  4 Calcular sueldo
                  5 Ingresar usuario""")
            op = int(input('Ingrese una opcion: '))
            menu.opcion(op,empleados)
            salir = op == 0
    else:
        print('Valor inválido.')  
