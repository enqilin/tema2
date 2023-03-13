import os
import platform

def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def valido_punto(x,y):
    try :
        x,y = float(x),float(y)
    except:
        x= input("Ingrese de nuevo el número: ")
        y= input("Ingrese de nuevo el número: ")
        return x,y
    