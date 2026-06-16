"""Base del ejercicio del metodo de la potencia inversa."""

from dataclasses import dataclass


@dataclass
class ConfiguracionPotenciaInversa:
    """Agrupa los datos de entrada del ejercicio 2."""

    dimension: int
    tolerancia: float
    max_iteraciones: int


def solicitar_float(mensaje: str) -> float:
    """Solicita un numero real por consola."""
    return float(input(mensaje).strip())


def solicitar_entero(mensaje: str) -> int:
    """Solicita un numero entero por consola."""
    return int(input(mensaje).strip())


def leer_configuracion_potencia_inversa() -> ConfiguracionPotenciaInversa:
    """Lee los parametros base del metodo."""
    print("Ingrese los datos del metodo:")
    dimension = solicitar_entero("Dimension de la matriz: ")
    tolerancia = solicitar_float("Tolerancia: ")
    max_iteraciones = solicitar_entero("Maximo de iteraciones: ")

    return ConfiguracionPotenciaInversa(
        dimension=dimension,
        tolerancia=tolerancia,
        max_iteraciones=max_iteraciones,
    )


def validar_configuracion_potencia_inversa(
    configuracion: ConfiguracionPotenciaInversa,
) -> list[str]:
    """Valida reglas basicas antes de ejecutar el algoritmo."""
    errores: list[str] = []

    if configuracion.dimension <= 0:
        errores.append("La dimension de la matriz debe ser positiva.")

    if configuracion.tolerancia <= 0:
        errores.append("La tolerancia debe ser mayor que cero.")

    if configuracion.max_iteraciones <= 0:
        errores.append("El maximo de iteraciones debe ser un entero positivo.")

    return errores


def mostrar_resumen_potencia_inversa(
    configuracion: ConfiguracionPotenciaInversa,
) -> None:
    """Muestra un resumen de los datos ingresados."""
    print()
    print("Resumen del ejercicio 2")
    print(f"dimension = {configuracion.dimension}")
    print(f"tolerancia = {configuracion.tolerancia}")
    print(f"maximo de iteraciones = {configuracion.max_iteraciones}")


def ejecutar_potencia_inversa() -> None:
    """Punto de entrada temporal para el ejercicio 2."""
    print()
    print("Ejercicio 2: calculo de autovalor y autovector por potencia inversa")

    configuracion = leer_configuracion_potencia_inversa()
    errores = validar_configuracion_potencia_inversa(configuracion)

    if errores:
        print()
        print("No se puede continuar por los siguientes motivos:")
        for error in errores:
            print(f"- {error}")
        return

    mostrar_resumen_potencia_inversa(configuracion)
    print()
    print("Estado actual: flujo de entrada y validacion listos.")
    print("Pendiente: cargar matriz, iterar y estimar autovalor y autovector.")
