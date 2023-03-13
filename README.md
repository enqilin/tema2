# tema2

## Instalar las dependencias

_Nota: Sólo incluye pytest para realizar pruebas unitarias._

```bash
pip install -r requirements.txt
```

## Para probar el programa en modo gráfico

```bash
python run.py
```

## Para probar el programa en modo terminal

```bash
python run.py -t
```

## Para ejecutar las pruebas unitarias

```bash
pytest -v
```
Punto
```bash
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
    

```


Rectangulo

```bash
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
```
