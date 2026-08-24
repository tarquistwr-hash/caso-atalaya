# Caso Atalaya — Seguridad convergente para un family office

**Un caso práctico completo de seguridad convergente físico-digital sobre un escenario de gran patrimonio: SGSI ISO/IEC 27001, un validador que ejecuta la regla de convergencia sobre el registro de riesgos, una herramienta de IA para protección de la huella familiar, y gobernanza ISO/IEC 42001 de esa herramienta. Cuatro capas sobre el mismo escenario.**

**EN — Abstract.** A complete convergent-security case study built on a fictional family office scenario: a full ISO/IEC 27001 ISMS (scenario-based risk methodology, 25-scenario risk register, 93-control SoA, and a convergence rule enforced as a verifiable requirement), a Python validator that executes that rule against the register, an AI agent for family digital-footprint monitoring (in progress), and ISO/IEC 42001 governance of that agent. Fictional in its data, real in its substance: every design decision is justified in context. Documentation in Spanish.

> ⚠️ **Escenario íntegramente ficticio.** Personas, sociedades, patrimonios y hechos son inventados y no guardan relación con ninguna persona u organización real. La verosimilitud procede de experiencia profesional real en protección ejecutiva y patrimonial; los datos, no.

---

## Por qué este caso

Los grandes patrimonios se protegen por silos: una empresa lleva la seguridad física, un MSP lleva "la informática", y nadie es dueño del espacio entre ambos. Los ataques reales no respetan esa división: empiezan en Instagram y terminan en la puerta de la finca. Este caso demuestra, pieza a pieza y con documentos reales de sistema de gestión, cómo se diseña seguridad para el conjunto.

El incidente que articula el escenario: un antiguo promotor deportivo con una cuenta pendiente encarga a un intermediario local reunir información sobre la familia. El intermediario se deja ver donde se mueve el hijo adolescente, y es el chaval quien busca el contacto. Durante semanas le suelta rutinas, viajes y detalles de la seguridad de la finca. Se destapa porque alguien del servicio de seguridad **reconoce un coche** aparcado donde no debe y lo vuelve a ver, semanas después, en las fotos que el chico publica.

Eso último es lo importante: la detección funcionó **por azar**. Dependía de que esa persona estuviera de servicio, se acordara del vehículo y atara los dos cabos. Ningún control puramente físico ni puramente digital habría cortado la cadena, y el que la cortó no era repetible ni auditable. Ese es el problema que el caso resuelve.

## El escenario en una línea

Family office español (9 personas, Marbella) de un exboxeador irlandés con ~110 M€, familia con tres hijos —uno de ellos influencer adolescente—, patrimonio en dos jurisdicciones, un círculo de confianza histórico sin marco formal y un MSP que administra desde el correo hasta las cámaras. Ficha completa: [`docs/escenario/00_escenario_caso_convergente.md`](docs/escenario/00_escenario_caso_convergente.md)

## Las cuatro capas

| Capa | Contenido | Estado |
|---|---|---|
| **1 — SGSI ISO/IEC 27001** | Sistema completo del family office: contexto, política, metodología de riesgos por escenarios, registro de 25 escenarios con 64 controles trazados uno a uno, plan de tratamiento con aceptación del residual, SoA de 93 controles justificados, las políticas que tratan los riesgos dominantes, y el bloque RGPD (RAT, ponderación del interés legítimo, EIPD) sobre los tratamientos de datos personales que el sistema genera | ✅ Publicada |
| **2 — `convergence-check`** | Validador en Python que ejecuta la regla de convergencia sobre el registro: filtra los escenarios Alto y Crítico y comprueba si cada uno alcanza cobertura efectiva en los dominios físico y digital. Es la verificación técnica que la propia metodología exige | ✅ Publicada |
| **3 — Herramienta de IA** | Monitorización de huella digital y exposición OSINT de la familia con alerta temprana, sobre el mismo escenario (trata los riesgos RSC-001, RSC-002 y RSC-015 del registro) | 🔜 En construcción |
| **4 — Gobernanza ISO/IEC 42001** | Gobernanza de esa herramienta: un sistema que trata datos de menores, geolocalización y perfiles de riesgo de personas es un caso de uso de alto riesgo que exige su propio sistema de gestión | ⏳ Pendiente |

