"""Implementacion del metodo de la potencia inversa."""

from dataclasses import dataclass

import numpy as np
from tabulate import tabulate


@dataclass
class ConfiguracionPotenciaInversa:
    """Agrupa los datos de entrada del ejercicio 2."""

    dimension: int
    tolerancia: float
    max_iteraciones: int


@dataclass
class IteracionPotenciaInversa:
    """Representa una iteracion del metodo."""

    iteracion: int
    vector_anterior: np.ndarray
    solucion_intermedia: np.ndarray
    vector_normalizado: np.ndarray
    autovalor_aprox: float
    error_vector: float


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


def leer_vector(dimension: int, mensaje: str) -> np.ndarray:
    """Lee un vector de la dimension indicada."""
    print(mensaje)
    componentes = [
        solicitar_float(f"Componente {indice + 1}: ")
        for indice in range(dimension)
    ]
    return np.array(componentes, dtype=float)


def leer_matriz(dimension: int) -> np.ndarray:
    """Lee una matriz cuadrada por filas."""
    print("Ingrese la matriz por filas.")
    filas: list[list[float]] = []

    for indice in range(dimension):
        fila_texto = input(
            f"Fila {indice + 1} ({dimension} valores separados por espacio): "
        ).strip()
        fila = [float(valor) for valor in fila_texto.split()]

        if len(fila) != dimension:
            raise ValueError(
                f"La fila {indice + 1} debe tener exactamente {dimension} valores."
            )

        filas.append(fila)

    return np.array(filas, dtype=float)


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


def validar_matriz_y_vector(matriz: np.ndarray, vector: np.ndarray) -> list[str]:
    """Valida la consistencia de la matriz y el vector inicial."""
    errores: list[str] = []

    if matriz.shape[0] != matriz.shape[1]:
        errores.append("La matriz debe ser cuadrada.")

    if vector.ndim != 1 or vector.shape[0] != matriz.shape[0]:
        errores.append("El vector inicial debe tener la misma dimension que la matriz.")

    if np.linalg.norm(vector) == 0:
        errores.append("El vector inicial no puede ser nulo.")

    try:
        determinante = float(np.linalg.det(matriz))
        if np.isclose(determinante, 0.0):
            errores.append("La matriz no debe ser singular para aplicar potencia inversa.")
    except np.linalg.LinAlgError:
        errores.append("No fue posible analizar la matriz ingresada.")

    return errores


def normalizar_vector(vector: np.ndarray) -> np.ndarray:
    """Devuelve el vector normalizado con norma euclidea."""
    norma = np.linalg.norm(vector)
    if np.isclose(norma, 0.0):
        raise ValueError("No se puede normalizar un vector nulo.")
    return vector / norma


def calcular_error_vectores(actual: np.ndarray, anterior: np.ndarray) -> float:
    """Calcula el cambio entre dos vectores contemplando cambio de signo."""
    return min(
        float(np.linalg.norm(actual - anterior)),
        float(np.linalg.norm(actual + anterior)),
    )


def metodo_potencia_inversa(
    matriz: np.ndarray,
    vector_inicial: np.ndarray,
    tolerancia: float,
    max_iteraciones: int,
) -> tuple[float, np.ndarray, list[IteracionPotenciaInversa], bool]:
    """Ejecuta el metodo de la potencia inversa."""
    vector_actual = normalizar_vector(vector_inicial)
    historial: list[IteracionPotenciaInversa] = []
    convergio = False
    autovalor_aprox = 0.0

    for iteracion in range(1, max_iteraciones + 1):
        solucion = np.linalg.solve(matriz, vector_actual)
        vector_siguiente = normalizar_vector(solucion)
        autovalor_aprox = float(vector_siguiente @ (matriz @ vector_siguiente))
        error_vector = calcular_error_vectores(vector_siguiente, vector_actual)

        historial.append(
            IteracionPotenciaInversa(
                iteracion=iteracion,
                vector_anterior=vector_actual.copy(),
                solucion_intermedia=solucion.copy(),
                vector_normalizado=vector_siguiente.copy(),
                autovalor_aprox=autovalor_aprox,
                error_vector=error_vector,
            )
        )

        vector_actual = vector_siguiente
        if error_vector < tolerancia:
            convergio = True
            break

    return autovalor_aprox, vector_actual, historial, convergio


def mostrar_tabla_iteraciones(historial: list[IteracionPotenciaInversa]) -> None:
    """Muestra las iteraciones del metodo en formato tabular."""
    filas = [
        [
            iteracion.iteracion,
            np.array2string(iteracion.vector_anterior, precision=6, suppress_small=True),
            np.array2string(iteracion.solucion_intermedia, precision=6, suppress_small=True),
            np.array2string(iteracion.vector_normalizado, precision=6, suppress_small=True),
            f"{iteracion.autovalor_aprox:.8f}",
            f"{iteracion.error_vector:.8e}",
        ]
        for iteracion in historial
    ]
    print()
    print(
        tabulate(
            filas,
            headers=["i", "v anterior", "z = A^-1 v", "v nuevo", "autovalor", "error"],
            tablefmt="grid",
        )
    )


def mostrar_resultado_final(
    autovalor: float,
    autovector: np.ndarray,
    convergio: bool,
    iteraciones_realizadas: int,
) -> None:
    """Muestra el resultado final del metodo."""
    print()
    print("Resultado final")
    print(f"Autovalor aproximado = {autovalor:.8f}")
    print(f"Autovector aproximado = {np.array2string(autovector, precision=6)}")
    print(f"Iteraciones realizadas = {iteraciones_realizadas}")
    print(f"Convergencia alcanzada = {'si' if convergio else 'no'}")
    if not convergio:
        print("Aviso: no se alcanzo la tolerancia pedida. Conviene aumentar las iteraciones.")


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
    """Punto de entrada del ejercicio 2."""
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

    try:
        matriz = leer_matriz(configuracion.dimension)
        vector_inicial = leer_vector(
            configuracion.dimension,
            "Ingrese el vector inicial:",
        )
    except ValueError as error:
        print()
        print("No se pudieron leer correctamente los datos numericos.")
        print(f"Detalle: {error}")
        return

    errores_datos = validar_matriz_y_vector(matriz, vector_inicial)
    if errores_datos:
        print()
        print("No se puede continuar por los siguientes motivos:")
        for error in errores_datos:
            print(f"- {error}")
        return

    print()
    mostrar_resumen_potencia_inversa(configuracion)
    print("Matriz ingresada:")
    print(matriz)
    print("Vector inicial:")
    print(vector_inicial)

    try:
        autovalor, autovector, historial, convergio = metodo_potencia_inversa(
            matriz=matriz,
            vector_inicial=vector_inicial,
            tolerancia=configuracion.tolerancia,
            max_iteraciones=configuracion.max_iteraciones,
        )
    except np.linalg.LinAlgError as error:
        print()
        print("No fue posible ejecutar el metodo de la potencia inversa.")
        print(f"Detalle: {error}")
        return

    mostrar_tabla_iteraciones(historial)
    mostrar_resultado_final(
        autovalor=autovalor,
        autovector=autovector,
        convergio=convergio,
        iteraciones_realizadas=len(historial),
    )
