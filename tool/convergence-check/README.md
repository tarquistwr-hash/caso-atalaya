# Convergencia ISO 27001 (convergence-check)

Forma parte del [Caso Atalaya](../../README.md), un caso completo de seguridad convergente para un family office.

## Explicación en vídeo

<a href="https://youtu.be/0B5Mc03_dyg">
  <img src="https://img.youtube.com/vi/0B5Mc03_dyg/hqdefault.jpg" width="480" alt="Explicación y ejecución del programa">
</a>

*Recorrido por la herramienta: qué comprueba y por qué*

---

Validador de la regla de convergencia del Caso Atalaya. Recibe el registro de riesgos, el registro de controles y una fecha de corte; filtra los escenarios de nivel Alto y Crítico y comprueba si cada uno tiene cobertura efectiva en el dominio físico y en el digital.

Un control solo cuenta como cobertura si está implantado, tiene evidencia registrada y su verificación está dentro de plazo en la fecha indicada. Los controles organizativos no satisfacen ninguna de las dos patas de la regla. Si falta cobertura, el informe indica en qué dominio, para su revisión posterior.

Comprobar esto a mano es viable una vez; con 25 escenarios y 64 controles, deja de hacerse en cuanto el registro crece. Por eso la regla se ejecuta como código.

## Archivos

- `project.py` — el validador.
- `test_project.py` — pruebas con pytest.
- `riesgos.csv` — escenarios de riesgo con su valoración.
- `controles.csv` — controles a fecha de corte (24/07/2026), antes de su implantación.
- `controles_junio.csv` — demostración ficticia a 30/06/2027 con verificaciones vencidas y controles sin implantar; no acredita ejecución ni proyecta el cierre del plan.
- `requirements.txt` — dependencias (solo pytest, para las pruebas).

## Funciones

- `clasificacion` — calcula el nivel del riesgo (Crítico, Alto, Moderado o Bajo) a partir del impacto máximo y la probabilidad.
- `es_grave` — primer filtro: deja pasar solo los riesgos Alto y Crítico.
- `esta_cubierto` — segundo filtro: un control cuenta solo si está implantado, con evidencia y con la verificación en plazo.
- `dominios_cubiertos` — indica si el conjunto de controles de un riesgo cubre el dominio físico y el digital.
- `tiene_convergencia` — devuelve si hay cobertura en ambos dominios.
- `diagnostico` — devuelve el estado del riesgo: cobertura convergente, falta de cobertura física, falta de cobertura digital o sin cobertura.
- `main` — lee los ficheros y la fecha, aplica las funciones anteriores e imprime el código de cada riesgo grave con su diagnóstico.

## Decisiones de diseño

**Fecha de corte como argumento.** Usar `datetime.now()` haría que el resultado cambiase según el día de ejecución. La fecha la indica el usuario, de modo que cada ejecución es reproducible.

**Dos ficheros de controles.** Los controles cambian con el tiempo; el escenario de riesgos sobre el que actúan, no.

**Periodicidad por control.** Cada control tiene su propio plazo de verificación. Sin registro de verificación, nada acredita que el control siga funcionando.

**Nivel de riesgo recalculado.** El nivel se calcula a partir de impacto y probabilidad en lugar de leerlo de la columna del registro: si esa columna tuviera un error humano, el cálculo lo destaparía en lugar de arrastrarlo.

## Ejecución

```
python project.py riesgos.csv controles.csv 31/07/2026
```
Estado real a fecha de corte: ningún control está implantado, así que ningún escenario alcanza cobertura.

```
python project.py riesgos.csv controles_junio.csv 30/06/2027
```
Estado simulado a 30/06/2027, con defectos deliberados para mostrar los cuatro diagnósticos; no es evidencia de implantación.

## Limitaciones conocidas

Este validador es mi proyecto final de CS50P y hace exactamente una cosa: leer dos CSV, aplicar la regla de convergencia escenario a escenario y decir en qué estado está cada uno. Funciona y los resultados de arriba salen de ejecutarlo, no de escribirlos a mano. Pero es la primera versión de un programa escrito mientras aprendía el lenguaje, y hay cosas que sé que no cubre. Las dejo escritas porque un validador de conformidad que no declara sus puntos ciegos tiene el mismo problema que un registro que nadie cruza.

**No valida el vocabulario de entrada.** Los dominios tienen que venir escritos exactamente como `FISICO`, `DIGITAL` u `ORGANIZATIVO`. Si en el CSV aparece `FÍSICO` con tilde, `Fisico` en minúsculas o con un espacio de más, el programa no falla ni avisa: descarta ese control en silencio y el escenario sale como si le faltara cobertura en ese dominio. Lo mismo con los estados. Es la limitación que más me importa, porque el caso entero se apoya en que el vocabulario del registro está cerrado, y el programa no lo comprueba: se fía.

**Validez temporal y evidencia.** Desde la revisión 1.1, una fecha de verificación posterior al corte no acredita cobertura. La evidencia debe contener algún carácter distinto de espacios; una periodicidad negativa tampoco acredita cobertura. El día exacto del vencimiento es válido, el siguiente no. Estas condiciones tienen pruebas de regresión.

**«Sin cobertura» tapa dos situaciones distintas.** Un escenario sin controles diseñados y otro con controles implantados pero verificaciones vencidas devuelven la misma respuesta. En la demostración `controles_junio.csv` son RSC-016 y RSC-018. En el registro de corte `controles.csv`, ninguno de los controles está IMPLEMENTADO. El programa no distingue el motivo; hay que ir al CSV a mirarlo.

**No maneja errores.** Si el fichero no existe, si la fecha va en otro formato, si falta una columna o si la periodicidad viene vacía, el programa se corta con el mensaje de error de Python. Lo único que comprueba es que se le pasen tres argumentos.

**Una ejecución correcta termina con código de salida 0 aunque encuentre falta de cobertura.** Los errores de ejecución sí pueden producir otro código. El programa no ofrece un código específico para automatizar decisiones sobre cobertura.

**Las pruebas no cubren todas las entradas.** `test_project.py` comprueba las seis funciones auxiliares, el vencimiento exacto y el día posterior, fechas futuras, evidencia en blanco y periodicidades cero y negativas. No cubre todas las entradas malformadas ni todos los caminos de `main()`.

**El programa comprueba etiquetas, no la justificación del control.** C-039/C-044 se han reclasificado como ORGANIZATIVO porque su soporte es papel; RSC-019/RSC-020 pasan a mostrar falta de cobertura digital en la demostración. El algoritmo conserva su regla. La revisión semántica del registro sigue siendo necesaria.

## Historial

- **1.2 — 24/09/2026:** la lógica común de `tiene_convergencia` y `diagnostico` pasa a `dominios_cubiertos`, con su prueba; salida con tildes («Falta cobertura física»); mensaje de uso simplificado. Resultados idénticos a la 1.1.
- **1.1 — 20/09/2026:** rechazo de verificaciones futuras y evidencia en blanco; lectura explícita UTF-8; pruebas de regresión; C-006 sincronizado con DOC-008 y REG-001/002; C-039/C-044 reclasificados como ORGANIZATIVO; C-015/C-059 alineados con DOC-007; separación entre registro de corte y demostración futura. Seguimiento de la revisión del corpus en [correcciones](../../docs/fase1-iso27001/correcciones_2026-09.md).
- **1.0:** publicación inicial.

# NOTA: Todos los escenarios, controles y riesgos son ficticios.
