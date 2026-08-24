# Convergencia ISO 27001 (convergence-check)

Forma parte del [Caso Atalaya](../../README.md), un caso completo de seguridad convergente para un family office.

## Explicación en vídeo

<a href="https://youtu.be/0B5Mc03_dyg">
  <img src="https://img.youtube.com/vi/0B5Mc03_dyg/hqdefault.jpg" width="480" alt="Explicación y ejecución del programa">
</a>

*Recorrido por la herramienta: qué comprueba y por qué*

---

En la gestión de un sistema de gestión de seguridad de la información (SGSI) llega a ser tedioso el comprobar manualmente el estado y la gestión de los controles que se aplican para su correcto desempeño.

Es por eso que he programado una herramienta para la asistencia en la implementación de un SGSI con metodología ISO 27001, a la que, entregándole un archivo de controles, otro de riesgos y una fecha, filtra los riesgos más graves y comprueba si están tratados en su "convergencia". De no ser así, muestra el lado en el cual le falta la cobertura para una posterior revisión.

Como he comentado, me baso en que la cobertura sea en su "convergencia", esto quiere decir que todo riesgo que filtre tiene que cubrir el lado físico y el lado digital. Para filtrarlos he considerado los riesgos etiquetados como "alto" y "crítico", y he desechado los controles organizativos o que no tienen evidencia o verificación en plazo.

## Los archivos son:

- `project.py` — el programa en sí, que ejecuta el código anteriormente mencionado.
- `test_project.py` — el programa que sirve para testear y así comprobar que es eficaz.
- `riesgos.csv` — es el fichero que contiene los escenarios de riesgo con su valoración.
- `controles.csv` — es el fichero que contiene los controles antes de su implementación.
- `controles_junio.csv` — es el fichero que contiene la proyección al cierre del plan de tratamiento, a 30/06/2027.
- `requirements.txt` — los requerimientos para usar este programa en cuestión.

## Las funciones son:

- `clasificacion` — te dice si el riesgo es crítico, alto, moderado o bajo, calculando el impacto por la probabilidad.
- `es_grave` — te recoge como válidos los riesgos altos o críticos; sería el primer filtro.
- `esta_cubierto` — solo recoge los que están implementados, con evidencia y verificación correctas; sería el segundo filtro.
- `tiene_convergencia` — registra si los riesgos ya filtrados tienen controles o no en su parte física y/o digital (esta función no se usa en el informe).
- `diagnostico` — devuelve la frase que explica el estado del riesgo.
- `main` — es la función que recoge los archivos y la fecha entregada y los procesa con las anteriores funciones para imprimir el resultado: una lista que enlaza el código de cada uno de los riesgos filtrados con su estado en cuanto a la implementación física y digital.

## Decisiones que tomé:

Al principio pensé en poner la fecha actualizada con `datetime.now()`, pero eso haría que la caducidad de los plazos y controles se viese afectada por el momento en el que se realizase el test. Por eso, al final decidí que sea el usuario el que ponga la fecha a comparar.

También puse dos archivos diferentes de controles porque los controles van cambiando; en cambio, el escenario sobre el que actúan estos controles es el mismo.

He usado fechas de verificación diferentes porque considero que es muy importante tener en cuenta que cada control tiene unos tiempos diferentes y que, por supuesto, si no tiene registro, nada comprueba que exista realmente.

Utilicé el cálculo "en bruto" del nivel de riesgo en vez de cogerlo directamente de la columna porque considero que hay menos margen de error: si hubiera un error humano al rellenar esa columna, este método lo destaparía en lugar de arrastrarlo.

## Para ejecutar el programa:

```
python project.py riesgos.csv controles.csv 31/07/2026
```
(esta línea mostrará los resultados del sistema antes de implementarse)

```
python project.py riesgos.csv controles_junio.csv 30/06/2027
```
(esta línea mostrará los resultados del sistema ya implementado y en su primera revisión)

## Limitaciones conocidas

Este validador es mi proyecto final de CS50P y hace exactamente una cosa: leer dos CSV, aplicar la regla de convergencia escenario a escenario y decir en qué estado está cada uno. Funciona y los resultados de arriba salen de ejecutarlo, no de escribirlos a mano. Pero es la primera versión de un programa escrito mientras aprendía el lenguaje, y hay cosas que sé que no cubre. Las dejo escritas porque un validador de conformidad que no declara sus puntos ciegos tiene el mismo problema que un registro que nadie cruza.

**No valida el vocabulario de entrada.** Los dominios tienen que venir escritos exactamente como `FISICO`, `DIGITAL` u `ORGANIZATIVO`. Si en el CSV aparece `FÍSICO` con tilde, `Fisico` en minúsculas o con un espacio de más, el programa no falla ni avisa: descarta ese control en silencio y el escenario sale como si le faltara cobertura en ese dominio. Lo mismo con los estados. Es la limitación que más me importa, porque el caso entero se apoya en que el vocabulario del registro está cerrado, y el programa no lo comprueba: se fía.

**Una fecha de verificación en el futuro cuenta como válida.** El cálculo mide los días transcurridos desde la última verificación y los compara con la periodicidad. Si la fecha es posterior a la fecha de corte, el resultado es negativo y pasa el filtro. Un `2027` tecleado donde iba `2026` da conforme un control que nunca se ha verificado.

**«Sin cobertura» tapa dos situaciones distintas.** Un escenario al que no se le ha diseñado ningún control en ninguno de los dos dominios y otro cuyos controles están todos implantados pero con la verificación vencida devuelven la misma respuesta. En este registro son RSC-016 y RSC-018, y la diferencia entre ellos es justo lo que hace interesante el segundo: no es un fallo de operación, es un fallo de verificación. El programa no distingue el motivo; hay que ir al CSV a mirarlo. Es lo primero que cambiaría.

**No maneja errores.** Si el fichero no existe, si la fecha va en otro formato, si falta una columna o si la periodicidad viene vacía, el programa se corta con el mensaje de error de Python. Lo único que comprueba es que se le pasen tres argumentos.

**Siempre termina con código de salida 0.** Encuentre incumplimientos o no. No se puede encadenar a nada que dependa del resultado.

**Las pruebas cubren las funciones, no los bordes.** `test_project.py` comprueba las cinco funciones con casos representativos. No comprueba el límite exacto de vencimiento (cuando los días transcurridos coinciden con la periodicidad), ni los valores frontera de la clasificación, ni la función `main()`.

Ninguna de estas cosas invalida los resultados publicados: los CSV de este repositorio están escritos con el vocabulario correcto y las fechas correctas, y lo he comprobado a mano. Pero es precisamente lo que el propio caso dice de los controles físicos: que algo funcione mientras nadie se equivoque no es lo mismo que funcione.

# NOTA: Todos los escenarios, controles y riesgos son ficticios.
