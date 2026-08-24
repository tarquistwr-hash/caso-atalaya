# Decisiones de diseño — Fase 1 (ISO/IEC 27001)

Este documento recoge las decisiones que definen el SGSI del caso y el razonamiento detrás de cada una. Es la pieza que distingue este trabajo de una plantilla rellenada: cualquiera puede descargar un kit de documentos 27001; lo que no viene en el kit es por qué cada cosa es como es **en este contexto**.

---

## 1. El alcance persigue a la información, no al organigrama

**Decisión:** la residencia principal de la familia está dentro del alcance del SGSI. Las sociedades irlandesas están fuera como organizaciones, pero el flujo de información con sus gestores está dentro como interfaz. Los miembros de la familia no son "usuarios internos" del sistema.

**Por qué:** un SGSI de family office que solo cubra la oficina es papel: el NAS con la documentación familiar, la videovigilancia, la domótica y el despacho del principal están en la casa. A la inversa, pretender que el SGSI gobierne la conducta de la familia (imponer políticas a un adolescente) fracasa en el primer mes y quema la credibilidad del sistema entero. La solución: la casa dentro, la familia como interfaz gestionada por acuerdo a través de un rol creado para ello — la representante de la propiedad, que no es un invento del sistema sino la formalización de una figura que en estas casas ya existe de facto (ESC-001 §10).

**Qué habría hecho una plantilla:** alcance = "las oficinas de la organización", y la casa —donde vive el riesgo— fuera del sistema.

## 2. Riesgos como cadenas, no como pares activo-amenaza

**Decisión:** metodología basada en escenarios (enfoque por eventos de ISO/IEC 27005:2022). MAGERIT, FAIR y las checklists de cumplimiento, descartados por escrito en el propio documento de metodología.

**Por qué:** el incidente que origina el caso —un encargo delegado a un intermediario local, que se hace visible en el entorno del hijo mayor hasta que es este quien busca el contacto, extracción gradual de rutinas y vigilancia física de confirmación— no es descomponible en pares activo-amenaza sin perder exactamente lo que lo hace peligroso: la secuencia, y el hecho de que quien lo instiga no actúa nunca. Además, una organización de nueve personas puede mantener vivo un catálogo de 25 escenarios; no puede mantener una matriz de cientos de combinaciones, que degenera en un documento muerto que nadie vuelve a abrir.

**La regla con dientes:** los escenarios de nivel Alto o Crítico exigen **cobertura efectiva en los dominios físico y digital**. Un escenario convergente tratado solo con controles digitales, o solo con físicos, se considera **no tratado**. Los controles organizativos son necesarios pero no satisfacen por sí solos ninguna de las dos patas: obligan al analista a decir dónde aterriza cada control, y "procedimiento de verificación" no es un control hasta que se declara si es una llamada, una firma presencial o un segundo canal en una aplicación.

La regla se aplica **al escenario, no a cada control**: un riesgo puede tener cuatro controles físicos y uno digital y cumplir. La confusión contraria —"cada control necesita su gemelo digital"— produce relleno, que es justo lo que la regla quiere evitar. Como candado adicional, cada control debe declarar **qué eslabón de la cadena rompe**; el que no rompe ninguno y está solo para cumplir la regla, se cae.

Esto convierte la tesis de la convergencia en una regla verificable de la metodología, no en un párrafo de introducción. Y es verificable en sentido literal: al ejecutarla sobre el registro completo produjo **nueve incumplimientos**. Siete se corrigieron añadiendo al plan los controles que faltaban en el dominio descubierto —nueve controles en total, siete físicos y dos digitales, C-056 a C-064: dos de esos siete escenarios no tenían ninguna de las dos patas y necesitaron un control en cada dominio—. Los otros dos no: RSC-004 y RSC-016 necesitan rediseñar el tratamiento, no completarlo, y quedan registrados como deuda de diseño con plazo (HD-02). Una regla que solo produce hallazgos que uno sabe arreglar en el momento no es una regla, es un adorno.

## 3. El impacto no se promedia

**Decisión:** el impacto de un escenario es el máximo de sus cuatro dimensiones (personas, patrimonio, privacidad/reputación, legal), nunca la media.

**Por qué:** en este contexto el activo final son personas, tres de ellas menores. Un escenario con impacto máximo sobre personas y bajo coste económico no puede salir "moderado" por aritmética. Promediarlo sería una decisión ética disfrazada de fórmula. Por el mismo motivo se descartó la cuantificación económica tipo FAIR: monetizar el daño a un menor como criterio de decisión es una frontera que este sistema no cruza.

## 4. El liderazgo se diseña para el líder que hay, no para el que la norma imagina

**Decisión:** política en dos niveles. Una declaración de compromiso de una página, en lenguaje llano, que el principal entiende y firma; y el desarrollo técnico aprobado por el Comité por delegación expresa. El documento lo dice sin eufemismos: una firma sobre un texto no leído no es liderazgo, es un riesgo documentado.