Las capas 1 y 2 se construyen juntas y son inseparables por diseño: la regla de convergencia se escribe como norma en la metodología y se ejecuta como código sobre el registro. Las capas 3 y 4 llegan con el capstone del bootcamp de AI Engineering y después.

## Estructura del repositorio

```
.
├── README.md                             ← esto
├── LICENSE                               ← MIT para el código; la documentación, CC BY-NC 4.0
├── docs/
│   ├── escenario/
│   │   └── 00_escenario_caso_convergente.md
│   └── fase1-iso27001/
│       ├── index.md                      ← índice comentado de la documentación
│       ├── decisiones.md                 ← las decisiones de diseño y su porqué
│       ├── cadena_rsc001.md              ← el riesgo estrella, dibujado
│       ├── mapa_interfaces.md            ← las diez interfaces del alcance, dibujadas
│       ├── regla_convergencia.md         ← la regla de convergencia como árbol de decisión
│       └── flujo_verificacion_ordenes.md ← el circuito antifraude de DOC-007
├── deliverables/fase1/                   ← documentos formales (Word/Excel) y sus PDF
└── tool/convergence-check/               ← capa 2: el validador
    ├── project.py
    ├── test_project.py
    ├── README.md                         ← uso, esquema de los CSV y limitaciones conocidas
    ├── requirements.txt
    ├── riesgos.csv                       ← registro real a fecha de corte
    ├── controles.csv                     ← controles reales a fecha de corte
    └── controles_junio.csv               ← estado simulado a fecha futura, con defectos deliberados
```

## La regla, y la máquina que la comprueba

La tesis del caso cabe en una frase: **un riesgo alto o crítico no está tratado si solo tiene cobertura en el dominio físico o solo en el digital.** Los controles organizativos son necesarios y no satisfacen ninguna de las dos patas.

Eso no es un párrafo de introducción: es un requisito de la metodología (SGSI-DOC-004 §6) con una definición operativa de cobertura efectiva —control implantado, con evidencia registrada y con verificación dentro de plazo— y con un programa que la ejecuta sobre el registro completo.

```
$ python project.py riesgos.csv controles_junio.csv 30/06/2027

RSC-001 Cobertura convergente
RSC-002 Cobertura convergente
RSC-003 Cobertura convergente
RSC-004 Falta cobertura fisica
RSC-005 Cobertura convergente
...
RSC-016 Sin cobertura
RSC-018 Sin cobertura
...
RSC-021 Falta cobertura digital
RSC-022 Falta cobertura fisica
...
```

Veinticuatro escenarios evaluados, cinco sin cobertura convergente efectiva, y cada uno por un motivo distinto. El más interesante es **RSC-018**: sus cuatro controles figuran implantados y todos dejan evidencia registrada. Aun así sale sin cobertura, porque las verificaciones de sus controles físicos y digital han vencido, y el único que sigue en plazo es organizativo — y el dominio organizativo no satisface ninguna de las dos patas de la regla. Un control que nadie comprueba deja de acreditar nada, y esa distinción —incumplimiento de verificación, no de operación— es precisamente lo que un registro mantenido a mano nunca detecta.

Ese resultado no es casual: `controles_junio.csv` no es una proyección optimista del plan de tratamiento, sino un estado simulado a fecha futura construido con defectos deliberados —verificaciones caducadas y dos controles que siguen sin implantar— para que el validador tenga los cuatro diagnósticos que tratar. El estado real del sistema a fecha de corte es `controles.csv`, y ahí ningún escenario alcanza cobertura.

Detalle de uso, esquema de los CSV y suite de pruebas: [`tool/convergence-check/README.md`](tool/convergence-check/README.md)

## Documentación de la capa 1

