import math
import unittest

from ejercicio1_edo import (
    ConfiguracionEDO,
    calcular_aproximaciones_rk4,
    crear_funcion_derivada,
    interpolar_valor,
    validar_configuracion_edo,
)


class EjercicioEDOTests(unittest.TestCase):
    def test_valida_intervalo_de_interpolacion(self) -> None:
        configuracion = ConfiguracionEDO(
            expresion_derivada="x + y",
            x_inicial=0.0,
            y_inicial=1.0,
            paso=0.1,
            cantidad_pasos=2,
            x_interpolacion=0.5,
        )

        errores = validar_configuracion_edo(configuracion)

        self.assertIn(
            "El valor a interpolar debe quedar dentro del intervalo calculado.",
            errores,
        )

    def test_runge_kutta_aproxima_solucion_conocida(self) -> None:
        configuracion = ConfiguracionEDO(
            expresion_derivada="y",
            x_inicial=0.0,
            y_inicial=1.0,
            paso=0.1,
            cantidad_pasos=10,
            x_interpolacion=1.0,
        )
        derivada = crear_funcion_derivada(configuracion.expresion_derivada)

        pasos = calcular_aproximaciones_rk4(configuracion, derivada)

        self.assertAlmostEqual(pasos[-1].y, math.e, places=4)

    def test_interpolacion_lineal_devuelve_valor_entre_pasos(self) -> None:
        configuracion = ConfiguracionEDO(
            expresion_derivada="y",
            x_inicial=0.0,
            y_inicial=1.0,
            paso=0.5,
            cantidad_pasos=2,
            x_interpolacion=0.25,
        )
        derivada = crear_funcion_derivada(configuracion.expresion_derivada)
        pasos = calcular_aproximaciones_rk4(configuracion, derivada)

        valor = interpolar_valor(pasos, 0.25)

        self.assertGreater(valor, pasos[0].y)
        self.assertLess(valor, pasos[1].y)


if __name__ == "__main__":
    unittest.main()
