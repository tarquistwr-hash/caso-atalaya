# Línea base 2.0 — cierre de la Fase 1

**13/11/2026.** Este documento resume qué aprobó el Comité de Seguridad Convergente al cerrar la Fase 1 y qué cambió respecto de la entrega de 27/09/2026. La sesión y sus acuerdos son parte del escenario ficticio; no existe acta con contenido ni se simula ninguna evidencia de operación.

## Acuerdos de la sesión

| N.º | Acuerdo | Dónde consta |
|---|---|---|
| 1 | Aprobar la línea base 2.0: diecinueve documentos pasan a Vigente | Cabecera de cada documento; [tabla de entregables](../../deliverables/fase1/README.md) |
| 2 | Aprobar el texto de SGSI-ACU-004 (Dirección General). Sigue en Borrador hasta la firma del MSP | SGSI-ACU-004; SGSI-REG-006, NC-2026-001 |
| 3 | Confirmar que el estado de los controles no ha variado desde el corte de 24/07/2026: ninguno implantado | SGSI-REG-001/002, hoja «Criterios» |
| 4 | Cerrar HD-06: la comprobación automática de coherencia entre la SoA y el registro existe y pasa | SGSI-REG-006; `check_corpus.py` |
| 5 | Convertir en no conformidad la deuda de diseño vencida: HD-01 → NC-2026-002, HD-02 → NC-2026-003, HD-03 → NC-2026-004 (mayor) | SGSI-REG-006; SGSI-DOC-010 §4.1 y §4.2 |
| 6 | Replanificar: los plazos de los 16 planes y de los 12 objetivos se cuentan desde el 13/11/2026 | SGSI-REG-001/002, hoja «Plan de tratamiento»; SGSI-DOC-005 §3 |
| 7 | Aprobar los seis planes revisados por la regla de dominios y aceptar sus residuales (PT-04, PT-06 y PT-12 a PT-15) | SGSI-REG-001/002, hoja «Plan de tratamiento» |
| 8 | Añadir el seguimiento mensual de plazos como quinta medición del sistema | SGSI-DOC-010 §2.3 |
| 9 | Fijar plazo cierto a HD-09 (13/03/2027) y a HD-10 (13/02/2027), que solo tenían una condición | SGSI-REG-006 |

## Estado de hallazgos y no conformidades

| Ref. | Asunto | Estado | Plazo |
|---|---|---|---|
| HD-01 | Trece controles del Anexo A sin soporte documental | Convertida en NC-2026-002 | — |
| HD-02 | RSC-004 sin control físico; RSC-016 sin medida digital | Convertida en NC-2026-003 | — |
| HD-03 | Controles físicos sin evidencia registrada (RSC-018) | Convertida en NC-2026-004 | — |
| HD-04, HD-05, HD-07 | Interfaces, objetivos y clasificación | Cerradas | — |
| HD-06 | Coherencia de estados entre la SoA y el registro | Cerrada el 13/11/2026 | — |
| HD-08 | MSP sin contrato de encargo (art. 28 RGPD) | Convertida en NC-2026-001 | — |
| HD-09 | RSC-020 sin medida digital computable | Abierta | 13/03/2027 |
| HD-10 | Validaciones de privacidad pendientes | Abierta | 13/02/2027 |
| HD-11 | Dominios y mecanismos pendientes de justificar (RSC-014, RSC-010, C-016, C-019) | Abierta | 27/11/2026 |
| NC-2026-001 | Menor · contrato de encargo con el MSP | Abierta | 20/11/2026 |
| NC-2026-002 | Menor · soporte de trece controles | Abierta | 13/02/2027 |
| NC-2026-003 | Menor · cobertura de diseño de RSC-004 y RSC-016 | Abierta | 13/01/2027 |
| NC-2026-004 | **Mayor** · controles físicos sin evidencia y planes críticos vencidos | Abierta | 13/01/2027 y 13/02/2027 |

## Tabla de impacto