**Por qué:** el principal del escenario no lee documentos técnicos y desprecia los protocolos ("yo vengo de la calle"). La alternativa estándar —hacerle firmar una política de diez páginas— cumple la letra de la cláusula 5 y traiciona su espíritu. Y hay un segundo movimiento: la declaración la comunica él en persona al personal y al círculo de confianza, porque la autoridad que esas personas reconocen es la suya, no la de un procedimiento.

## 5. El círculo de confianza: el requisito va del sistema hacia ellos

**Decisión:** las dos personas del entorno histórico del principal (acceso físico total, poderes notariales amplios, cero marco formal) se tratan como parte interesada con un giro deliberado: el requisito no es de ellos hacia el SGSI, sino del SGSI hacia ellos — regularizar su acceso **sin romper la relación**. Acuerdos personales en lenguaje llano, revisión de poderes con asesoría legal, y sesión de concienciación propia con el principal delante.

**Por qué:** en un family office real, formalizar mal al círculo de confianza es la forma más rápida de cargarse el proyecto: esas personas tienen más influencia sobre el principal que cualquier consultor. El documento de terceros lo declara como lo que es: el riesgo de implantación más alto de todo el proyecto.

## 6. La voz no verifica

**Decisión:** regla R2 del procedimiento de órdenes: la voz no es factor de verificación para nada, y las entidades bancarias son informadas por escrito de que Atalaya no reconoce órdenes verificadas solo por voz.

**Por qué:** el principal tiene cientos de horas de voz pública (combates, entrevistas, streams). En 2026, clonar esa voz es trivial. La regla incomoda —contradice décadas de "conozco su voz, es él"— y precisamente por eso hay que escribirla y comunicarla a los bancos antes del incidente, no después.

## 7. La segregación imposible se confiesa

**Decisión:** el sistema declara que con nueve personas la segregación completa de funciones es materialmente imposible, y la compensa: cuatro ojos en operaciones críticas, registro de los actos por delegación, revisión mensual.

**Por qué:** fingir segregación en una estructura de nueve es la mentira más común de los SGSI pequeños, y un auditor competente la desmonta en una mañana. Declarar la limitación y demostrar los compensatorios es más defendible y más honesto. El caso particular más delicado: la asistente personal concentra la identidad digital del principal. El circuito de confirmación la protege a ella tanto como al patrimonio — cada acto suyo queda confirmado y registrado, de modo que ni puede ser suplantada sin detección ni señalada sin causa.

## 8. Publicación diferida, no prohibición

**Decisión:** la regla acordada con la familia para redes sociales no prohíbe publicar: difiere la publicación hasta haber abandonado la ubicación.

**Por qué:** el vector del cuasi-incidente fundacional es un adolescente con una marca personal creciente. Prohibirle publicar garantiza el incumplimiento sistemático y, peor, clandestino. El diferimiento preserva su actividad y elimina el valor operativo de la señal para un observador hostil: le quita al dato lo único que lo hacía peligroso, el tiempo real.

## 9. Un control sin escenario detrás es un candidato a eliminación

**Decisión:** en la Declaración de Aplicabilidad, cada control aplicable remite al riesgo o requisito que lo exige. Diez controles se declaran no aplicables con justificación individual, y los diez lo son por la misma causa: aquí no se desarrolla software ni existen entornos de desarrollo, prueba o analítica que traten datos reales. Esa causa lleva anotada su propia caducidad: si la herramienta de IA de la Fase 2 entra en alcance, la causa desaparece y los diez se reactivan.

**Por qué:** la SoA típica marca 93 "aplicables" sin que nadie sepa por qué, y eso es exactamente lo contrario de gestionar. La regla inversa —el control se gana su sitio o sale— produce un sistema que la organización puede sostener y un documento que un auditor puede seguir. Y la nota de caducidad de la exclusión es la costura visible entre las fases del caso: el sistema ya sabe qué le cambiará cuando llegue la IA. El más elocuente de los diez es 8.11, enmascaramiento de datos, que hoy no aplica porque no hay ningún tratamiento analítico con datos reales y que pasará a ser el control más exigente del conjunto en cuanto la herramienta procese datos de tres menores.

## 10. La probabilidad no es una frecuencia: es exposición acumulada

**Decisión:** los anclajes de probabilidad no se apoyan en estadística de incidentes —que esta organización no tiene— sino en la acumulación de condiciones de exposición. El nivel 4 exige, además, una **señal observada**: que ya haya ocurrido, que haya indicios activos o que alguien lo haya intentado.

**Por qué:** que caiga un rayo dentro de casa es imposible. En el campo, muy poco probable. En el campo, con tormenta, en un alto y con un paraguas, probable. Encima de un pararrayos, muy probable. El rayo es el mismo en los cuatro casos: lo que cambia es dónde estás tú. Trasladado al caso, las condiciones son que la información esté en abierto, que el acceso sea fácil, que haya alguien con motivo cerca, que el perfil sea notorio y que exista precedente.

