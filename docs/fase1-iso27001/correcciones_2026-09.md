# Revisión documental de septiembre de 2026

Versión 1.0 · 21/09/2026 · Autor: autor del caso · Escenario ficticio · Aprobación documental pendiente.

Se revisan 14 Word y 6 Excel originales y se exportan sus 20 PDF, disponibles en el [índice de entrega](../../deliverables/fase1/revision_2026-09/README.md). Cada documento tiene versión e historial propios. Se conservan los PDF anteriores. La fecha de corte sigue siendo 24/07/2026: esta publicación no acredita implantación, firma, aprobación del Comité ni eficacia.

## Tabla de impacto: antes / después

| Antes | Después | ISO; RGPD/RAT | Cascada |
|---|---|---|---|
| Evidencia con espacios y fechas futuras podían acreditar cobertura | Evidencia no vacía tras retirar espacios; plazo válido: cero días transcurridos hasta la periodicidad, ambos incluidos | 9.1; A.8.15; sin cambio RAT | Programa, pruebas, README |
| Importación dependiente de codificación | UTF-8 con admisión de marca inicial | 7.5; sin cambio RAT | Programa |
| C-039/C-044 DIGITAL pese al soporte en papel | ORGANIZATIVO; se retiran de A.8.15; C-044 se traza a A.5.33. RSC-019/020 sin cobertura digital acreditada | A.8.15/A.5.33; T-04/T-06 | REG-001/002, REG-003/006, DOC-004/007, CSV, README |
| C-059 presencial frente a videollamada | Desde 50.000 €, confirmación presencial también para el principal; sin excepción por urgencia. Por debajo, su circuito permite videollamada iniciada por Atalaya | A.5.14; art. 5.1.c; T-06 | DOC-005/007, REG-001/002, CSV, diagrama |
| C-006 describía mínimo de 48 horas | Publicación después de abandonar la ubicación | A.5.10/A.6.3; T-07 | CSV, DOC-008 |
| Independencia del auditor insuficientemente diferenciada | Auditor independiente de la implantación y ciclo alineado | 9.2 | DOC-003/010 |
| Indicadores con universos y frecuencias distintos | O3 incluye principal; O5 agencia; O8 distingue arranque y medición trimestral; O10 separa denominadores; O11 documenta todos los destinos, con formulario completo o simplificado | 6.2/9.1; T-05/T-06/T-07 | DOC-005 y procedimientos |
| ACU-003 duplicado; anexo MSP incoherente con redes y autoridad | MSP renumerado ACU-004 v0.2; conserva las tres redes previstas y autoridad de aprobación; región y proveedor sujetos a validación | A.5.19–5.23/A.8.22; arts. 28/44 ss.; T-10 | ACU-004, DOC-002/006/010, REG-006/008 |
| CCTV: 30 días y bases mezcladas | Máximo de un mes, con excepción y puesta a disposición según art. 22 LOPDGDD; base diferenciada de otros tratamientos | A.5.31/A.5.34/A.7.4; art. 6.1.e; T-01 | DOC-002/011/012, REG-005/008 |
| Retención laboral apoyada en art. 21 ET | Se retira esa justificación; validación por categoría pendiente; no se incluyen nóminas de agencia como propias | A.5.31/A.5.34; arts. 5.1.e/6; T-05 | DOC-002, REG-005/008, HD-10 |
| Conducta hostil equiparada a datos penales | Art. 10 según contenido concreto, sin presumir habilitación; descarte razonado de falsos positivos | A.5.25/A.5.34; arts. 5/10; T-04 | DOC-009/011/012, REG-004/008 |
| EIPD omitía un Alto y presumía reducción residual | Tres Altos iniciales; escala propia 1–3 por dimensión; sin reducción por medidas no verificadas. Consulta previa pendiente de reevaluación | A.5.34; cláusulas 8.2/8.3; arts. 35–36; T-01 a T-04 | DOC-012/010, REG-006 HD-10 |
| Roles, bases, geolocalización y transferencias poco diferenciados | Se explicitan datos de C-055 y pendientes por finalidad/relación contractual; el contrato MSP no sirve como base general de todos los tratamientos | A.5.19/A.5.31/A.5.34; arts. 6/13/28/44 ss.; T-06 a T-10 | REG-008, DOC-011/012, ACU-004, HD-10 |
| Implantación justificaba ausencia de no conformidades | NC-2026-001 vinculada al contrato de HD-08, abierta; separación entre deuda, incumplimiento y eficacia | 10.2; A.5.20/A.5.34; art. 28; T-10 | DOC-010, REG-006, índice |
| Reconstrucción garantizaba detección en semana 4 y confundía evaluación con S2 | Reconstrucción condicional a indicios y revisión; sin fecha ni severidad automática | A.5.25/A.5.27; T-04 | DOC-009, REG-004, cadena RSC-001 |
| Estado real y simulación mezclados; referencias desajustadas | Corte 2026 separado de demostración 2027; HD-04 en mapa; IA no iniciada; 13 controles con deuda; excepción A.8.14 de SoA diferenciada | 7.5/9.1; sin nueva actividad RAT | Índices, README, diagramas, DOC-010, INF-001 |

## Verificación

- Siete funciones de prueba ejecutadas directamente; 1.024 combinaciones válidas de valoración comprobadas.
- Cada celda original con contenido contrastada frente a su valor conservado o delta previsto en los seis Excel; fórmulas preservadas.
- Referencias bidireccionales entre los 64 controles y los 93 de la SoA comprobadas. Esto valida correspondencia, no certifica suficiencia de las medidas.
- Descripción y dominio de ambos CSV contrastados con el Excel revisado.
- Al corte: 24 escenarios evaluables sin cobertura. Demostración: **17 convergentes y 7 excepciones**. Los dos positivos retirados corresponden a RSC-019/020. Se mantiene la regla física + digital, sin inventar controles.
- Exportación y revisión de PDF, incluidos portadas, tablas, saltos y numeración.

## Pendientes y límites

HD-08 sigue abierto: borrador no equivale a contrato firmado. HD-09 recoge la cobertura digital no acreditada. HD-10 recoge validaciones de privacidad, conservación, responsabilidades y riesgo residual antes de operar. No se declara innecesaria la consulta previa ni se inventa una decisión de la autoridad.

Los originales disponibles DOC-009 v1.5, REG-004 v1.3 y REG-006 v1.8 tenían revisión/aprobación pendiente. Las versiones anteriores citadas como vigentes (1.4, 1.2 y 1.7) no estaban entre los archivos aportados. La revisión usa los originales disponibles y no reconstruye las versiones ausentes.

## Fuentes contrastadas

[RGPD](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32016R0679); [LOPDGDD, arts. 10, 22 y 90](https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673); [guía de videovigilancia AEPD](https://www.aepd.es/guias/guia-videovigilancia.pdf); [consulta previa AEPD](https://www.aepd.es/derechos-y-deberes/cumple-tus-deberes/medidas-de-cumplimiento/consulta-previa).

Historial: v0.1 (20/09), revisión en curso; v1.0 (21/09), deltas aplicados, editables/PDF, comprobaciones y pendientes explícitos.
