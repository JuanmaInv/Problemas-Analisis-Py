# Trabajo Integrador de Analisis Numerico

Proyecto base en Python para desarrollar dos ejercicios:

1. Resolucion de una ecuacion diferencial ordinaria de primer orden mediante Runge-Kutta de cuarto orden.
2. Calculo de un autovalor y su autovector mediante el metodo de la potencia inversa.

## Estado actual

La estructura del proyecto ya esta preparada y actualmente:

- el ejercicio 1 ya resuelve una EDO de primer orden con Runge-Kutta de cuarto orden;
- se muestran las aproximaciones de cada paso en forma tabular;
- se calcula la interpolacion lineal de `y(x)` dentro del intervalo generado;
- el ejercicio 2 ya calcula un autovalor y un autovector con potencia inversa.

## Estructura

- `main.py`: punto de entrada con menu principal.
- `ejercicio1_edo.py`: modulo de Runge-Kutta de orden 4 con interpolacion.
- `ejercicio2_potencia_inversa.py`: modulo de potencia inversa con iteraciones y convergencia.
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

El programa muestra un menu para elegir el ejercicio `1` o `2`.

## Tests

```powershell
python -m unittest discover -s tests
```

En el ejercicio 1 la funcion derivada debe ingresarse como expresion en terminos de `x` e `y`, por ejemplo:

```text
x + y
sin(x) - y / 2
y - x**2 + 1
```

En el ejercicio 2 se debe ingresar:

- la dimension de la matriz;
- la matriz cuadrada por filas;
- un vector inicial no nulo;
- la tolerancia y el maximo de iteraciones.

La implementacion calcula el autovalor de menor magnitud asociado a la matriz, siempre que sea no singular.

## Verificacion paso a paso

Para el ejercicio 1 se puede probar, por ejemplo:

```text
f(x, y) = x + y
x0 = 0
y0 = 1
h = 0.1
pasos = 2
x a interpolar = 0.15
```

La salida mostrara:

- una tabla con `k1`, `k2`, `k3`, `k4` y `y_(i+1)` en cada paso;
- el tramo usado para interpolar;
- el reemplazo numerico de la formula de interpolacion.

Para el ejercicio 2 se puede probar, por ejemplo:

```text
dimension = 2
tolerancia = 0.000001
maximo de iteraciones = 20
matriz =
2 0
0 5
vector inicial =
1
1
```

La salida mostrara:

- el vector anterior de cada iteracion;
- el vector intermedio `z = A^-1 v`;
- el vector normalizado nuevo;
- el autovalor aproximado y el error de convergencia.

Con esos datos, el metodo debe converger hacia el autovalor `2` y hacia un autovector proporcional a `[1, 0]`.

## Dependencias actuales

- `numpy`
- `tabulate`
