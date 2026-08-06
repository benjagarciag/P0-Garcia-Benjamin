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

## Estado actual

- Información del computador obtenida en `data/system_info.json`.
- Primera versión de `src/mimatmul.py` implementada.
- Pruebas iniciales en `tests/test_mimatmul.py` (3 pruebas).
- Pendiente para P0E2: benchmark, datos CSV, gráfico y documentación final.
