# Test
import unittest
from src.logic.calculadora import Media, DesviacionEstandar
from src.logic.exceptions import NoSePuedeCalcular

class TestCalculadora(unittest.TestCase):

    def test_media_lista_vacia(self):
        media = Media([])
        with self.assertRaises(NoSePuedeCalcular):
            media.calcular_media()

    def test_media_un_elemento(self):
        media = Media([5])
        self.assertEqual(media.calcular_media(), 5)

    def test_dos_elementos_lista(self):
        media = Media([5, 7])
        self.assertEqual(media.calcular_media(), 6)

    def test_n_elementos_positivos(self):
        media = Media([4, 8, 5, 1])
        self.assertEqual(media.calcular_media(), 4.5)

    def test_n_elementos_todos_cero(self):
        media = Media([0, 0, 0, 0, 0])
        self.assertEqual(media.calcular_media(), 0)

    def test_media_positivos_y_negativos(self):
        media = Media([-1, -2, 3, 4])
        self.assertEqual(media.calcular_media(), 1)

    def test_media_elementos_no_numericos(self):
        media = Media([1, 'a', 3])
        with self.assertRaises(TypeError):
            media.calcular_media()

    def test_desviacion_lista_vacia(self):
        desviacionEstandar = DesviacionEstandar([])
        with self.assertRaises(NoSePuedeCalcular):
            desviacionEstandar.calcular()

    def test_desviacion_un_elemento(self):
        desviacionEstandar = DesviacionEstandar([5])
        self.assertEqual(desviacionEstandar.calcular(), 0)

    def test_desviacion_dos_elementos(self):
        desviacionEstandar = DesviacionEstandar([2, 4])
        self.assertAlmostEqual(desviacionEstandar.calcular(), 1.41, places=2)

    def test_desviacion_todos_ceros(self):
        desviacionEstandar = DesviacionEstandar([0, 0, 0, 0])
        self.assertEqual(desviacionEstandar.calcular(), 0)

    def test_desviacion_n_elementos_positivos(self):
        desviacionEstandar = DesviacionEstandar([1, 5, 8, 9])
        self.assertAlmostEqual(desviacionEstandar.calcular(), 3.59, places=2)

    def test_desviacion_no_numerico_type_error(self):
        desviacionEstandar = DesviacionEstandar([-1, "a", 4])
        with self.assertRaises(TypeError):
            desviacionEstandar.calcular()
    def test_desviacion_positivos_y_negativos(self):
        desviacionEstandar = DesviacionEstandar([-1, -2, 3, 4])
        self.assertAlmostEqual(desviacionEstandar.calcular(), 2.94, places=2)


if __name__ == '__main__':
    unittest.main()
