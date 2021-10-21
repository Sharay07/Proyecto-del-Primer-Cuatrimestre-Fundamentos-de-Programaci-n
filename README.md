# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  21/21ç2)
Autora: Sharay Portillo Jurado;   uvus: shaporjur;

## Estructura de las carpetas del proyecto

* **/src**: Esta carpeta contiene los diferentes módulos de Python que conforman el proyecto.
    * **ventas_mayoristas.py**: Este archivo contiene funciones para explotar los datos sobre las ventas mayoristas.
    * **test_ventas_mayoristas.py**: este archivo contiene funciones de test para probar las funciones del módulo `ventas_mayoristas.py`. Además en este módulo está el main.
* **/data**: Esta carpeta contiene el dataset o datasets del proyecto
    * **poverty_data.csv**: Este archivo contiene los datos de ventas mayoristas que van a ser explotados.

## Estructura del *dataset*

En cada fila del dataset se recogen los datos anonimizados de una persona, es decir, no sabemos sus nombre ni sus apellidos. Para cada persona se registran 9 datos. Por lo tanto, el dataset está compuesto por 9 columnas, con la siguiente descripción:

* **medio_pedido**: de tipo str, representa el medio por el que se han vendido los productos.
* **tipo_tienda**: de tipo str, representa el tipo de tienda en el que se han vendido los productos.
* **tipo_producto**: de tipo str, representa el tipo de producto que se ha vendido los productos.
* **producto**: de tipo date.time, representa el producto que se ha vendido.
* **fecha_compra**: de tipo int, representa la fecha de la venta.
* **unidades_venta**: de tipo int, representa las unidades vendidas del producto
* **precio_unidad**: de tipo float, representa el precio del producto por unidad.
* **margen_de_ganancia**: de tipo float, representa el margen de ganacia que tien el verdedor.
* **libre_de_impuestos**: de tipo boolean, representa si la venta ha sido libre de impuesto o no

## Tipos implementados

Para trabajar con los datos del dataset se ha definido la siguiente tupla con nombre:

VentasMayoristas =  namedtuple('VentasMayoristas', 'medio_pedido, tipo_tienda, tipo_producto, \
                            producto, fecha_compra, unidades_venta, \
                            precio_unidad, margen_de_ganancia, libre_de_impuestos')

en la que los tipos de cada uno de los campos son los siguientes:

`VentasMayoristas(str, str, str, date.time, int, int, float, float, boolen)`

**********************Las decisiones de diseño más destacadas de este tipo son:
* El campo genero es de tipo str, en lugar de boolean como aparece en el dataset original, y puede tomar los valores 'Hombre' o 'Mujer'..********************

## Funciones implementadas

En este proyecto se han implementado las siguientes funciones, que están clasificadas según los bloques y tipos de funciones que se requieren en cada una de las entregas.
El módulo principal es el módulo ventas_mayoristas.py, así que aquí es donde se hará referencia a cada uno de los bloques de las entregas.

### Módulo ventas_mayoristas

#### Entrega del proyecto

* **Comienzo**  
  * **lee_fichero(fichero)**: lee los datos del fichero csv, exactamente de ventas_mayoristas.csv y devuelve una lista de tuplas de tipo VentasMayoristas con los datos del fichero. Para implementar esta función se han definido las siguientes funciones auxiliares en la parte superior del archivo:

    * **import csv**: Función para importar la informcaión del csv
    * **from collections import namedtuple**: Función para poder crear una tupla con nombre
    * **from datetime import datetime**: Función para convertir de cadena a fecha.   
***********************la del boolen

 * **Función 1**

  * **lee_ventas_mayoristas(fichero)**: Dadas una lista de tuplas de tipo **********,


 ### Módulo poverty_test

En el módulo de pruebas se han definido las siguientes funciones de pruebas, cada una de las cuales se usa para probar la función con que tiene el mismo nombre (pero sin comenzar por `test\_` del módulo `ventas_mayoristas`. Por ejemplo, la función `test_lee_ventas_mayoristas` prueba la función `lee_ventas_mayoristas`.

* **test_lee_ventas_mayoristas(fichero)**

En este módulo también se definido dos funciones auxiliares:***************
* **mostrar_registros (registros)**
* **mostrar_diccionario(dicc)**