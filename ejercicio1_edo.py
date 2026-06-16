"""Base del ejercicio de EDO con Runge-Kutta de orden 4."""

from dataclasses import dataclass
import math
from typing import Callable

from tabulate import tabulate


@dataclass
class ConfiguracionEDO:
    """Agrupa los datos de entrada del ejercicio 1."""

    expresion_derivada: str
    x_inicial: float
    y_inicial: float
    paso: float
    cantidad_pasos: int
    x_interpolacion: float


@dataclass
class PasoRK4:
    """Representa una fila de resultados del metodo."""

    iteracion: int
    x: float
    y: float
    k1: float
    k2: float
    k3: float
    k4: float
    y_siguiente: float


def solicitar_float(mensaje: str) -> float:
    """Solicita un numero real por consola."""
    return float(input(mensaje).strip())


def solicitar_entero(mensaje: str) -> int:
    """Solicita un numero entero por consola."""
    return int(input(mensaje).strip())


def leer_configuracion_edo() -> ConfiguracionEDO:
    """Lee por consola los parametros base del problema."""
    print("Ingrese los datos iniciales del problema:")
    expresion_derivada = input("f(x, y) = ").strip()
    x_inicial = solicitar_float("x0: ")
    y_inicial = solicitar_float("y0: ")
    paso = solicitar_float("Paso h: ")
    cantidad_pasos = solicitar_entero("Cantidad de pasos: ")
    x_interpolacion = solicitar_float("Valor de x para interpolar: ")

    return ConfiguracionEDO(
        expresion_derivada=expresion_derivada,
        x_inicial=x_inicial,
        y_inicial=y_inicial,
        paso=paso,
        cantidad_pasos=cantidad_pasos,
        x_interpolacion=x_interpolacion,
    )


def validar_configuracion_edo(configuracion: ConfiguracionEDO) -> list[str]:
    """Valida reglas basicas antes de ejecutar el algoritmo."""
    errores: list[str] = []

    if not configuracion.expresion_derivada:
        errores.append("La funcion f(x, y) no puede estar vacia.")

    if configuracion.paso <= 0:
        errores.append("El paso h debe ser mayor que cero.")

    if configuracion.cantidad_pasos <= 0:
        errores.append("La cantidad de pasos debe ser un entero positivo.")

    x_final = configuracion.x_inicial + configuracion.paso * configuracion.cantidad_pasos
    if not configuracion.x_inicial <= configuracion.x_interpolacion <= x_final:
        errores.append("El valor a interpolar debe quedar dentro del intervalo calculado.")

    return errores


def crear_funcion_derivada(expresion: str) -> Callable[[float, float], float]:
    """Crea una funcion evaluable a partir de una expresion en x e y."""
    entorno = {nombre: getattr(math, nombre) for nombre in dir(math) if not nombre.startswith("_")}
    entorno["abs"] = abs

    def funcion(x: float, y: float) -> float:
        variables = {"x": x, "y": y}
        return float(eval(expresion, {"__builtins__": {}}, entorno | variables))

    return funcion


def calcular_aproximaciones_rk4(
    configuracion: ConfiguracionEDO,
    derivada: Callable[[float, float], float],
) -> list[PasoRK4]:
    """Calcula las aproximaciones del metodo de Runge-Kutta de orden 4."""
    pasos: list[PasoRK4] = []
    x_actual = configuracion.x_inicial
    y_actual = configuracion.y_inicial
    h = configuracion.paso

    for iteracion in range(configuracion.cantidad_pasos + 1):
        if iteracion == 0:
            pasos.append(
                PasoRK4(
                    iteracion=iteracion,
                    x=x_actual,
                    y=y_actual,
                    k1=0.0,
                    k2=0.0,
                    k3=0.0,
                    k4=0.0,
                    y_siguiente=y_actual,
                )
            )
            continue

        x_previo = x_actual
        y_previo = y_actual
        k1 = derivada(x_previo, y_previo)
        k2 = derivada(x_previo + h / 2, y_previo + h * k1 / 2)
        k3 = derivada(x_previo + h / 2, y_previo + h * k2 / 2)
        k4 = derivada(x_previo + h, y_previo + h * k3)
        y_actual = y_previo + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x_actual = x_previo + h

        pasos.append(
            PasoRK4(
                iteracion=iteracion,
                x=x_actual,
                y=y_actual,
                k1=k1,
                k2=k2,
                k3=k3,
                k4=k4,
                y_siguiente=y_actual,
            )
        )

    return pasos


