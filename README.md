# Trabajo Práctico N°5
Una empresa de producción de noticias necesita un programa que le permita operar con los eventos que ha cubierto. 
De cada Evento, se tiene:

1. codigo = un código de identificación (una cadena que puede tener dígitos y caracteres).
2. titulo = un título (una cadena corta), 
3. descripcion = una descripción o resumen del evento (una cadena con un texto terminado en punto y con palabras separadas por un blanco (por ejemplo: “El terremoto tuvo su epicentro en San Juan y se sintió en todo el norte argentino.”), 
4. costo = el costo de producción por su desarrollo (un valor de tipo float), 
5. tipo_evento = un número entre 0 y 19 que indica el tipo de evento (por ejemplo: 0: Deportivo, 2: Social, 3: Político, etc.), y 
6. segmento = otro número, pero entre 0 y 9 para indicar el segmento diario en el que se emitirá la noticicia o desarrollo para ese evento (por ejemplo: 0: matinal primera hora, 1: matinal media mañana, 2: mediodía, etc.).

En base a lo anterior, desarrollar un programa completo que disponga al menos de dos módulos:

En uno de ellos, definir la clase Evento que represente al registro a usar en el programa, y los métodos y funciones básicos para operar con objetos de ese tipo.
En otro módulo, incluir el programa principal y las funciones generales que sean necesarias. Para la carga de datos, aplique las validaciones que considere necesarias.
El programa debe basarse en un menú de opciones para desarrollar las siguientes tareas:

## Punto 1: Generar un arreglo de Objetos.
Generar un arreglo de objetos que contenga los datos de todos los eventos. Debe generar obligatoriamente los datos en forma aleatoria. El arreglo debe permanecer ordenado por código de identificación en todo momento durante la carga. Debe considerar que esta opción puede ser invocada varias veces a lo largo del programa, y que en cada ejecución pueden agregarse tantos objetos como desee el operador, sin eliminar los datos que ya estaban cargados. Será considerada la eficiencia de la estrategia de carga y los algoritmos que aplique.

## Punto 2: Mostrar el arreglo.
Mostrar el arreglo generado en el punto anterior, a razón de un registro por línea en la consola de salida.

## Punto 3: Generar un archivo binario.
A partir del arreglo, generar un archivo binario de registros que contenga los datos de todos los eventos cuyo monto de producción sea mayor a un valor p que se carga por teclado. Cada vez que esta opción se seleccione, el archivo debe crearse otra vez, eliminando los anteriores registros que hubiese contenido.

## Punto 4: Mostrar los datos del archivo binario.
Mostrar todos los datos del archivo que generó en el punto 3, a razón de un registro por línea.

## Punto 5: Generar un vector de costos/montos.
Recorra el archivo que generó en el punto 3, y genere a partir de él un arreglo unidimensional de valores de tipo float, que contenga en cada casilla solo el monto de producción de los eventos del archivo cuyo tipo de evento sea mayor o igual a 5. Muestre el arreglo generado de esta forma, y al final del listado agregue una línea adicional indicando el promedio de los montos mostrados.

## Punto 6: Busqueda Binaria por codigo.
Determine si existe en el arreglo creado en el punto 1, un evento cuyo código de identificación coincida con el valor cod que se carga por teclado. Si existe, muestre sus datos completos, detenga la búsqueda y retorne la cadena contenida en el campo descripción del evento. Si no existe, informe con un mensaje y retorne la cadena “No existe.”.

## Punto 7: Generar Matriz de Conteo por tipo de evento y segmento diario.
A partir del arreglo creado en el punto 1, determine cuántos eventos existen para cada una de las posibles combinaciones entre tipos de evento y segmentos diarios (un total de 20 * 10 = 200 contadores). Genere todos los contadores posibles, pero muestre solo los resultados que correspondan a los tipos de evento mayores a te, siendo te un número que se carga por teclado.

## Punto 8: Analisis de caracteres.
Tome la cadena retornada en el punto 6, y determine cuántas palabras de esa cadena comenzaban con una letra mayúscula y tenían al menos una "t" y una "s" (en cualquier orden y no necesariamente seguidas).  Como se dijo, la cadena debe terminar con un punto y las palabras deben separarse entre ellas con un (y solo un) espacio en blanco. La cadena debe ser procesada caracter a caracter, a razón de uno por cada vuelta del ciclo que itere sobre ella. Obviamente, el programa debe controlar que la opción 6 haya sido activada antes de ejecutar este proceso, o hacer lo que sea necesario para evitar una clavada si la opción 6 no había sido activada previamente.

### Algoritmos y Estructura de Datos - Universidad Tecnológica Nacional FRC - Argentina - 2023
