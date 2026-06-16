# Trabajo Integrador de Analisis Numerico

Proyecto base en Python para desarrollar dos ejercicios:

1. Resolucion de una ecuacion diferencial ordinaria de primer orden mediante Runge-Kutta de cuarto orden.
2. Calculo de un autovalor y su autovector mediante el metodo de la potencia inversa.

## Estado actual

La estructura del proyecto ya esta preparada y ambos ejercicios cuentan con:

- punto de entrada desde el menu principal;
- lectura de datos por consola;
- validaciones iniciales;
- resumen de parametros ingresados.

Los algoritmos numericos todavia no fueron implementados.

## Estructura

- `main.py`: punto de entrada con menu principal.
- `ejercicio1_edo.py`: modulo base para EDO, entrada de datos y validaciones.
- `ejercicio2_potencia_inversa.py`: modulo base para potencia inversa, entrada de datos y validaciones.
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
