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
