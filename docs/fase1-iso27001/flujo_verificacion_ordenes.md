# Flujo de verificación de una orden financiera (SGSI-DOC-007)

Las seis reglas de verificación (§2) aplicadas en secuencia a una orden de disposición, con el freno de emergencia (R5) como vía transversal que cualquiera puede activar en cualquier punto. Trata RSC-006 (suplantación de asesor/proveedor), RSC-010 (suplantación del principal ante la banca, incluida voz sintética) y RSC-014 (abuso de la identidad digital delegada).

```mermaid
flowchart TD
    START(["Orden de disposición recibida<br/>(email, mensajería, llamada, presencial)"])

    CONST["R2 — La voz NO verifica, nunca.<br/>Ni del principal, ni de un familiar,<br/>ni de un asesor conocido"]

    CB{"¿Cambio de cuenta<br/>de beneficiario?"}
    R4["R4 — Se trata como intento de fraude<br/>hasta verificación en contrario:<br/>R1 obligatorio + confirmación con<br/>2ª persona de la entidad receptora"]

    UMB{"¿Importe ≥ 10.000 €<br/>o cambio de beneficiario?"}
    R1["R1 — Doble canal siempre:<br/>verificación por canal DISTINTO al de entrada,<br/>contra la ficha de contactos verificados (§3).<br/>Nunca al contacto que figura en el propio mensaje"]

    UMB2{"¿Importe ≥ 50.000 €?"}
    R3["R3 — Cuatro ojos:<br/>quien prepara ≠ quien valida<br/>(asistente/financiero + Dirección General)"]

    EJEC["Orden ejecutada"]
    R6["R6 — Registro íntegro:<br/>solicitante, canal, verificaciones, validadores, importe.<br/>Revisión mensual por Dirección General"]

    R5["🛑 R5 — Freno de emergencia<br/>Urgencia, presión o confidencialidad exigida<br/>= indicio de fraude, no motivo para saltarse el proceso.<br/>Cualquier interviniente detiene la orden,<br/>sin autorización previa.<br/>Escala a Dirección General.<br/>Se anota en el cuaderno de indicios (DOC-009 §5)<br/>aunque resultara legítima"]

    START --> CB
    CB -- "Sí" --> R4 --> UMB
    CB -- "No" --> UMB
    UMB -- "Sí" --> R1 --> UMB2
    UMB -- "No" --> UMB2
    UMB2 -- "Sí" --> R3 --> EJEC
    UMB2 -- "No" --> EJEC
    EJEC --> R6

    CONST -.->|"aplica en todo momento"| START
    R5 -.->|"puede activarse en cualquier punto"| CB
    R5 -.-> UMB
    R5 -.-> UMB2

    PRINC["Circuito reforzado del principal (§4)<br/>Asistente formaliza por escrito →<br/>el principal confirma presencial o por videollamada<br/>INICIADA por Atalaya (nunca llamada entrante) →<br/>si ≥ 50.000 €, valida también Dirección General (R3)"]
    START -.->|"si la orden es del principal"| PRINC
    PRINC -.-> UMB

    classDef start fill:#1F3864,color:#fff,stroke:#1F3864
    classDef regla fill:#fff,color:#1F3864,stroke:#1F3864,stroke-width:2px
    classDef decision fill:#fff,color:#1F3864,stroke:#1F3864
    classDef freno fill:#fff,color:#B22222,stroke:#B22222,stroke-width:2px
    classDef nota fill:#fff,color:#7F7F7F,stroke:#8FAADC,stroke-dasharray: 3 3

    class START,EJEC start
    class R1,R3,R4,R6 regla
    class CB,UMB,UMB2 decision
    class R5 freno
    class CONST,PRINC nota
```

## Lo que el flujo no deja pasar

**El freno de emergencia no es el último paso: es transversal.** R5 no espera a que la orden falle una regla — cualquier interviniente puede pararla en cualquier punto de la secuencia, sin autorización previa y sin consecuencias para quien la para. El coste de una falsa alarma es una reunión; el de no pararla, ya se conoce por el cuasi-incidente fundacional. Y se anota en el cuaderno de indicios con independencia de que la orden resultara legítima: el patrón de intentos importa aunque cada intento individual se explique.

**La voz nunca es un canal de verificación**, ni siquiera cuando quien llama es reconocible. Con cientos de horas de voz pública del principal, la suplantación por voz sintética (RSC-010) es hoy trivial — y por eso R2 no admite excepción por confianza o urgencia.

**El circuito del principal no es un atajo: es un circuito distinto y más estricto**, diseñado porque el principal no opera medios digitales propios y delega su identidad en su asistente personal. La videollamada la inicia siempre Atalaya hacia el dispositivo registrado — nunca se acepta una llamada entrante como confirmación —, lo que protege a la vez al patrimonio y a la asistente: ningún acto suyo en nombre del principal queda sin confirmar ni sin registrar.

**Lo que este diagrama no cubre: el efectivo.** Las disposiciones en efectivo y el movimiento físico de valores (RSC-019) no viajan por ningún canal verificable, así que R1-R6 no les aplican — DOC-007 §6 las trata con un juego de reglas propio (E1-E5), que es harina de otro diagrama.

**Aplicación de la regla de convergencia (DOC-004 §6).** E1/E2 (§6) son organizativos, E4 aporta la cobertura física y E3 la digital — la nota de trazabilidad ya está en el propio DOC-007, no se repite aquí.