Esto resuelve el problema real de valorar probabilidad en una organización sin datos: en vez de inventar una frecuencia, se cuenta lo que está a la vista. Y la separación entre el 3 y el 4 deja de ser intuición: **el 4 exige haber visto algo**. Ante la pregunta "¿por qué probabilidad 3 y no 2?", la respuesta no es "lo pone la tabla".

**Qué habría hecho una plantilla:** cuatro adjetivos —raro, posible, probable, muy probable— sin definir, aplicados a ojo y con la gravedad del daño contaminando la estimación.

## 11. Un control que no se ejecuta no es un control

**Decisión:** la cobertura solo cuenta si el control está **implantado y su ejecución deja evidencia registrada**. Un control planificado, o implantado pero sin prueba de que opera, no cubre nada a efectos de la regla de convergencia.

**Por qué:** el catálogo inicial de escenarios estaba construido desde el adversario y por eso daba por buenos la alarma, el vigilante y el conductor: están contratados y operativos. La revisión de campo aportó lo contrario — la alarma que no se conecta al cerrar, la ronda que se descuida en una conversación larga, el retraso que deja a la familia esperando en la calle. El control existe y no opera, que a efectos de exposición equivale a que no exista.

De ahí salen ocho escenarios nuevos (RSC-018 a RSC-025) y, con ellos, un vuelco: **de los tres escenarios que alcanzan el nivel máximo del registro (Crítico, 16), dos no tienen adversario en el origen**. Empatan con el cuasi-incidente fundacional, y uno de los dos es, sencillamente, que la casa no se cierra bien (RSC-018); el otro, que los hijos meten en casa a quien les parece (RSC-021).

**Consecuencia en los indicadores:** los objetivos del ciclo se dividen en los que miden *implantación* (O1–O7) y los que miden *ejecución sostenida* (O8–O12), evaluados sobre el último trimestre y no sobre el mes de arranque.

## 12. Dos indicadores miden fricción, no cumplimiento

**Decisión:** el número de usos de la vía de urgencia del procedimiento de órdenes y la proporción de visitas registradas sobre las detectadas se miden **sin meta de reducción**.

**Por qué:** un control que en la práctica nadie cumple es peor que no tenerlo, porque produce falsa seguridad. Si en un trimestre hay tres urgencias con doble validación, el procedimiento encaja; si hay quince, el procedimiento no existe y hay que rediseñarlo, no exigir más disciplina. Convertir esas cifras en objetivo de cumplimiento solo conseguiría que dejaran de registrarse.

Lo mismo con las visitas: es un control que descansa en la voluntad de la familia y no es verificable por medios técnicos. La meta es del 80%, no del 100%, porque una meta del 100% sería falsa y su incumplimiento se trataría como falta personal en lugar de como señal de que el diseño roza.

## 13. La política de terceros declara su propio límite

**Decisión:** la política de terceros está construida sobre la relación contractual y **no cubre a los invitados de la familia**. En vez de estirar la tabla de niveles para meter ahí al amigo de un hijo, el documento reconoce el límite y añade una sección propia con tres reglas mínimas acordadas —no impuestas— con la familia.

**Por qué:** el cuasi-incidente entró exactamente por ahí. Someter a una visita social a verificación de idoneidad y firma de acuerdos sería desproporcionado, inaplicable y contrario a la vida normal de una familia; fingir que la tabla T1-T3 los cubre sería peor. La sección incluye además una aceptación explícita: estas reglas dependen del cumplimiento voluntario y su eficacia se mide de forma indirecta. **Un control que descansa en la voluntad de una persona debe declararse como tal y no presentarse como una barrera.**

Este mismo criterio se aplica después en otro sitio: cuando el Anexo A no contiene un control para lo que el registro trata —la logística de efectivo, la seguridad en destino, la posición de un vehículo—, la SoA declara el mapeo como adaptación en lugar de forzar el encaje en silencio. Declarar el límite es siempre más fuerte que disimularlo.

## 14. Lo que se detecta antes de la auditoría no se llama no conformidad

**Decisión:** la trazabilidad entre el registro de riesgos y la SoA produjo seis hallazgos antes de que existiera auditoría alguna. Se registran como **deuda de diseño**, no como no conformidades, con responsable, plazo y una regla de conversión: vencido el plazo sin cierre, entonces sí lo son.

**Por qué:** en fase de implantación, un control planificado que aún no opera no incumple ningún requisito. Calificar doce controles sin soporte documental y dos riesgos sin convergencia como "no conformidades" inflaría el registro justo antes del primer ciclo y devaluaría el término precisamente cuando más falta hace que signifique algo. Saber cuándo **no** usar la etiqueta es parte del criterio.

