import ejercicio1 as db
import helpers

def iniciar():
    while True:
        helpers.limpiar_pantalla()
        print("========================")
        print("  El menu de ejercicio1 ")
        print("========================")
        print("[1] Punto               ")
        print("[2] Rectángulo          ")
        print("[3] Salir               ")
        print("========================")

        opcion = input( "> ")
        helpers.limpiar_pantalla()
        if opcion == '1':
            print("Punto")
            x = input("Ingrese una número: ")
            y = input("Ingrese una número: ")
                
            punto = db.Punto(x,y)
            print(punto)
            print(punto.cuadrante())
            x_2 = input("Ingrese una número: ")
            y_2= input("Ingrese una número: ")
            punto2= db.Punto(x_2,y_2)
            print(punto.vector(punto2))
            print(punto.distancia(punto2))

        elif opcion=='2':
            print("Rectangulo")
            x = input("Ingrese una número: ")
            y = input("Ingrese una número: ")
            punto = db.Punto(x,y)
            x_2 = input("Ingrese una número: ")
            y_2= input("Ingrese una número: ")
            punto2= db.Punto(x_2,y_2)
            rectangulo= db.Rectangulo(punto,punto2)
            print(rectangulo.base_rectangulo())
            print(rectangulo.altura_rectangulo())
            print(rectangulo.area_rectangulo())
