
import helpers
import unittest
import ejercicio1 as db


class TestDatabase(unittest.TestCase):



    def test_cuadrante(self):
        punto1= db.Punto(2,3)
        punto2= db.Punto(-5 ,5)
        punto3 = db.Punto(-3,-1)
        punto4 = db.Punto()
        punto5 = db.Punto(0,3)
        punto6=  db.Punto(4,0)
        punto7 = db.Punto(2,-5)
        self.assertEqual(punto1.cuadrante(),"El punto (2, 3) esta en primer cuadrante")
        self.assertEqual(punto2.cuadrante(), "El punto (-5, 5) esta en primer cuadrante")
        self.assertEqual(punto3.cuadrante(), "El punto (-3, -1) esta en tercer cuadrante")
        self.assertEqual(punto7.cuadrante(), "El punto (2, -5) esta en cuatro cuadrante")
        self.assertEqual(punto4.cuadrante(), "El punto (0, 0) esta en punto de origen")
        self.assertEqual(punto5.cuadrante(), "El punto (0, 3) esta en el eje Y")
        self.assertEqual(punto6.cuadrante(), "El punto (2, 0) esta en el eje X")


    def test_vector(self):
        punto1= db.Punto(2,3)
        punto2= db.Punto(-5 ,5)
        self.assertEqual(punto1.vector(punto2), "el vector  es (-7, 2)")

    def test_distancia(self):
        punto1= db.Punto(2,3)
        punto2= db.Punto(-5 ,5)
        self.assertEqual(punto1.distancia(punto2),"La distancia es 7.28 ")

    def test_base(self):
        punto1= db.Punto(2,3)
        punto2= db.Punto(-5 ,5)
        rectangulo= db.Rectangulo(punto1,punto2)
        self.assertEqual(rectangulo.base_rectangulo(), "La base es 7")

    def test_altura(self):
        punto1= db.Punto(2,3)
        punto2= db.Punto(-5 ,5)
        rectangulo= db.Rectangulo(punto1,punto2)
        self.assertEqual(rectangulo.altura_rectangulo(), "La base es 2")

    def test_area_rectangulo(self):
        punto1= db.Punto(2,3)
        punto2= db.Punto(-5 ,5)
        rectangulo= db.Rectangulo(punto1,punto2)
        self.assertEqual(rectangulo.area_rectangulo(), "La base es 14")
