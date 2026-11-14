# Fase 1 — SGSI ISO/IEC 27001 · Índice de la documentación

**Estado: línea base 2.0, aprobada por el Comité de Seguridad Convergente el 13/11/2026** (aprobación dentro del escenario ficticio). Diecinueve documentos vigentes y uno, el anexo del proveedor informático, en Borrador hasta su firma. Los documentos formales, en Word o Excel y en PDF, están en [`deliverables/fase1/vigente/`](../../deliverables/fase1/README.md). Este índice explica qué hace cada pieza y en qué orden leerla.

> **El sistema está en implantación, no operado.** Los datos de estado de los controles son los del corte de 24/07/2026, confirmados sin variación el 13/11/2026: ningún control del registro de riesgos ha alcanzado el estado IMPLEMENTADO y, aplicando literalmente la definición de cobertura efectiva de la metodología, ningún escenario la alcanza todavía. Un sistema que presume de una regla verificable tiene que decir cuándo aún no la cumple.

> **Hay cuatro no conformidades abiertas, una de ellas mayor.** Entre julio y noviembre el diseño se revisó cuatro veces y no se implantó nada; los primeros plazos vencieron. La línea base lo registra en lugar de mover las fechas: está en SGSI-REG-006 y explicado en [decisiones.md, sección 25](decisiones.md).

> **Sobre la clasificación.** Los documentos van marcados «Interna», «Confidencial» o «Restringida» porque esa es su clasificación dentro de la ficción: una Declaración de Aplicabilidad o un registro de riesgos reales no se publican. Este repositorio puede mostrarlos porque el caso es ficticio.

## Orden de lectura recomendado

Si solo vas a leer tres cosas: el [escenario](../escenario/00_escenario_caso_convergente.md), las [decisiones de diseño](decisiones.md) y el [informe ejecutivo para la propiedad](../../deliverables/fase1/vigente/SGSIINF001_Informe_Ejecutivo_Propiedad_v2_0.pdf). Ahí está el caso; el resto es el sistema.

Si quieres ver la regla funcionando en lugar de leerla, el validador está en [`tool/convergence-check/`](../../tool/convergence-check/README.md): lee el registro de riesgos exportado a CSV y devuelve, escenario a escenario, si alcanza cobertura efectiva en sus dominios aplicables.

Qué se aprobó al cerrar la fase y qué cambió respecto de las entregas anteriores: [línea base de cierre de la Fase 1](linea_base_2026-11-13.md).

## Documentos del sistema

| Código | Documento | Para qué existe |
|---|---|---|
| ESC-001 | [Ficha de escenario](../escenario/00_escenario_caso_convergente.md) | La base del caso: quién es quién, qué hay en juego, el cuasi-incidente que lo arranca todo y lo que pasa el resto de los días |
| SGSI-DOC-001 | Contexto y alcance | Qué protege el SGSI y qué deja fuera, con cada exclusión justificada. Diez interfaces donde el sistema se juega la eficacia: cada escenario del registro cita al menos una, y ninguna se queda sin escenario que la ponga a prueba |
| SGSI-DOC-002 | Control documental | Codificación, versionado, estados y los cuatro niveles de clasificación. La regla que más se usa: rutinas de la familia = Restringida, siempre. Plazos de retención de los registros con datos personales |
| SGSI-DOC-003 | Política de seguridad | Política en dos niveles: la declaración de una página que el principal entiende y firma, y el desarrollo aprobado por delegación. Distingue el Responsable del SGSI (ISO 27001) del Responsable del Tratamiento (RGPD) |
| SGSI-DOC-004 | Metodología de riesgos | Evaluación por escenarios narrados como cadenas, con MAGERIT, FAIR y las listas de comprobación descartados por escrito. Regla del máximo, matriz 4×4, probabilidad por exposición acumulada y la regla de cobertura por dominios aplicables, que es la que ejecuta el validador. Anexo B: el cuasi-incidente resuelto como ejemplo |
| SGSI-DOC-005 | Objetivos 2026-27 | Doce objetivos medibles. Los siete primeros miden implantación; los cinco últimos, ejecución sostenida. Dos indicadores miden fricción en lugar de cumplimiento |
| SGSI-DOC-006 | Terceros y círculo de confianza | Niveles T1-T3 por acceso real, no por vínculo. Planificación previa de obras y contratas. Y una sección donde la política declara su propio límite: los invitados de la familia no son terceros contractuales, y por ahí entró el cuasi-incidente |
| SGSI-DOC-007 | Verificación de órdenes | Seis reglas antifraude —la central: la voz no verifica nada— y cinco reglas para el dinero en efectivo, que no viajaba por ningún canal verificable |
| SGSI-DOC-008 | Seguridad en viajes | Necesidad de conocer por tramos, publicación diferida en lugar de prohibición, evaluación del destino antes de la reserva y los trayectos diarios |
| SGSI-DOC-009 | Incidentes convergentes | El cuaderno único de indicios físicos y digitales y la revisión semanal de correlación. La inejecución de un control es un evento, no una incidencia laboral |
| SGSI-DOC-010 | Auditoría, revisión y mejora | Evaluación del desempeño diseñada sin fingir ejecuciones: auditoría externalizada, revisión anual con la propiedad, cinco mediciones (cláusula 9.1) y la sección 4, con la deuda de diseño y las no conformidades registradas |
| SGSI-DOC-011 | Ponderación del interés legítimo | Necesidad, proporcionalidad y ponderación de los cuatro tratamientos con mayor intensidad de vigilancia: videovigilancia, contratas, visitas y cuaderno de indicios |
| SGSI-DOC-012 | Evaluación de impacto (EIPD) | Riesgo desde el lado del interesado, con escala propia y no la matriz patrimonial. Tres riesgos Altos que conservan su nivel mientras no se justifique reducirlo |
| SGSI-INF-001 | Informe ejecutivo para la propiedad | El sistema entero en lenguaje llano: lo único que la propiedad necesita leer |
| SGSI-ACU-004 | Anexo de encargo del tratamiento con el MSP | Lo que el art. 28 RGPD exige al proveedor que administra correo, NAS y cámaras. En Borrador hasta su firma |

