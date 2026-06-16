"""Base del ejercicio de EDO con Runge-Kutta de orden 4."""

from dataclasses import dataclass


@dataclass
class ConfiguracionEDO:
    """Agrupa los datos de entrada del ejercicio 1."""

    x_inicial: float
    y_inicial: float
    paso: float
    cantidad_pasos: int
    x_interpolacion: float


def solicitar_float(mensaje: str) -> float:
    """Solicita un numero real por consola."""
    return float(input(mensaje).strip())


def solicitar_entero(mensaje: str) -> int:
    """Solicita un numero entero por consola."""
    return int(input(mensaje).strip())


def leer_configuracion_edo() -> ConfiguracionEDO:
    """Lee por consola los parametros base del problema."""
    print("Ingrese los datos iniciales del problema:")
    x_inicial = solicitar_float("x0: ")
    y_inicial = solicitar_float("y0: ")
    paso = solicitar_float("Paso h: ")
    cantidad_pasos = solicitar_entero("Cantidad de pasos: ")
    x_interpolacion = solicitar_float("Valor de x para interpolar: ")

    return ConfiguracionEDO(
        x_inicial=x_inicial,
        y_inicial=y_inicial,
        paso=paso,
        cantidad_pasos=cantidad_pasos,
        x_interpolacion=x_interpolacion,
    )


def validar_configuracion_edo(configuracion: ConfiguracionEDO) -> list[str]:
    """Valida reglas basicas antes de ejecutar el algoritmo."""
    errores: list[str] = []

    if configuracion.paso <= 0:
        errores.append("El paso h debe ser mayor que cero.")

    if configuracion.cantidad_pasos <= 0:
        errores.append("La cantidad de pasos debe ser un entero positivo.")

    return errores


def mostrar_resumen_edo(configuracion: ConfiguracionEDO) -> None:
    """Muestra un resumen de los datos ingresados."""
    print()
    print("Resumen del ejercicio 1")
    print(f"x0 = {configuracion.x_inicial}")
    print(f"y0 = {configuracion.y_inicial}")
    print(f"h = {configuracion.paso}")
    print(f"pasos = {configuracion.cantidad_pasos}")
    print(f"x a interpolar = {configuracion.x_interpolacion}")


def ejecutar_ejercicio_edo() -> None:
    """Punto de entrada temporal para el ejercicio 1."""
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

    mostrar_resumen_edo(configuracion)
    print()
    print("Estado actual: flujo de entrada y validacion listos.")
    print("Pendiente: implementar Runge-Kutta, tabla de aproximaciones e interpolacion.")