**Los hallazgos se publican, no se esconden.** La SoA marca doce controles declarados aplicables que descansaban en una práctica no escrita, y el registro deja dos escenarios sin cobertura convergente. Un sistema que sale limpio a la primera es un sistema que nadie ha comprobado.

## 15. Se registran también los hallazgos ya corregidos

**Decisión:** dos hallazgos detectados y resueltos en el mismo acto —escenarios sin interfaz declarada, escenarios sin objetivo asociado— se registran igualmente.

**Por qué:** omitirlos dejaría sin rastro el mecanismo que los encontró. Y el mecanismo —la verificación cruzada entre registro, alcance, SoA y objetivos— es precisamente lo que hay que repetir en cada ciclo. El hallazgo es prescindible; el procedimiento que lo produjo, no. Uno de los dos, además, venía arrastrándose desde la versión 1.0: dos riesgos llevaban meses sin objetivo asociado y nadie lo había visto porque nadie había cruzado las dos listas.

## 16. No se versiona lo que no lo necesita

**Decisión:** la declaración de compromiso de la política (DOC-003 §3) es lo único del sistema que **no se versiona nunca**. El desarrollo del documento sí se revisa cuando hace falta; la página firmada, no.

**Por qué:** la política se estructuró en dos niveles precisamente para esto. El desarrollo técnico lo aprueba el Comité por delegación y se revisa como cualquier otro procedimiento —en el ciclo v1.1 no hizo falta, y en el cierre del ciclo sí, para dar entrada a la toma de conciencia y a los recursos—. La declaración de la sección 3 está firmada por el principal, y tocarla obliga a una nueva firma. Separar los dos niveles permite mantener vivo el documento sin devaluar la firma, que es justo lo que se perdería si cada corrección de una tabla obligara a volver a sentar al principal delante de un papel. Versionar por simetría es ruido con coste; no versionar por miedo a la firma es dejar morir el documento.

## 17. La regla se ejecuta, no se declara

**Decisión:** la regla de convergencia tiene un validador propio —`convergence-check`, capa 2 del caso— que la ejecuta sobre el registro exportado a CSV y devuelve, escenario a escenario, si alcanza cobertura efectiva. La metodología (DOC-004 §6) y el registro (REG-001, hoja «Criterios») lo citan como el mecanismo de la «verificación técnica» que DOC-010 §3.1 exige como entrada de la revisión por la dirección.

**Por qué:** un requisito que solo se comprueba a mano deja de comprobarse en cuanto el registro crece. Con 25 escenarios y 64 controles, cruzarlo a ojo lleva una tarde y se hace una vez; a los seis meses el registro sigue pareciendo correcto y ya no lo es. La comprobación automática no es una floritura de programador: es lo que convierte la regla en un requisito sostenible.

Esto tiene una consecuencia hacia atrás que es la parte interesante: **el registro está diseñado para poder ejecutarse.** Una fila por control en lugar de una lista dentro de una celda, un vocabulario de dominio y estado cerrado y en mayúsculas, y las columnas de periodicidad y última verificación como datos y no como comentario. Esas decisiones parecen de formato y no lo son: sin ellas la regla no es verificable por máquina y vuelve a ser un párrafo bonito.

**Qué habría hecho una plantilla:** una columna «¿Cubierto? Sí/No» rellenada por quien redacta el registro, que es exactamente la persona que no puede auditarse a sí misma.

## 18. El residual Alto no se acepta por defecto: se firma

**Decisión:** doce de los dieciséis planes de tratamiento cierran en riesgo residual Alto. Ninguno se da por aceptado de forma implícita. La aceptación del riesgo residual corresponde al **propietario del riesgo**, como exige ISO/IEC 27001 6.1.3 f), que es también quien aprueba el plan; sobre ese mínimo, esta organización añade un requisito más estricto: todo residual Alto exige además **ratificación expresa del Comité**, registrada en acta. El plan lleva columnas propias para los tres actos. Ningún plan admite residual Crítico.

**Por qué:** la concentración en la banda alta es la consecuencia lógica de la regla del máximo en un contexto cuyo activo final son personas. Ningún control reduce por debajo de 4 el impacto sobre personas de una aproximación coactiva; lo que el tratamiento reduce es la probabilidad, y por eso los residuales bajan de 16 a 8 y no a 3. Rebajar el impacto para que la matriz quedara más presentable sería falsear la valoración.

Pero un sistema donde casi todo queda en Alto tiene un problema real: si el nivel no discrimina, deja de servir para priorizar. La solución no es maquillar la escala, es poner la priorización donde de verdad está —en la secuencia de plazos del plan, de dos a seis meses— y obligar a que cada residual Alto se acepte por acto expreso. Doce firmas incomodan; ese es el punto. Un criterio de aceptación que no genera ninguna obligación visible es un criterio decorativo.