| Cambio | Controles ISO 27001 | RGPD / RAT | Documentos actualizados en cascada |
|---|---|---|---|
| Conversión de HD-01, HD-02 y HD-03 y alta de NC-2026-002 a 004 | Cláusulas 8.1, 8.3, 9.1 y 10.2 | — | REG-006; DOC-010 §4.1 y §4.2; INF-001 §5; REG-003 (portada y resumen); REG-001/002 («Criterios») |
| Replanificación de plazos | Cláusulas 6.1.3, 6.2 y 8.1 | — | REG-001/002 («Plan de tratamiento»); DOC-005 §3; INF-001 §5 |
| Aceptación de residuales de seis planes | Cláusula 6.1.3 f) | — | REG-001/002 («Plan de tratamiento») |
| Seguimiento mensual de plazos | Cláusula 9.1 | — | DOC-010 §2.3 |
| HD-11 incluye la carencia digital de RSC-010 | A 5.17; DOC-004 §6 | — | REG-006; DOC-010 §4.1; DOC-007 §2 |
| Texto de ACU-004 aprobado, sin firma | A 5.20, A 5.31, A 5.34 | Art. 28; T-10 | ACU-004; REG-006 (HD-08, NC-2026-001); REG-008 (portada) |
| Decisión sobre la consulta previa remitida a HD-10 | A 5.34 | Arts. 35 y 36; T-01 y T-04 | DOC-012 §3; REG-006; REG-008 (portada) |
| Geolocalización de vehículos integrada en el procedimiento | A 5.34 | Art. 6; T-07 | DOC-008 §7; REG-006 (HD-10) |
| Dominio y alcance de controles integrados en su sección | DOC-004 §6; A 5.33 | — | DOC-004 §5.1 y §6; DOC-006 §7; DOC-007 §2 y §6 |
| Regla de versionado de las líneas base | Cláusula 7.5 | — | DOC-002 §3 y §7 |
| Figuras actualizadas a la regla y al procedimiento vigentes | — | — | DOC-004 (Figura 1); DOC-007 (Figura 1) |
| El informe ejecutivo designa a la familia por su rol | A 5.12 | Art. 5.1.c | ESC-001 (convención de nomenclatura); DOC-003 §3 |

## Qué cambió en la forma

- **Una sola plantilla.** Los catorce documentos Word se han reconstruido sobre la misma plantilla: misma cabecera de control, mismo historial, mismos estilos y mismo pie con clasificación, código, versión y página. Dos documentos (DOC-009 y el anexo del MSP) usaban otra.
- **Las revisiones, integradas.** Los párrafos añadidos al final de los documentos en septiembre («Revisión de septiembre:», «Seguimiento 27/09/2026», «Precisión de…») se han integrado en la sección que modificaban, en presente, o se han retirado si solo narraban un cambio.
- **Historiales resumidos.** Cada documento conserva su emisión, su primera aprobación, un resumen de las revisiones intermedias y la línea base. El detalle está en el [histórico](../../deliverables/fase1/historico/README.md).
- **Registros.** Los seis Excel tienen portada normalizada y la hoja «Criterios» del registro de riesgos se ha reordenado. Sus PDF son vistas de lectura con la plantilla de los documentos Word. La Declaración de Aplicabilidad ya no cita versiones en sus justificaciones.
- **Carpetas.** Lo vigente está en `deliverables/fase1/vigente/`; lo anterior, en `deliverables/fase1/historico/`.

## Lo que no cambió

Ningún escenario, valoración, control, dominio ni estado de implantación. `riesgos.csv` y `controles.csv` son idénticos a los de la entrega anterior, y el validador devuelve los mismos resultados: ningún escenario con cobertura a fecha de corte, y 16, 7 y 1 en la demostración a 30/06/2027.

## Comprobaciones

- `pytest` y `check_corpus.py` sobre los Excel de `vigente/`: sin fallos; los CSV coinciden con el Excel y la SoA cuadra (50 + 20 + 13 = 83 aplicables).
- Enlaces internos del repositorio: sin enlaces rotos.
- Los veinte PDF, revisados página a página tras generarlos.
- La tabla de deuda de diseño de SGSI-DOC-010 §4.1 y la hoja de SGSI-REG-006 salen de la misma fuente de datos, de modo que no pueden diferir.
