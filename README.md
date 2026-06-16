# Trabajo Integrador de Analisis Numerico

Proyecto base en Python para desarrollar dos ejercicios:

1. Resolucion de una ecuacion diferencial ordinaria de primer orden mediante Runge-Kutta de cuarto orden.
2. Calculo de un autovalor y su autovector mediante el metodo de la potencia inversa.

## Estado actual

La estructura del proyecto ya esta preparada y actualmente:

- el ejercicio 1 ya resuelve una EDO de primer orden con Runge-Kutta de cuarto orden;
- se muestran las aproximaciones de cada paso en forma tabular;
- se calcula la interpolacion lineal de `y(x)` dentro del intervalo generado;
- el ejercicio 2 conserva su flujo base de entrada y validaciones.

## Estructura

- `main.py`: punto de entrada con menu principal.
- `ejercicio1_edo.py`: modulo de Runge-Kutta de orden 4 con interpolacion.
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

En el ejercicio 1 la funcion derivada debe ingresarse como expresion en terminos de `x` e `y`, por ejemplo:

```text
x + y
sin(x) - y / 2
y - x**2 + 1
```

## Dependencias actuales

- `numpy`
- `tabulate`

`tabulate` sera util cuando se agregue la salida tabular de las aproximaciones numericas.