def interpolar_valor(pasos: list[PasoRK4], x_objetivo: float) -> float:
    """Interpola linealmente y(x) a partir de las aproximaciones calculadas."""
    for paso in pasos:
        if math.isclose(paso.x, x_objetivo, rel_tol=1e-9, abs_tol=1e-9):
            return paso.y

    for indice in range(1, len(pasos)):
        paso_izquierdo = pasos[indice - 1]
        paso_derecho = pasos[indice]

        if paso_izquierdo.x <= x_objetivo <= paso_derecho.x:
            proporcion = (x_objetivo - paso_izquierdo.x) / (paso_derecho.x - paso_izquierdo.x)
            return paso_izquierdo.y + proporcion * (paso_derecho.y - paso_izquierdo.y)

    raise ValueError("No fue posible interpolar el valor solicitado.")


def mostrar_tabla_aproximaciones(pasos: list[PasoRK4]) -> None:
    """Muestra la tabla de iteraciones del metodo."""
    filas = [
        [
            paso.iteracion,
            f"{paso.x:.6f}",
            f"{paso.y:.6f}",
            f"{paso.k1:.6f}",
            f"{paso.k2:.6f}",
            f"{paso.k3:.6f}",
            f"{paso.k4:.6f}",
            f"{paso.y_siguiente:.6f}",
        ]
        for paso in pasos
    ]
    encabezados = ["i", "x_i", "y_i", "k1", "k2", "k3", "k4", "y_(i+1)"]
    print()
    print(tabulate(filas, headers=encabezados, tablefmt="grid"))


def mostrar_detalle_interpolacion(pasos: list[PasoRK4], x_objetivo: float) -> None:
    """Muestra el tramo usado para interpolar y el calculo aplicado."""
    for paso in pasos:
        if math.isclose(paso.x, x_objetivo, rel_tol=1e-9, abs_tol=1e-9):
            print()
            print("Detalle de interpolacion")
            print("El valor solicitado coincide exactamente con un nodo calculado.")
            print(f"y({x_objetivo}) = {paso.y:.6f}")
            return

    for indice in range(1, len(pasos)):
        paso_izquierdo = pasos[indice - 1]
        paso_derecho = pasos[indice]

        if paso_izquierdo.x <= x_objetivo <= paso_derecho.x:
            proporcion = (x_objetivo - paso_izquierdo.x) / (paso_derecho.x - paso_izquierdo.x)
            valor_interpolado = paso_izquierdo.y + proporcion * (paso_derecho.y - paso_izquierdo.y)
            print()
            print("Detalle de interpolacion")
            print(
                f"Se usa el tramo [{paso_izquierdo.x:.6f}, {paso_derecho.x:.6f}] "
                f"con y = [{paso_izquierdo.y:.6f}, {paso_derecho.y:.6f}]"
            )
            print(
                "Formula: y(x) = y_i + ((x - x_i) / (x_(i+1) - x_i)) * (y_(i+1) - y_i)"
            )
            print(
                f"Reemplazo: y({x_objetivo}) = {paso_izquierdo.y:.6f} + "
                f"(({x_objetivo:.6f} - {paso_izquierdo.x:.6f}) / "
                f"({paso_derecho.x:.6f} - {paso_izquierdo.x:.6f})) * "
                f"({paso_derecho.y:.6f} - {paso_izquierdo.y:.6f})"
            )
            print(f"Resultado interpolado = {valor_interpolado:.6f}")
            return


def mostrar_resumen_edo(configuracion: ConfiguracionEDO) -> None:
    """Muestra un resumen de los datos ingresados."""
    print()
    print("Resumen del ejercicio 1")
    print(f"f(x, y) = {configuracion.expresion_derivada}")
    print(f"x0 = {configuracion.x_inicial}")
    print(f"y0 = {configuracion.y_inicial}")
    print(f"h = {configuracion.paso}")
    print(f"pasos = {configuracion.cantidad_pasos}")
    print(f"x a interpolar = {configuracion.x_interpolacion}")


def ejecutar_ejercicio_edo() -> None:
    """Punto de entrada del ejercicio 1."""
    print()
    print("Ejercicio 1: EDO de primer orden con Runge-Kutta de orden 4")

    configuracion = leer_configuracion_edo()
    errores = validar_configuracion_edo(configuracion)

    if errores:
        print()
        print("No se puede continuar por los siguientes motivos:")
        for error in errores:
            print(f"- {error}")
        return

    try:
        derivada = crear_funcion_derivada(configuracion.expresion_derivada)
        derivada(configuracion.x_inicial, configuracion.y_inicial)
    except Exception as error:
        print()
        print("No se pudo interpretar la funcion ingresada.")
        print(f"Detalle: {error}")
        return

    mostrar_resumen_edo(configuracion)
    pasos = calcular_aproximaciones_rk4(configuracion, derivada)
    mostrar_tabla_aproximaciones(pasos)
    valor_interpolado = interpolar_valor(pasos, configuracion.x_interpolacion)
    mostrar_detalle_interpolacion(pasos, configuracion.x_interpolacion)

    print()
    print(f"Interpolacion: y({configuracion.x_interpolacion}) = {valor_interpolado:.6f}")