| Código | Documento | Qué decide |
|---|---|---|
| SGSI-DOC-001 | Contexto y Alcance | La residencia entra en alcance; las sociedades irlandesas salen como organizaciones pero su flujo de información queda como interfaz; la familia no es "usuario interno" y se gestiona por acuerdo |
| SGSI-DOC-002 | Control documental | 4 niveles de clasificación; "rutinas de la familia = Restringida, siempre"; plazos de retención de todos los registros, incluidos los que contienen datos personales |
| SGSI-DOC-003 | Política de Seguridad | Política en dos niveles: declaración de una página en lenguaje llano firmada por el principal + desarrollo aprobado por delegación. Comité de Seguridad Convergente con el jefe de seguridad física dentro. Distingue el Responsable del SGSI (ISO 27001) del Responsable del Tratamiento (RGPD): son el mismo órgano de gobierno, con responsabilidades distintas |
| SGSI-DOC-004 | Metodología de riesgos | Basada en escenarios (ISO 27005, enfoque por eventos), no por activos: los riesgos que importan aquí son cadenas que cruzan dominios. Regla del máximo en impacto. Probabilidad por acumulación de condiciones de exposición, con el nivel máximo condicionado a señal observada. Alto/crítico exigen cobertura efectiva en ambos dominios: implantada, con evidencia y verificada en plazo |
| SGSI-DOC-005 | Objetivos 2026-27 | 12 objetivos medibles. Los 7 primeros miden implantación; los 5 últimos, ejecución sostenida. Dos indicadores miden fricción y no llevan meta de reducción |
| SGSI-DOC-006 | Terceros y círculo de confianza | El nivel de exigencia lo fija el acceso real, no el vínculo. Regularización del círculo histórico sin romperlo. Y una sección donde la política declara su propio límite: los invitados de la familia no son terceros contractuales, y por ahí entró el incidente |
| SGSI-DOC-007 | Verificación de órdenes financieras | Doble canal siempre; la voz no verifica (voz sintética); cuatro ojos; el freno de emergencia no penaliza. Y cinco reglas para el dinero que se mueve en efectivo, que no viajaba por ningún canal verificable |
| SGSI-DOC-008 | Seguridad en viajes | Necesidad de conocer por tramos; publicación diferida en lugar de prohibición (la prohibición a un adolescente garantiza el incumplimiento); evaluación del destino antes de la reserva, no después |
| SGSI-DOC-009 | Incidentes convergentes | Canal único, cuaderno común de indicios físicos y digitales, revisión semanal de correlación con umbral deliberadamente bajo |
| SGSI-DOC-010 | Auditoría, revisión por la dirección y mejora | Diseñados sin simular ejecuciones: programa de auditoría externalizada (con 9 personas no hay independencia interna posible), revisión anual con la propiedad, y no conformidades con verificación de eficacia |
| SGSI-DOC-011 | Ponderación del interés legítimo (RGPD art. 6.1.f) | Test de tres pasos (Dictamen 06/2014 GT29) sobre los cuatro tratamientos de SGSI-REG-008 con mayor intensidad de vigilancia: CCTV, contratas, visitas y cuaderno de indicios. Identifica que una parte del cuaderno de indicios —cuando describe a una persona por una conducta hostil o delictiva— cae en el art. 10 RGPD y no en el interés legítimo genérico, y lo remite a SGSI-DOC-012 |
| SGSI-DOC-012 | Evaluación de Impacto (EIPD, RGPD art. 35-36) | Obligatoria por concurrir cuatro criterios WP248 (observación sistemática, menores, cruce de tratamientos, datos de infracciones). Evalúa el riesgo desde el lado del interesado, no del patrimonio, con escala propia; no encuentra riesgo residual que exija consulta previa a la AEPD, salvo si el cuaderno llega a registrar un dato real del art. 10 RGPD |

