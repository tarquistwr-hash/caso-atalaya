# La regla de convergencia, dibujada

Lo que exige SGSI-DOC-004 §6, y lo que ejecuta literalmente `convergence-check` (capa 2) sobre el registro. No es un párrafo de metodología: es una función. Este diagrama es esa función dibujada.

```mermaid
flowchart TD
    A["Escenario del registro<br/>(SGSI-REG-001)"] --> B{"Nivel de riesgo<br/>¿Alto (6-9) o Crítico (12-16)?"}

    B -- "No —<br/>Bajo o Moderado" --> B1["Fuera del alcance de la regla.<br/>Aceptación conforme a §4.4<br/>(propietario del riesgo)"]

    B -- "Sí" --> C{"¿Tiene cobertura EFECTIVA<br/>en dominio FÍSICO?"}
    B --> D{"¿Tiene cobertura EFECTIVA<br/>en dominio DIGITAL?"}

    C --> CDEF["Cobertura efectiva =<br/>control implantado<br/>+ evidencia registrada<br/>+ verificación en plazo"]
    D --> CDEF

    CDEF --> E{"Combinación"}

    E -- "Física SÍ<br/>Digital SÍ" --> R1["✅ Cobertura convergente"]
    E -- "Física NO<br/>Digital SÍ" --> R2["⚠️ Falta cobertura física"]
    E -- "Física SÍ<br/>Digital NO" --> R3["⚠️ Falta cobertura digital"]
    E -- "Física NO<br/>Digital NO" --> R4["🛑 Sin cobertura"]

    N1["Los controles ORGANIZATIVOS<br/>no cuentan para ninguna de las dos patas.<br/>Necesarios, pero no suficientes"]
    N2["Un control PLANIFICADO,<br/>sin evidencia, o con verificación VENCIDA<br/>no cuenta como cobertura"]

    N1 -.-> CDEF
    N2 -.-> CDEF

    classDef entrada fill:#1F3864,color:#fff,stroke:#1F3864
    classDef decision fill:#fff,color:#1F3864,stroke:#1F3864,stroke-width:2px
    classDef ok fill:#fff,color:#1F3864,stroke:#2E7D32,stroke-width:2px
    classDef warn fill:#fff,color:#1F3864,stroke:#B8860B,stroke-width:2px
    classDef bad fill:#fff,color:#1F3864,stroke:#B22222,stroke-width:2px
    classDef nota fill:#fff,color:#7F7F7F,stroke:#8FAADC,stroke-dasharray: 3 3

    class A entrada
    class B,C,D,E,CDEF decision
    class R1 ok
    class R2,R3 warn
    class R4 bad
    class B1,N1,N2 nota
```

## Lo que la regla dice y lo que la regla calla

**La regla se aplica al escenario, no al control.** Un escenario puede tener cuatro controles físicos y uno digital y cumplir; la confusión contraria —"cada control necesita su gemelo"— produce relleno. Lo único que un control debe declarar es qué eslabón de la cadena rompe.

**"Sin cobertura" no significa una sola cosa.** El registro real (24/07/2026) tiene dos escenarios en ese estado por motivos opuestos: RSC-016 no tiene ningún control diseñado en ninguno de los dos dominios — es un fallo de diseño, deuda de HD-02. RSC-018 tiene sus cuatro controles implantados y con evidencia, pero la verificación de los controles físico y digital ha vencido; el único que sigue en plazo es organizativo, que no cuenta. Es un fallo de verificación, no de operación, y el diagrama de decisión no lo distingue — hay que ir al registro a mirarlo. Es la limitación que el propio `README.md` del validador señala como lo primero que cambiaría.

**A fecha de corte (24/07/2026), la rama "Cobertura convergente" está vacía.** Ningún control del registro ha alcanzado el estado IMPLEMENTADO; por tanto ningún escenario Alto o Crítico pasa hoy por la casilla ✅. Declararlo es parte de la propia regla (DOC-004 §6): un sistema que se apoya en un requisito verificable tiene que decir cuándo aún no lo cumple, no maquillarlo.

**La regla no se comprueba a mano.** Con 25 escenarios y 64 controles, cruzarlo a ojo se hace una vez y a los seis meses ya no vale. Por eso el diagrama de arriba no es una aspiración: es el código de `project.py` (funciones `clasificacion`, `es_grave`, `esta_cubierto`, `tiene_convergencia`, `diagnostico`) ejecutado sobre `riesgos.csv` y `controles.csv`.
