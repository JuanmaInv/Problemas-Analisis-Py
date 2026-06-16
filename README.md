# Trabajo Integrador de Analisis Numerico

Proyecto base en Python para desarrollar dos ejercicios:

1. Resolucion de una ecuacion diferencial ordinaria de primer orden mediante Runge-Kutta de cuarto orden.
2. Calculo de un autovalor y su autovector mediante el metodo de la potencia inversa.

## Estado actual

La estructura del proyecto ya esta preparada, pero los algoritmos todavia no fueron implementados.

## Estructura

- `main.py`: punto de entrada con menu principal.
- `ejercicio1_edo.py`: modulo reservado para el ejercicio de EDO e interpolacion.
- `ejercicio2_potencia_inversa.py`: modulo reservado para el ejercicio de potencia inversa.
- `requirements.txt`: dependencias del proyecto.

## Entorno virtual

El proyecto usa un entorno virtual local en `.venv`.

### Activacion en PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

## Instalacion de dependencias

```powershell
python -m pip install -r requirements.txt
```

## Ejecucion

```powershell
python main.py
```

## Dependencias actuales

- `numpy`
- `tabulate`

`tabulate` sera util cuando se agregue la salida tabular de las aproximaciones numericas.