| Código | Registro | Contenido |
|---|---|---|
| SGSI-REG-001/002 | Registro de riesgos + plan de tratamiento (un libro, cinco hojas) | 25 escenarios narrados como cadenas, valorados y tratados eslabón a eslabón, cada uno situado en las interfaces del alcance con vocabulario cerrado. 64 controles, uno por fila, cada uno con dominio, estado, evidencia y periodicidad de verificación: así la regla de convergencia se puede ejecutar por máquina. 16 planes con riesgo residual y su acto de aceptación |
| SGSI-REG-003 | Declaración de Aplicabilidad | 93 controles con propietario: 83 aplicables justificados por riesgo o requisito, 10 no aplicables justificados. Los diez no aplicables lo son por la misma causa —aquí no se desarrolla software ni hay entornos de desarrollo, prueba o analítica con datos reales— y los diez llevan anotada su caducidad: la capa 3 elimina esa causa y los reactiva. Ningún aplicable queda huérfano, y 12 salen marcados como deuda documental. Estado de implantación con el mismo vocabulario que el registro y regla de coherencia declarada: ningún control del Anexo A puede figurar más avanzado que su tratamiento, con dos excepciones declaradas —los controles físicos preexistentes y los acreditados por contrato de un tercero—. Regla: control sin escenario detrás = candidato a eliminación |
| SGSI-REG-004 | Cuaderno único de indicios | Registro con vocabulario controlado para la revisión semanal de correlación. Incluye la reconstrucción del cuasi-incidente: con el cuaderno operativo, el patrón se detecta en la semana 4 en lugar de la 10 |
| SGSI-REG-005 | Registro de requisitos legales | RGPD/LOPDGDD, videovigilancia, seguridad privada, fiscal ES/IE, límites al pago en efectivo, coordinación de actividades empresariales, contractuales; NIS2 y DORA evaluados y descartados por escrito |
| SGSI-REG-006 | No conformidades y deuda de diseño | La hoja de no conformidades está vacía, y es correcto: el sistema está en implantación. La de deuda de diseño lleva ocho hallazgos reales con plazo y regla de conversión (tres ya cerrados), el último de ellos (HD-08) por la ausencia de contrato de encargado del tratamiento (art. 28 RGPD) con el MSP |
| SGSI-REG-008 | Registro de Actividades de Tratamiento (RAT, RGPD art. 30) | Diez tratamientos de datos personales (T-01 a T-10) que el SGSI genera —CCTV, contratas, visitas, cuaderno de indicios, gestión de personal doméstico, verificación de órdenes financieras y banca privada, viajes y agenda, documentación patrimonial/societaria/fiscal ES-IE, presencia pública del principal, y la administración de sistemas por el MSP (correo, NAS, CCTV, domótica)—, cada uno con responsable, encargado, finalidad, base jurídica, colectivo, categorías de datos, plazo de conservación y medidas de seguridad del SGSI que lo protegen. Es la fuente única que SGSI-DOC-011 y SGSI-DOC-012 dan por conocida y no repiten |
| SGSI-INF-001 | Informe ejecutivo para la propiedad | El sistema en 2 páginas y lenguaje llano: qué pasó, qué se montó, qué cambia para la familia y qué se le pide a la propiedad |

## Decisiones de diseño (lo que distingue esto de una plantilla)

