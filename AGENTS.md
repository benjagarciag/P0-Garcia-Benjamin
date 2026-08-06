# AGENTS.md

## Propósito del proyecto

Implementar desde cero una multiplicación de matrices (`mimatmul`), verificar
su correctitud con pruebas automáticas y comparar su rendimiento con NumPy
mediante un benchmark que genera datos (CSV) y un gráfico.

## Reglas para OpenCode

- Mantén el código sencillo y legible.
- No inventes mediciones: los datos del benchmark deben obtenerse ejecutando el
  código real en este computador.
- No ejecutes comandos destructivos de Git como `git reset --hard`.
- No subas credenciales ni archivos `.env` al repositorio.
- Ejecuta las pruebas después de modificar código:
  - `pytest`
- No hagas `git commit` ni `git push` sin pedir autorización al estudiante.
- Antes de cada commit, muestra un resumen de qué archivos cambiaron.
