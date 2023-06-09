"""Teoría previa

En este ejercicio vas a trabajar el concepto de puntos, coordenadas y vectores sobre el plano cartesiano y cómo la programación Orientada a Objetos 
puede ser una excelente aliada para trabajar con ellos. No está pensado para que hagas ningún tipo de cálculo sino para que practiques la automatización de tareas.

Nota

Creo que es un ejemplo muy interesante, punto de partida en la programación de gráficos, 
pero si consideras que esto no lo tuyo puedes simplemente pasar de largo. Ahora bien, 
debes ser consciente de que te vas a perder uno de los ejercicios más interesantes del curso.

Voy a explicar brevemente los conceptos básicos por si alguien necesita un repaso.

El plano cartesiano

Representa un espacio bidimensional (en 2 dimensiones), formado por dos rectas perpendiculares, 
una horizontal y otra vertical que se cortan en un punto. La recta horizontal se denomina eje de las abscisas o eje X, 
mientras que la vertical recibe el nombre de eje de las ordenadas o simplemente eje Y. En cuanto al punto donde se cortan, 
se conoce como el punto de origen O.


Es importante remarcar que el plano se divide en 4 cuadrantes:


Puntos y coordenadas

El objetivo de todo esto es describir la posición de puntos sobre el plano en forma de coordenadas, 
que se forman asociando el valor del eje de las X (horizontal) con el valor del eje Y (vertical).

La representación de un punto es sencilla: P(X,Y) dónde X y la Y son la distancia horizontal (izquierda o derecha) y 
vertical (arriba o abajo) respectivamente, utilizando como referencia el punto de origen (0,0), justo en el centro del plano.


Vectores en el plano

Finalmente, un vector en el plano hace referencia a un segmento orientado, generado a partir de dos puntos distintos.

A efectos prácticos no deja de ser una línea formada desde un punto inicial en dirección a otro punto final, 
por lo que se entiende que un vector tiene longitud y dirección/sentido.


En esta figura, podemos observar dos puntos A y B que podríamos definir de la siguiente forma:

A(x1, y1) => A(2, 3)
B(x2, y2) => B(5, 5)
Y el vector se representaría como la diferencia entre las coordendas del segundo punto respecto al primero (el segundo menos el primero):

AB = (x2-x1, y2-y1) => (5-2, 5-3) => (3,2)
Lo que en definitiva no deja de ser: 3 a la derecha y 2 arriba.

Y con esto finalizamos este mini repaso.

Ejercicio

Crea una clase llamada Punto con sus dos coordenadas X e Y.
Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será cero.
Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, teniendo en cuenta que si X == 0 e Y != 0 
se sitúa sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.
Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.
(Optativo) Añade un método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla. La fórmula es la siguiente:


Nota

La función raíz cuadrada en Python sqrt() se debe importar del módulo math y utilizarla de la siguiente forma:

import math

math.sqrt(9)

Crea una clase llamada Rectangulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.
Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.
Añade al rectángulo un método llamado base que muestre la base.
Añade al rectángulo un método llamado altura que muestre la altura.
Añade al rectángulo un método llamado area que muestre el area.
Sugerencia

Puedes identificar fácilmente estos valores si intentas dibujar el cuadrado a partir de su diagonal. Si andas perdido, 
prueba de dibujarlo en un papel, ¡seguro que lo verás mucho más claro! Además recuerda que puedes utilizar la función abs() para saber el valor absolute de un número.

Experimentación

Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
Consulta a que cuadrante pertenecen el punto A, C y D.
Consulta los vectores AB y BA.
(Optativo) Consulta la distancia entre los puntos 'A y B' y 'B y A'.
(Optativo) Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0).
Crea un rectángulo utilizando los puntos A y B.
Consulta la base, altura y área del rectángulo.
"""

import math

class Punto:

    def __init__(self,x=0 , y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "El punto de coodernado ({},{})".format(self.x,self.y)


    def cuadrante(self):
        if (self.x > 0 and self.y > 0):
            print("El punto ({}, {}) esta en primer cuadrante".format(self.x , self.y))
        elif (self.x < 0 and self.y < 0):
            print("El punto ({}, {}) esta en tercer cuadrante".format(self.x , self.y))
        elif (self.x < 0 and self.y > 0):
            print("El punto ({}, {}) esta en segundo cuadrante".format(self.x , self.y))
        elif (self.x > 0 and self.y < 0):
            print("El punto ({}, {}) esta en cuarto cuadrante".format(self.x , self.y))
        elif (self.x == 0 and self.y != 0):
            print("El punto ({}, {}) esta en el eje Y".format(self.x , self.y))
        elif (self.x != 0 and self.y ==0):
            print("El punto ({}, {}) esta en el eje X".format(self.x , self.y))
        elif (self.x == 0 and self.y ==0):
            print("El punto ({}, {}) esta en punto de origen".format(self.x , self.y))

    def vector(self , punto):

        resultado_x = punto.x - self.x
        resultado_y = punto.y - self.y
        return "el vector es ({}, {})".format(resultado_x , resultado_y)

    def distancia(self, punto):
        resultado_x = (punto.x - self.x)**2
        resultado_y = (punto.y - self.y)**2
        resultao =round( math.sqrt(resultado_x + resultado_y ),2)
        return "La distancia es {}".format(resultao)
    

punto1= Punto(2,3)
punto2= Punto(5 ,5 )
punto3 = Punto(-3,-1)
punto4 = Punto()
print(punto1.cuadrante())
print(punto3.cuadrante())
print(punto4.cuadrante())


print(punto1.vector(punto2))
print(punto2.vector(punto1))


print(punto1.distancia(punto2))
print(punto2.distancia(punto1))


class Rectangulo:
    def __init__(self,punto_1, punto_2):
        self.punto_1 =punto_1
        self.punto_2 = punto_2

    def base_rectangulo(self):
        base = abs(self.punto_2.x - self.punto_1.x)
        return "la base es {}".format(base)

    def altura_rectangulo(self):
        altura = abs(self.punto_2.y - self.punto_1.y)
        return "La altura es {}".format(altura)

    def area_rectangulo(self):
        area= abs(self.punto_2.x - self.punto_1.x) * abs(self.punto_2.y - self.punto_1.y)
        return "El área de rectangulo son {}".format(area)

rectangulo = Rectangulo(punto1,punto2)

base = rectangulo.base_rectangulo()

altura = rectangulo.altura_rectangulo()

area = rectangulo.area_rectangulo()