## Registros

| Código | Registro | Contenido |
|---|---|---|
| SGSI-REG-001/002 | Registro de riesgos y plan de tratamiento | 25 escenarios valorados, cada uno con sus dominios justificados; 64 controles, uno por fila, con dominio, estado, evidencia, periodicidad y alcance; 16 planes con su residual aceptado por el propietario del riesgo y ratificado por el Comité en los doce que cierran en Alto |
| SGSI-REG-003 | Declaración de Aplicabilidad | 93 controles del Anexo A: 83 aplicables y 10 excluidos, justificados uno a uno. Cada aplicable traza a un control del registro (50), a un documento (20) o consta como deuda documental (13) |
| SGSI-REG-004 | Cuaderno único de indicios | Estructura del registro y de la revisión semanal de correlación, con una reconstrucción condicional del cuasi-incidente. Sin entradas reales |
| SGSI-REG-005 | Requisitos legales | RGPD y LOPDGDD, videovigilancia, seguridad privada, fiscal España-Irlanda, límites al pago en efectivo y coordinación con contratas; NIS2 y DORA evaluados y descartados por escrito |
| SGSI-REG-006 | No conformidades y deuda de diseño | Once hallazgos de diseño (cuatro cerrados, tres abiertos y cuatro convertidos) y cuatro no conformidades abiertas, con causa, acción, responsable, plazo y verificación de eficacia |
| SGSI-REG-008 | Registro de Actividades de Tratamiento | Diez tratamientos de datos personales (T-01 a T-10), con responsable, encargado, finalidad, base jurídica, conservación y medidas |

## Diagramas

Cuatro piezas que se entienden mejor dibujadas, todas en Mermaid:

- **[cadena_rsc001.md](cadena_rsc001.md)** — la cadena del cuasi-incidente, con sus seis eslabones y cada control situado sobre el que rompe.
- **[mapa_interfaces.md](mapa_interfaces.md)** — las diez interfaces del alcance y el riesgo de borde de cada una.
- **[regla_convergencia.md](regla_convergencia.md)** — la regla de cobertura como el árbol de decisión que ejecuta el validador.
- **[flujo_verificacion_ordenes.md](flujo_verificacion_ordenes.md)** — el circuito antifraude: las seis reglas en secuencia, con el freno de emergencia y el circuito reforzado del principal.

## Lo que este repositorio no incluye, y por qué

Las evidencias de operación no se simulan: no hay actas con contenido, informes de auditoría, registros de cierre diario ni evidencias de formación, porque nada de eso ha ocurrido. Las sesiones del Comité y sus aprobaciones sí forman parte del escenario, como la familia: son decisiones de gobierno que el propio diseño exige, no pruebas de que algo funcione.

La distinción importa. El diseño del ciclo de operación (SGSI-DOC-010) y los registros con su estructura (SGSI-REG-004, SGSI-REG-006) están publicados, porque ahí se ve el criterio. Un cuaderno de indicios sin entradas y con la explicación de por qué está vacío dice más que uno relleno de entradas inventadas.

## Versiones anteriores

Las entregas previas a la línea base están en [`deliverables/fase1/historico/`](../../deliverables/fase1/historico/README.md), y las notas de cada revisión, en [`historial/`](historial/). Cómo evolucionó el sistema y qué encontró cada revisión se cuenta en [decisiones.md](decisiones.md), secciones 19 a 26.
