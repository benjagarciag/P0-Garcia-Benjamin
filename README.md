# P0-Garcia-Benjamin

## Propósito del proyecto

Implementar desde cero una función de multiplicación de matrices (`mimatmul`),
verificar su correctitud con pruebas automáticas y comparar su rendimiento con
NumPy mediante un benchmark que genera datos y un gráfico de rendimiento.

## Sistema operativo

Windows 10 (64 bits)

## Versión de Python

3.14.7

## Ambiente virtual

Crear el ambiente virtual:

```powershell
python -m venv .venv
```

Activar el ambiente virtual:

```powershell
.venv\Scripts\activate
```

Instalar las dependencias:

```powershell
pip install -r requirements.txt
```

## Ejecutar las pruebas

```powershell
pytest
```

## Ejecutar el benchmark y el gráfico

Genera los datos CSV del benchmark:

```powershell
python -m src.benchmark
```

Genera el gráfico de rendimiento a partir del CSV:

```powershell
python -m src.grafico
```

## Resultados del benchmark

Se midió `mimatmul` contra `numpy.matmul` con matrices cuadradas aleatorias
de varios tamaños en este computador. Cada medición verifica primero que ambos
resultados coincidan. Datos completos en `data/benchmark.csv` y gráfico en
`data/grafico_rendimiento.png`.

| Tamaño (n×n) | mimatmul (s) | NumPy (s) | Vez más rápida NumPy |
|---|---|---|---|
| 2 | 0.000007 | 0.000006 | 1.1× |
| 4 | 0.000012 | 0.000004 | 3.0× |
| 8 | 0.000058 | 0.000004 | 15× |
| 16 | 0.000385 | 0.000005 | 80× |
| 32 | 0.002822 | 0.000012 | 233× |
| 64 | 0.023414 | 0.000047 | 497× |

La brecha crece con el tamaño: `mimatmul` es O(n³) con ciclos explícitos en
Python, mientras que NumPy delega la multiplicación a código nativo optimizado.

## Estado actual

- Información del computador obtenida en `data/system_info.json`.
- `src/mimatmul.py` implementado con ciclos explícitos (sin `@`, `np.matmul`,
  `np.dot` ni `np.einsum`).
- Pruebas en `tests/test_mimatmul.py` (6 pruebas, todas pasan).
- Benchmark y gráfico de rendimiento generados en `data/`.
- Documentación de este README actualizada.
