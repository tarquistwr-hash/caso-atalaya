# Validador de cobertura del Caso Atalaya

Versión **2.0 — 27/09/2026**. Comprueba la cobertura de los **dominios aplicables** a escenarios Altos y Críticos. La no aplicabilidad se justifica; lo pendiente no se considera cubierto. [Regla y diagrama](../../docs/fase1-iso27001/regla_convergencia.md).

La versión original fue el proyecto final de CS50P del autor. El [vídeo original](https://youtu.be/0B5Mc03_dyg) muestra una versión anterior: **han cambiado la regla, los datos y los resultados**.

## Ejecutar

La comprobación de GitHub utiliza Python 3.12. El programa principal usa la biblioteca estándar; las pruebas y el contraste con Excel requieren las dependencias indicadas. Desde esta carpeta:

```shell
python -m pip install -r requirements.txt
python project.py riesgos.csv controles.csv 24/07/2026 --detalle
python project.py riesgos.csv controles_junio.csv 30/06/2027 --json
python check_corpus.py
python -m pytest -q
```

`--exigir-cobertura` devuelve código 1 si hay carencias o evaluación pendiente. Sin esa opción, una ejecución válida devuelve 0 aunque informe carencias; los errores de entrada devuelven 2. GitHub comprueba coherencia y resultados esperados por escenario, sin exigir que un sistema en implantación aparezca cubierto.

## Datos y fuentes

| Archivo | Función |
|---|---|
| `riesgos.csv` | 25 escenarios de REG-001/002 v2.0, con dominios y justificación. |
| `controles.csv` | 64 controles al corte 24/07/2026. Ninguno IMPLEMENTADO. |
| `controles_junio.csv` | Simulación a 30/06/2027: comparte metadatos, pero modifica deliberadamente estado, evidencia y fecha de verificación. |
| `check_corpus.py` | Contrasta fórmulas del Excel, exportación y estados de la SoA. `--exportar` actualiza los dos CSV de corte; no modifica la simulación. |
| `test_project.py` | Pruebas de lógica, entradas, ejecución y resultados del corpus. |
| `ejemplo_corte.txt`, `ejemplo_demo.txt` | Salidas reproducibles; no son evidencias operativas. |

Fuentes: [registro v2.0 y Declaración de Aplicabilidad v1.10](../../deliverables/fase1/revision_2026-09-27/README.md). C-060 se retira sin reutilizar el identificador; C-065 traza una regla presencial existente de DOC-007, con su umbral.

## Qué se comprueba

- Escalas enteras 1–4; impacto máximo y probabilidad; Alto desde 6 y Crítico desde 12.
- Identificadores únicos, relaciones riesgo-control, columnas, vocabularios y fechas válidos.
- Dominios del escenario: `Fisico`, `Digital`, `Ambos` o `Pendiente`, con justificación. Son distintos del dominio del control: `FISICO`, `DIGITAL`, `ORGANIZATIVO`.
- Un control computa si está `IMPLEMENTADO`, tiene evidencia no vacía, verificación no futura y vigente, y alcance `GENERAL` justificado. El día exacto de vencimiento es válido. Periodicidades: 90, 180 o 365 días.
- `CONDICIONADO` y `PENDIENTE` se explican y no acreditan cobertura general. `GENERAL` tampoco significa eliminar todas las ramas del riesgo.
- Los 93 identificadores de la SoA, sus referencias y estados. Excepciones explícitas: A.7.1 por el perímetro preexistente y A.8.14 por contrato de tercero. Las trazas documentales no prueban eficacia.

La columna `dominios` existía en la versión 1.2, pero el algoritmo no la consultaba. La versión 2.0 la utiliza. El nivel calculado solo se contrasta con el Excel mediante `check_corpus.py`; `project.py` no lee el libro.

## Resultados y límites

**Corte 24/07/2026:** 24 escenarios sujetos a la regla, ninguno con cobertura acreditada; RSC-014 tiene evaluación pendiente. RSC-017 es Moderado y queda fuera del filtro, sin quedar fuera del SGSI.

**Demostración 30/06/2027:** 16 cumplen, 7 presentan carencias y 1 tiene evaluación pendiente. [Salida completa](ejemplo_demo.txt).

RSC-016 tiene C-020 organizativo, no ausencia total de diseño. En RSC-018 vencen las verificaciones físicas y digital. RSC-006 conserva pendiente justificar C-016; RSC-010 no obtiene cobertura digital por la instrucción bancaria C-062. RSC-014 no se resuelve suponiendo el medio de coacción.

El programa **no lee ni autentica evidencias**, no decide suficiencia jurídica o técnica, no acepta el residual y no certifica ISO/RGPD. Los dominios y la relación control–eslabón requieren revisión humana. Una medida organizativa puede ser necesaria aunque no sume cobertura.

El comprobador del corpus verifica también la numeración de eslabones y el resumen calculado de la SoA: 50 trazas al registro, 20 documentales y 13 de deuda suman sus 83 controles aplicables. Las pruebas comparan los ejemplos publicados con la salida real del programa.

## Historial

- **2.0 — 27/09/2026:** dominios aplicables, justificaciones, alcance condicionado, errores de entrada, motivos y JSON; contraste Excel–CSV–SoA y pruebas automáticas. Cambian el esquema y los resultados.
- **1.2 — 24/09/2026:** lógica común de cobertura y tildes; resultados anteriores conservados en Git.
- **1.1 — 20/09/2026:** rechazo de fechas futuras/evidencia en blanco y sincronización documental.
- **1.0:** publicación inicial para CS50P.

Escenario ficticio. [Entrega y deltas](../../docs/fase1-iso27001/revision_2026-09-27.md).
