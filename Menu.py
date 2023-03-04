import os
from tkinter import filedialog
from Lector import Lector

class Menu:
    #funcion para limpiar la consola
    def limpiar__consola(self):
        os.system('clear' if os.name == 'posix' else 'cls')
       

    #metodo para pausar la ejecucion
    def pausa_informacion(self):
        print('        ******** presiona una enter para continuar *****')
        ms_tp= input()

    #impresion del menu
    def print_menu(self):
        self.limpiar__consola()
        print(
                    '''
        ------------- MENU --------------
        |       1. Cargar Archivo       |
        |       2. Gestionar            |
        |       3. graficar             |
        |       4. salir                |
        ---------------------------------
                    '''
                )
    
    #inicio del menu
    def inicio(self):
        while True:
            self.print_menu()
            try:
                sl = int(input('Seleccione una opcion: \n'))
                if sl == 1:
                    nombre_archivo= filedialog.askopenfilename()
                    print(nombre_archivo)
                    Lector.leer_archivo(nombre_archivo)
                    self.pausa_informacion()

                elif sl ==2:
                    print ('*** gestione ***')
                    self.pausa_informacion()
                elif sl == 3:
                    print ('*** imprimiendo ***')
                    self.pausa_informacion()
                elif sl == 4:
                    print('bye')
                    break
                else:
                    print ('*** Opcion no disponible ***')
                    self.pausa_informacion()
            except:
                print('*** Por favor seleccione una opcion valida -Err: menu***')
                self.pausa_informacion()