Y la distinción entre quién acepta y quién ratifica no es formalismo: la norma pone la responsabilidad en el propietario precisamente para que nadie pueda diluirla en un órgano colegiado. Un riesgo aceptado "por el Comité" es un riesgo que no ha aceptado nadie en particular.

## 19. Las reglas se comprueban también contra los documentos que las enuncian

**Decisión:** el ciclo v1.3 no añade escenarios, controles ni objetivos. Cruza cada regla enunciada en la documentación contra el registro que dice gobernar, y corrige la regla cuando la que estaba mal era la regla.

**Por qué:** los ciclos anteriores comprobaron el registro contra sí mismo —trazabilidad de la SoA, escenarios sin interfaz, escenarios sin objetivo—. Faltaba la comprobación inversa, que es la que un lector externo hace de verdad: coger una frase de la metodología y verificarla fila a fila. Salieron cuatro cosas, y ninguna era un error de valoración:

- **La columna «Dominios» no significaba lo que tres documentos decían que significaba.** La metodología, la hoja de criterios y el índice afirmaban que reflejaba «la cobertura prevista por el tratamiento diseñado». No es cierto en diez de veinticinco filas: la columna describe los dominios que el escenario **atraviesa**, que es información distinta y más útil. Se corrige la frase, no la columna, y el encabezado pasa a llamarse «Dominios del escenario». La cobertura por dominios se lee donde tiene que leerse: en la hoja de controles, y la comprueba el validador.

- **La regla de completitud del alcance no era verificable.** HD-04 se cerró añadiendo cuatro interfaces a DOC-001, pero la columna «Interfaz» del registro siguió usando vocabulario propio —«Interna», «Externa», «Terceros»— que no apuntaba a ninguna interfaz declarada. La corrección estaba hecha en un documento y no en el otro. Se normaliza la columna a las diez interfaces declaradas, y con eso la regla queda verificable en los dos sentidos: todo escenario cita una interfaz del alcance, y toda interfaz del alcance es citada por algún escenario. Un hallazgo cerrado sin trazabilidad es un hallazgo que se ha dado por cerrado.

- **Un hallazgo describía mal el registro que auditaba.** HD-02 decía que RSC-004 y RSC-016 estaban tratados «únicamente con controles organizativos». RSC-004 tiene un control digital; lo que le falta es cobertura física, que es exactamente lo que el validador imprime. Un hallazgo mal redactado en el documento que presume de verificación cruzada vale menos que no tenerlo.

- **El residual de los planes que agrupan escenarios no seguía ninguna regla escrita.** Dos planes cerraban con impacto residual 3 sobre escenarios con impacto 4 sobre personas, contradiciendo la nota del propio plan («ningún control reduce por debajo de 4 el impacto sobre personas»). Se declara la regla que faltaba —el residual de un plan agrupado se valora por el peor de sus escenarios— y se corrigen PT-09 y PT-13. La regla es conservadora y sobrestima el residual de los escenarios menores del grupo; la alternativa, un residual por escenario, multiplicaría las filas sin cambiar ninguna decisión de aceptación.

**La conclusión operativa, que es lo que se lleva el ciclo siguiente:** tres de los cuatro fallos estaban en la *prosa* que describe el registro, no en el registro. La verificación automática comprueba datos contra datos y no habría encontrado ninguno. Lo que los encontró fue leer cada afirmación de la documentación como si fuera una aserción ejecutable y comprobarla a mano una por una. Mientras eso siga siendo trabajo manual, hay que ponerlo en el calendario del ciclo; convertir parte de ello en comprobación automática —empezando por la coherencia entre la SoA y el registro, que ya está registrada como pendiente en HD-06— es la deuda técnica reconocida de la capa 2.

## 20. Lo último que se comprueba es la propia narración

**Decisión:** la ronda que cierra el ciclo no comprueba el registro contra sí mismo ni las reglas contra el registro, sino **el relato del caso contra sí mismo entre documentos**, y el control documental de los registros contra el procedimiento que lo exige. No añade escenarios, controles, objetivos ni valoraciones.

**Por qué:** el mismo hecho se narra en cinco sitios —la ficha de escenario, el diagrama de la cadena, el anexo resuelto de la metodología, el informe a la propiedad y la reconstrucción del cuaderno de indicios— y nadie los había leído en paralelo. Cuando se hace, aparece lo siguiente:

- **La cadena de RSC-001 estaba numerada de tres maneras.** El diagrama y la narrativa del anexo usan seis eslabones; el bloque de tratamiento de ese mismo anexo usaba otra numeración; y el registro usaba una tercera, de cuatro. El mismo control estaba en el eslabón 2 y en el 3, y la detección se atribuía al eslabón 4 en un sitio y al 5 en otro. Es el fallo más caro de todos porque el candado que sostiene la metodología —cada control declara qué eslabón rompe— solo vale si todos cuentan los eslabones igual, y se rompía justo en el escenario estrella. Prevalece la cadena de seis eslabones, que es la que sostiene la ficha de escenario.