1. **El alcance persigue a la información, no al organigrama.** La residencia está dentro; la conducta de la familia se gestiona por acuerdo, no por imposición.
2. **El riesgo se piensa como cadena.** Un escenario convergente tratado solo con controles digitales, o solo físicos, se considera no tratado. Está escrito como regla en la metodología, y al ejecutarla sobre el registro completo produjo nueve incumplimientos: siete se corrigieron añadiendo los controles que faltaban en el dominio descubierto —nueve en total, siete físicos y dos digitales—, y dos siguen abiertos con plazo y responsable porque su tratamiento hay que rediseñarlo, no completarlo (RSC-004 y RSC-016, hallazgo HD-02).
3. **La regla se ejecuta, no se declara.** Si un requisito solo se comprueba a mano, deja de comprobarse en cuanto el registro crece. Por eso la regla de convergencia tiene un validador propio, y por eso el registro está diseñado con una fila por control en lugar de una lista dentro de una celda.
4. **Un control que no se ejecuta no es un control.** La cobertura solo cuenta si está implantada, deja evidencia registrada y su verificación sigue en plazo. Por eso el propio sistema declara que a fecha de corte, sin ningún control del registro implantado, ningún escenario alcanza aún cobertura efectiva.
5. **El riesgo de todos los días entra en el catálogo.** El registro de la v1.0 estaba construido desde el adversario y daba por buenos la alarma, el vigilante y el conductor porque están contratados. La revisión de campo dio entrada a ocho escenarios de fallo de ejecución y operativa material (RSC-018 a RSC-025), y con ellos el vuelco del caso: de los tres escenarios que alcanzan el nivel máximo del registro, dos no tienen adversario en el origen. Uno de ellos es, sencillamente, que la alarma no se conecta al cerrar.
6. **La probabilidad es exposición acumulada, no frecuencia.** Que caiga un rayo dentro de casa es imposible; en el campo, con tormenta, en un alto y con paraguas, probable. El rayo es el mismo: cambia dónde estás tú. El nivel máximo exige, además, una señal observada.
7. **El sistema asume a las personas reales que tiene.** Un principal que no lee documentos técnicos firma una declaración de una página que sí entiende. Un círculo de confianza de décadas se regulariza con acuerdos en lenguaje llano y la autoridad del propio principal, no con un NDA de despacho.
8. **La segregación de funciones imposible se confiesa y se compensa**, no se finge.
9. **El SGSI y el RGPD comparten sistema, no vocabulario.** Los tratamientos de datos personales que el SGSI genera —CCTV, cuaderno de indicios, correo del gestor de Irlanda— tienen su propio registro (RAT), su propia base jurídica y, cuando la vigilancia se intensifica sobre personas, su propio juicio de ponderación y su propia evaluación de impacto. No se resuelven por analogía con el registro de riesgos patrimoniales: la escala de esa evaluación mide el riesgo para el interesado, no para el patrimonio, y usa una matriz distinta a propósito.

El porqué de cada una, desarrollado: [`docs/fase1-iso27001/decisiones.md`](docs/fase1-iso27001/decisiones.md)

**Estado y fecha de corte.** El caso publica el SGSI **en implantación**, con fecha de corte 24/07/2026. Los plazos de los planes de tratamiento y de la deuda de diseño se cuentan desde ahí. Ningún control del registro de riesgos está en estado implantado, y el sistema lo dice en lugar de disimularlo.

**Qué queda fuera y por qué:** las evidencias de ejecución —actas de comité, informes de auditoría realizados, registros de formación— no se simulan. El **diseño** del ciclo de operación sí está publicado (DOC-010) y sus registros también, con su estructura y vacíos (REG-004, REG-006), porque ahí es donde se ve el criterio. Redactar actas de reuniones que nunca ocurrieron sería ficción sobre ficción. Un registro de no conformidades vacío con la explicación de por qué está vacío dice más que un registro relleno de entradas inventadas.

## Aviso legal

Caso ficticio con fines demostrativos y formativos. No constituye asesoramiento. Los documentos siguen la estructura de ISO/IEC 27001:2022 pero no reproducen el texto de la norma, que es propiedad de ISO/IEC.

## Licencia

Dos licencias, porque hay dos tipos de contenido:

- **Código** (`tool/`, y las capas 2 y 3 según se publiquen): licencia **MIT**, en [`LICENSE`](LICENSE).
- **Documentación y documentos de gestión** (`docs/`, `deliverables/`): **CC BY-NC 4.0** — se pueden leer, citar y compartir con atribución, no vender ni reutilizar como plantilla comercial.

---

*Capas 1 y 2 cerradas. La capa 3 (herramienta de IA) se construye durante el capstone del bootcamp de AI Engineering, sobre este mismo escenario y contra los riesgos RSC-001, RSC-002 y RSC-015 de este registro.*
