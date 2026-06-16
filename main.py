"""Punto de entrada del Trabajo Integrador de Analisis Numerico."""

from ejercicio1_edo import ejecutar_ejercicio_edo
from ejercicio2_potencia_inversa import ejecutar_potencia_inversa


def mostrar_menu() -> None:
    """Muestra las opciones disponibles del proyecto."""
    print("=" * 55)
    print("TRABAJO INTEGRADOR DE ANALISIS NUMERICO")
    print("=" * 55)
    print("1. Resolucion de una EDO e interpolacion")
    print("2. Metodo de la potencia inversa")
    print("0. Salir")


def main() -> None:
    """Coordina la navegacion principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            ejecutar_ejercicio_edo()
        elif opcion == "2":
            ejecutar_potencia_inversa()
        elif opcion == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opcion invalida. Intente nuevamente.")

        print()


if __name__ == "__main__":
    main()