- **La narrativa retirada en la v2.0 del escenario seguía viva en tres piezas.** El registro describía la cadena como «identifica al hijo mayor por su exposición pública → contacto y confianza por RRSS → contacto físico», que es la versión que la revisión de campo sustituyó por buenas razones: en la nueva, el intermediario se deja ver físicamente y es este quien busca el contacto. Y ambos colapsaban al instigador y al ejecutor en un solo «actor», con lo que se perdía lo único que hace inalcanzables los dos primeros eslabones. Una revisión que corrige la biblia y no persigue sus citas deja el sistema contando dos historias.

- **El informe a la propiedad contradecía su propio argumento.** Decía que el vigilante «se acordaba de una matrícula», cuando la ficha de escenario declara expresamente que no lo identificó por matrícula sino por saber de quién era el coche. La diferencia no es un detalle: si la detección hubiera sido por matrícula, el problema tendría solución técnica y no haría falta un SGSI. Todo el caso se apoya en que fue conocimiento local no sistematizado.

- **La norma exige que el residual lo acepte el propietario del riesgo, no un órgano.** El plan atribuía la aceptación al Comité en los doce residuales Altos. Se corrige y se conserva la ratificación colegiada como requisito propio añadido, que era la intención original y es más exigente que la norma; lo que no puede es sustituirla.

- **Los registros no cumplían el procedimiento de control documental que el propio sistema aprobó.** Ningún libro llevaba pie con clasificación, código y paginación; cuatro no declaraban autor; el estado «Vigente — aprobado» no existe en el vocabulario de DOC-002 §3; y la hoja de plan de tratamiento seguía usando «Planificado / En curso», el vocabulario que HD-06 dio por retirado del sistema sin advertir que seguía vivo ahí. Un procedimiento de control documental que sus propios registros incumplen es el hallazgo más fácil de encontrar y el más caro de explicar.

- **Deshacer los mapeos forzados destapó dos controles sin soporte real.** La destrucción de soportes en papel estaba trazada a 7.14, «eliminación segura o reutilización de equipos»; el papel no es un equipo, así que se reasigna a 7.10, y para que 7.14 siga soportado se escribe en el anexo del proveedor informático la cláusula de borrado certificado de equipos retirados, que se daba por supuesta y no existía. El mismo cruce dejó al descubierto que el antivirus (8.7) y la instalación de software (8.19) estaban trazados a ese mismo anexo, que no regula ninguno de los dos: pasan a deuda documental, que sube de diez controles a doce. Corregir un mapeo forzado descubre el agujero que el mapeo tapaba, y por eso conviene deshacerlos aunque el cuadre ya saliera.

**La conclusión que se lleva el ciclo siguiente.** La verificación automática comprueba datos contra datos. La verificación manual de reglas comprueba prosa contra datos. Falta la tercera: **prosa contra prosa**, que es la que un lector hace sin proponérselo cuando lee dos documentos seguidos. No hay forma de automatizarla hoy, y es la que más daño hace cuando falla, porque un lector que encuentra dos versiones del mismo hecho deja de creerse las dos. Entra en el calendario del ciclo como paso propio: leer en paralelo los cinco sitios donde se cuenta el mismo suceso, antes de dar ninguna versión por cerrada.

## 21. Lo que la norma exige y ningún documento decía

**Decisión:** la misma ronda que cruza el relato consigo mismo recorre las cláusulas 4 a 10 de la norma una por una, preguntando de cada una «¿qué documento la desarrolla?». Cuatro no tenían respuesta, y se escriben: medición (9.1) en SGSI-DOC-010 §2.3, toma de conciencia (7.3) y recursos (7.1) en SGSI-DOC-003 §6.4 y §6.5, y control operacional (8.1) en SGSI-DOC-004 §9. Y una quinta estaba mal atribuida: la aceptación del riesgo residual.

**Por qué esos cuatro se caen siempre.** No es casualidad que fueran esos. Son las cláusulas que no producen un entregable vistoso: nadie enseña su procedimiento de medición como enseña su análisis de riesgos. Un SGSI de escaparate tiene política, riesgos, SoA y plan de tratamiento —lo que se ve— y se queda corto justo donde la norma pregunta si el sistema funciona. La cláusula 9.1 es el ejemplo puro: este caso llevaba cuatro revisiones presumiendo de una regla verificable por máquina y no había escrito en ninguna parte qué se mide, cada cuánto y quién lo mira. Tenía el instrumento y no tenía el procedimiento.

**Cómo se han escrito.** Sin inventar mecanismos nuevos. Las cuatro mediciones de 9.1 ya existían dispersas —los indicadores del cuadro de objetivos, el validador, el contraste de fechas de verificación del registro, los indicadores de ejecución sostenida—; lo único que faltaba era declararlas como sistema de medición, con su quién y su cuándo. Igual con 8.1: los procesos operativos son los procedimientos que ya estaban escritos, y lo que se añade es la frase que dice que lo son. Un requisito se cubre nombrando lo que ya haces, no montando un aparato paralelo que nadie va a mantener.

