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

## Puesta en marcha en una PC recien clonada

Si alguien clona el proyecto por primera vez, estos son los pasos recomendados para dejarlo listo y ejecutarlo.

### 1. Entrar a la carpeta del proyecto

```powershell
cd C:\ruta\al\proyecto
```

### 2. Crear el entorno virtual

```powershell
python -m venv .venv
```

### 3. Activar el entorno virtual en PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la ejecucion de scripts, se puede habilitar solo para la sesion actual con:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\.venv\Scripts\Activate.ps1
```

### 4. Actualizar `pip`

```powershell
python -m pip install --upgrade pip
```

### 5. Instalar las dependencias

```powershell
python -m pip install -r requirements.txt
```

### 6. Ejecutar el programa

```powershell
python main.py
```

El programa muestra un menu para elegir el ejercicio `1` o `2`.

### 7. Ejecutar los tests

```powershell
python -m unittest discover -s tests
```

Si el comando `python` no funciona en la PC, se puede probar con `py` en los mismos pasos.

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

- una tabla con `x_i`, `y_i`, `k1`, `k2`, `k3`, `k4` y `y_(i+1)` en cada paso;
- `x_i` es el valor actual de `x` en el paso `i`;
- `y_i` es la aproximacion actual de `y(x_i)`;
- `k1`, `k2`, `k3` y `k4` son las pendientes intermedias que calcula Runge-Kutta de cuarto orden;
- `y_(i+1)` es la nueva aproximacion de `y` en el siguiente paso.

En cada paso se calcula:

```text
k1 = h * f(x_i, y_i)
k2 = h * f(x_i + h/2, y_i + k1/2)
k3 = h * f(x_i + h/2, y_i + k2/2)
k4 = h * f(x_i + h, y_i + k3)
```

Luego se obtiene el siguiente valor aproximado con:

```text
y_(i+1) = y_i + (k1 + 2k2 + 2k3 + k4) / 6
```

Esto significa que el metodo no usa una sola pendiente, sino un promedio ponderado de cuatro pendientes para lograr una aproximacion mas precisa.

- el tramo usado para interpolar;
- el reemplazo numerico de la formula de interpolacion.

Para el ejercicio 2 se puede probar, por ejemplo:
dimension = 2
tolerancia = 0.000001
maximo de iteraciones = 20
matriz =
2 0
0 5
vector inicial =
1
1

La salida mostrara:
Las 20 iteraciones con
el v anterior (es el vector con el que el método empieza esa fila)
el z (que se calcula de Az=v, despejano la z dado que tengo el valor de A y de v)
el v nuevo
el autovalor
el error

- el vector anterior de cada iteracion;
- el vector intermedio `z = A^-1 v`;
- el vector normalizado nuevo;
- el autovalor aproximado y el error de convergencia.

Con esos datos, el metodo debe converger hacia el autovalor `2` y hacia un autovector proporcional a `[1, 0]`.

## Dependencias actuales

- `numpy`
- `tabulate`
