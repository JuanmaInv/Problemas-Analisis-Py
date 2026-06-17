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

## Datos de entrada

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
k1 = f(x_i, y_i)
k2 = f(x_i + h/2, y_i + h*k1/2)
k3 = f(x_i + h/2, y_i + h*k2/2)
k4 = f(x_i + h, y_i + h*k3)
```

Luego se obtiene el siguiente valor aproximado con:

```text
y_(i+1) = y_i + h * (k1 + 2k2 + 2k3 + k4) / 6
```

Esto significa que el metodo no usa una sola pendiente, sino un promedio ponderado de cuatro pendientes para lograr una aproximacion mas precisa.

Despues de calcular la tabla, el programa usa los puntos generados para interpolar el valor pedido. Si `x = 0.15`, toma el tramo entre `0.1` y `0.2` y aplica interpolacion lineal:

```text
y(x) = y_i + ((x - x_i) / (x_(i+1) - x_i)) * (y_(i+1) - y_i)
```

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
- el vector intermedio `z = A^-1 v`, que en la practica se obtiene resolviendo `A z = v`;
- el vector normalizado nuevo;
- el autovalor aproximado y el error de convergencia.

Con esos datos, el metodo debe converger hacia el autovalor `2` y hacia un autovector proporcional a `[1, 0]`.

## Casos de prueba sugeridos

Estos son los dos ejercicios resueltos del archivo de ejemplo `ejercicios-ejemplo-analisis.pdf` y sirven para que cualquier docente o revisor pueda probar rapidamente el programa.

### Caso de prueba 1: EDO con Runge-Kutta e interpolacion

Ingresar:

```text
f(x, y) = x + y
x0 = 0
y0 = 1
h = 0.1
pasos = 2
x a interpolar = 0.15
```

Resultado esperado:

- la tabla debe incluir los nodos `y(0.1) ~= 1.110342` y `y(0.2) ~= 1.242805`;
- en el paso 0 deben obtenerse `k1 = 1`, `k2 = 1.1`, `k3 = 1.105`, `k4 = 1.2105`;
- el siguiente valor del paso 0 debe ser `y1 = 1.110341666...`;
- la interpolacion lineal debe dar `y(0.15) ~= 1.176573`.

### Caso de prueba 2: Potencia inversa

Ingresar:

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

Resultado esperado:

- el vector inicial se normaliza a `v0 = [0.70710678, 0.70710678]`;
- en la primera iteracion se resuelve `A z = v0`, por lo que `z = [0.35355339, 0.14142136]`;
- el vector nuevo de la primera iteracion debe ser `v1 = [0.92847669, 0.37139068]`;
- el autovalor aproximado de la primera iteracion debe ser `2.41379310`;
- el error de la primera iteracion debe ser `0.40213174`;
- al continuar las iteraciones, el metodo debe converger al autovalor `2` y a un autovector proporcional a `[1, 0]`.

## Dependencias actuales

- `numpy`
- `tabulate`