**La que estaba mal, y por qué importa.** El sistema atribuía la aceptación del riesgo residual al Comité de Seguridad Convergente. La norma la atribuye al **propietario del riesgo**, en singular, y lo hace a propósito: un riesgo aceptado «por el Comité» es un riesgo que no ha aceptado nadie en particular, y a los seis meses no hay a quién preguntar. El diseño original no era una interpretación laxa sino un instinto equivocado —parecía más serio que lo firmara un órgano—. Se corrige poniendo la aceptación donde la norma la pone y conservando la ratificación colegiada del residual Alto como requisito propio *añadido*, que es más exigente que la norma y era lo que se quería conseguir desde el principio.

**Lo que se lleva el ciclo siguiente.** Las tres verificaciones que este caso ha ido descubriendo —datos contra datos, prosa contra datos, prosa contra prosa— comprueban la coherencia *interna*. Falta la cuarta, que es la que un auditor hace el primer día: **el corpus contra la norma**, cláusula por cláusula, con una tabla que diga dónde se cubre cada una. Esa tabla es ahora un artefacto del sistema y no un ejercicio de una revisión: sin ella, la próxima cláusula que se caiga se caerá igual de silenciosamente que estas cuatro.

## 22. La capa RGPD no hereda la matriz de riesgo patrimonial

**Decisión:** el cierre del bloque RGPD (SGSI-REG-008 RAT, SGSI-DOC-011 ponderación de interés legítimo, SGSI-DOC-012 EIPD) exigió tres decisiones propias, distintas de las de la capa 1 patrimonial:

- **Se designa por primera vez un Responsable del Tratamiento en sentido RGPD.** El sistema ya tenía «Responsable del SGSI» (Dirección General, DOC-003 §6.1), un rol de gobernanza 27001. Nunca había un titular RGPD explícito para los tratamientos de datos personales del propio family office (CCTV, cuaderno de indicios, contratas, visitas). Se asigna a Atalaya GP SL, representada operativamente por Dirección General, citando DOC-003 §6.1 como el precedente que se extiende y no como un rol inventado. Mezclar los dos —usar «Responsable del Tratamiento» para hablar de gobernanza 27001, o «Responsable del SGSI» para hablar de RGPD— es justo la deriva de nomenclatura que las reglas del proyecto prohíben.

- **La EIPD no reutiliza la matriz de riesgo de SGSI-DOC-004 §4.3.** El primer borrador de DOC-012 sí la citaba como base («la matriz habitual de la metodología»), y era un error: esa matriz ancla el impacto en daño patrimonial y físico (pérdida en euros, secuestro), categorías que no describen el riesgo para los derechos de un interesado —estigmatización de un menor, falso positivo en una correlación— que exige el art. 35 RGPD. Forzar el encaje habría sido peor que declarar una escala cualitativa propia (Baja/Media/Alta) y decir por qué no es la otra. La verificación final de coherencia detectó la contradicción —el propio Anexo A de trazabilidad de DOC-012 ya decía «escala, adaptada» mientras el cuerpo del documento decía «matriz habitual»— antes de entregar el documento, no después.

- **El hallazgo HD-08 nace de construir el RAT, no de una auditoría.** Documentar T-10 (relación con el MSP) obligó a comprobar si existía contrato de encargado del tratamiento conforme al art. 28 RGPD, y no existe: el MSP administra correo, NAS y CCTV con acceso administrativo pleno sin ese instrumento. Seis meses de convivencia con el hallazgo del "MSP como nodo de mayor concentración de poder" (mapa de interfaces) sin que nadie escribiera la implicación RGPD tan directa que se deriva de él. Se cascada igual que HD-01 a HD-07: alta en SGSI-REG-006 (deuda de diseño), reflejo en SGSI-DOC-010 §4.1, y aparece como medida mitigadora del riesgo de mayor severidad en DOC-012 §3.

**Por qué importa como patrón, no solo como corrección puntual:** las tres decisiones repiten el mismo mecanismo que ya aparece en las decisiones 19-21 —construir un documento nuevo obliga a comprobar los que ya existían, y esa comprobación encuentra cosas que ninguna revisión aislada habría visto—. La diferencia es que aquí el disparador no fue releer el corpus 27001, sino añadir una capa normativa distinta (RGPD) sobre el mismo objeto (los tratamientos de datos personales que el SGSI patrimonial ya generaba sin haberlos mirado con esa lente).

## 23. La verificación también se verifica a sí misma

