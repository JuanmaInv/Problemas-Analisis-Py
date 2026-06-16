import unittest

import numpy as np

from ejercicio2_potencia_inversa import (
    metodo_potencia_inversa,
    validar_matriz_y_vector,
)


class EjercicioPotenciaInversaTests(unittest.TestCase):
    def test_detecta_vector_inicial_nulo(self) -> None:
        matriz = np.array([[2.0, 0.0], [0.0, 5.0]])
        vector = np.array([0.0, 0.0])

        errores = validar_matriz_y_vector(matriz, vector)

        self.assertIn("El vector inicial no puede ser nulo.", errores)

    def test_detecta_matriz_singular(self) -> None:
        matriz = np.array([[1.0, 2.0], [2.0, 4.0]])
        vector = np.array([1.0, 0.0])

        errores = validar_matriz_y_vector(matriz, vector)

        self.assertIn(
            "La matriz no debe ser singular para aplicar potencia inversa.",
            errores,
        )

    def test_converge_al_autovalor_de_menor_magnitud(self) -> None:
        matriz = np.array([[2.0, 0.0], [0.0, 5.0]])
        vector = np.array([1.0, 1.0])

        autovalor, autovector, historial, convergio = metodo_potencia_inversa(
            matriz=matriz,
            vector_inicial=vector,
            tolerancia=1e-6,
            max_iteraciones=20,
        )

        self.assertTrue(convergio)
        self.assertAlmostEqual(autovalor, 2.0, places=6)
        self.assertAlmostEqual(abs(float(autovector[0])), 1.0, places=6)
        self.assertGreater(len(historial), 0)


if __name__ == "__main__":
    unittest.main()
