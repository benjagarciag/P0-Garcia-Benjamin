# AGENTS.md

## Propósito del proyecto

Implementar desde cero una multiplicación de matrices (`mimatmul`), verificar
su correctitud con pruebas automáticas y comparar su rendimiento con NumPy
mediante un benchmark que genera datos (CSV) y un gráfico.

## Entorno

- Windows + Python 3.14.7, ambiente virtual en `.venv` (layout de Windows).
- Usa los ejecutables del venv directamente: `.venv\Scripts\python.exe`,
  `.venv\Scripts\pytest.exe` (o actívalo con `.venv\Scripts\activate`).
- Repositorio git clonado de `github.com/benjagarciag/P0-Garcia-Benjamin`
  (rama `main`); Git está disponible en el equipo.
- NumPy (`numpy==2.5.1`) está instalado en el venv y se usa solo en el
  benchmark.

## Estructura

- `src/mimatmul.py`: función `mimatmul(A, B)` sobre listas de listas. Lanza
  `ValueError` si las dimensiones no son compatibles y devuelve `[]` para
  entrada vacía.
- `src/system_info.py`: escribe `data/system_info.json`. Se regenera con
  `python -m src.system_info`.
- `src/benchmark.py`: mide `mimatmul` vs `np.matmul` y guarda
  `data/benchmark.csv`. Se ejecuta con `python -m src.benchmark`.
- `tests/test_mimatmul.py`: pruebas de correctitud de `mimatmul`.

## Pruebas

- Ejecuta `pytest` desde la raíz del proyecto después de modificar código.
- Los imports de `src.*` funcionan porque `pyproject.toml` fija
  `pythonpath = ["."]` y `testpaths = ["tests"]`; `src` no es un paquete
  instalado, no corras `pip install .`.

## Convenciones

- El idioma del proyecto es el español: mensajes de error, comentarios y docs.
- Mantén el código sencillo y legible (sin dependencias de terceros para
  `mimatmul`; solo se usa NumPy en el benchmark).

## Reglas

- No inventes mediciones: los datos del benchmark deben obtenerse ejecutando el
  código real en este computador.
- No ejecutes comandos destructivos de Git como `git reset --hard`.
- No subas credenciales ni archivos `.env` al repositorio.
- No hagas `git commit` ni `git push` sin pedir autorización al estudiante;
  antes de cada commit, muestra un resumen de qué archivos cambiaron.