**Decisión:** la ronda de verificación cruzada del 21-22/08/2026 no comprobó el registro ni las reglas: comprobó que las correcciones que el propio corpus decía tener cerradas —el parte de cambios sobre los once documentos `.docx` del ciclo de julio— estaban de verdad en el texto vigente, no solo prometidas en un historial de versiones. Cerró tres cosas reales. Primera: una referencia de nomenclatura sin cerrar en SGSI-DOC-012, que citaba «Cian, 17 años» en su tabla de riesgos donde el resto del corpus usa «el hijo mayor» — corregida en el archivo (v1.1). Segunda: dos trazabilidades del Anexo A de SGSI-DOC-006 que no habían cerrado del todo pese a darse por hechas, entre ellas la retirada del control 8.21 de la fila «MSP» — corregidas en el archivo (v1.5). Tercera, y consecuencia directa de la segunda: esa misma retirada dejó huérfana la justificación de 8.21 en la Declaración de Aplicabilidad (SGSI-REG-003), que lo seguía sosteniendo citando un apartado de DOC-006 que ya no lo reclamaba. Se reclasifica a deuda documental — sin soporte identificado, pendiente de asignar documento o control — y se da de alta como decimotercer control en HD-01 (SGSI-REG-006 v1.7).

**Por qué importa como patrón:** un control retirado de un documento no desaparece solo porque se borra de un sitio; hay que perseguir cada referencia cruzada que lo citaba como soporte. Aquí el hilo era corto —el Anexo A de DOC-006 y la columna de trazabilidad de REG-003—, pero es el mismo mecanismo que en un corpus más grande falla en silencio: un control se reclasifica en su documento de origen y sigue viviendo, sin soporte real, en el documento que lo cita. Corregir una fila sin perseguir quién la citaba deja el sistema con la mitad de la corrección.

**Nota de método.** Esta misma ronda generó y descartó un hallazgo propio sobre SGSI-DOC-001 §9, al comparar su afirmación contra la hoja equivocada del registro de riesgos —la hoja «Controles», a nivel de control individual, en vez de la SoA, a nivel de Anexo A: dos «PARCIAL» distintos, en dos documentos distintos, con dos objetos distintos—. Se retractó tras verificar contra la hoja correcta, sin tocar ningún documento por ese motivo. Se deja escrito porque una revisión que solo registra los hallazgos que confirma, y no los que descarta, no es una revisión: es una lista de aciertos.

Versiones vigentes tras esta ronda: SGSI-DOC-005 v1.6, SGSI-DOC-006 v1.5, SGSI-DOC-012 v1.1, SGSI-REG-003 v1.7, SGSI-REG-006 v1.7 — sin cambios en el resto del corpus.

## El caso frente a los datos del sector

El escenario es ficticio; el patrón de amenaza, no. Los informes públicos del sector describen exactamente los riesgos que articulan este caso:

- **La convergencia ciber-física ya no es una tesis, es una categoría de riesgo reconocida.** El informe de riesgo y seguridad para family offices de Simple (2025) señala que los riesgos físicos son crecientemente ciber-físicos, con la domótica y los sistemas de finca inteligente creando nuevos vectores de intrusión, y documenta un caso de principios de 2025 en EE.UU. donde una brecha en la domótica —originada en una app comprometida y facilitada por credenciales filtradas de un contratista— permitió desactivar alarmas perimetrales y entrar físicamente en la residencia con la familia dentro. Ese caso real es, casi literalmente, la combinación de los escenarios RSC-009 y RSC-011 de este registro. [Fuente](https://andsimple.co/reports/risk-and-security/)

- **La frecuencia del ataque a family offices está medida.** Según el informe de ciberseguridad para family offices de Deloitte (2024), citado por Family Wealth Report, el 43% de los family offices a nivel global sufrió un ciberataque en los últimos 12-24 meses (57% en Norteamérica), la mitad de los atacados lo fue tres o más veces, y el phishing apareció en el 93% de los casos. El detonante de este caso y los escenarios RSC-005/006 no son pesimismo de diseño: son la estadística del sector. [Fuente](https://www.familywealthreport.com/article.php/Protecting-Family-Offices-From-Emerging-Cyber-Threats)

- **La suplantación por voz sintética preocupa exactamente donde este caso pone la regla.** Una encuesta de Omega Systems de 2025 recoge que el 83% de los family offices expresa preocupación por campañas de deepfake y suplantación dirigidas a sus principales. La regla R2 del procedimiento de verificación de órdenes de este caso —«la voz no verifica»— responde a ese punto ciego, agravado aquí por un principal con cientos de horas de voz pública. (Misma fuente que la anterior.)

La conclusión de diseño: este caso no inventa amenazas exóticas para lucirse. Toma las tres que el sector ya tiene medidas —ingeniería social dirigida, convergencia ciber-física y suplantación sintética— y muestra cómo se tratan con un sistema de gestión, no con una compra de tecnología.

---

*Estas decisiones están implementadas en los documentos de [`/deliverables/fase1/`](../../deliverables/fase1/); este documento solo las argumenta. Si lees alguna y piensas "eso en mi organización no colaría", esa conversación es exactamente para lo que existe este caso.*
