# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  21/22)
Autora: Sharay Portillo Jurado;   uvus: shaporjur;

## Estructura de las carpetas del proyecto.

* **src**: esta carpeta contiene los diferentes módulos de Python que conforman el proyecto.
    * **ventas_mayoristas.py**: este archivo contiene funciones para explotar los datos sobre las ventas mayoristas.
    * **test_ventas_mayoristas.py**: este archivo contiene funciones de test para probar las funciones del módulo `ventas_mayorista.py`. Además en este módulo está el main.
* **data**: esta carpeta contiene el dataset del proyecto.
    * **ventas_mayorista.csv**: este archivo contiene los datos de ventas mayoristas que van a ser explotados.

## Estructura del *dataset*.

En cada fila del dataset se recogen los datos de la ventas de unos productos. Para cada venta se registran 9 datos. Por lo tanto, el dataset está compuesto por 9 columnas, con la siguiente descripción:

* **medio_pedido**: de tipo str, representa el medio por el que se han vendido los productos.
* **tipo_tienda**: de tipo str, representa el tipo de tienda en el que se han vendido los productos.
* **tipo_producto**: de tipo str, representa el tipo de producto que se ha vendido los productos.
* **producto**: de tipo str, representa el producto que se ha vendido.
* **fecha_compra**: de tipo date.time, representa la fecha de la venta.
* **unidades_venta**: de tipo int, representa las unidades vendidas del producto.
* **precio_unidad**: de tipo float, representa el precio del producto por unidad.
* **margen_de_ganancia**: de tipo float, representa el margen de ganacia que tien el verdedor.
* **libre_de_impuestos**: de tipo boolean, representa si la venta ha sido libre de impuesto o no.

## Tipos implementados.

Para trabajar con los datos del dataset se ha definido la siguiente tupla con nombre:

VentasMayoristas =  namedtuple('VentasMayoristas', 'medio_pedido, tipo_tienda, tipo_producto, \
                            producto, fecha_compra, unidades_venta, \
                            precio_unidad, margen_de_ganancia, libre_de_impuestos')

En la que los tipos de cada uno de los campos son los siguientes:

`VentasMayoristas(str, str, str, str, date.time, int, float, float, boolean)`

## Funciones implementadas.

En este proyecto se han implementado las siguientes funciones, que están clasificadas según los bloques y tipos de funciones que se requieren.
El módulo principal es el módulo ventas_mayoristas.py, así que aquí es donde se hará referencia a cada uno de los bloques de las entregas.

### Módulo ventas_mayoristas.

* **Encabezado.**  

   * **import csv**: función para importar la informcaión del csv.
   * **from collections import namedtuple**: función para poder crear una tupla con nombre.
   * **from datetime import datetime**: función para convertir una cadena a fecha.   

 * **Funciones.**

  * **lee_ventas_mayoristas(fichero)**:  lee los datos del fichero csv, exactamente de ventas_mayorista.csv y devuelve una lista de tuplas con nombre (VentasMayoristas) con los datos del fichero. Para implementar esta función se han definido las siguientes funciones auxiliares:

   * **if libre_de_impuestos =='true':**
      * **libre_de_impuestos = True**
   * **else:**
      * **libre_de_impuestos = False**
   
   : definimos esta función porque libre_de_impuesto es de tipo boolean, en este caso nos llega la información en tipo str, por tanto comprobamos si la palabra que nos llega es 'true', guardamos el valor del boolean como True y en el caso que no se cumpla lo guardamos como False.

   * **if fecha_compra ==' ':**
      * **fecha_compra = None**
   
   : definimmos esta función debido a que en el csv nos podiamos encontrar alguna casilla sin imformación, el None denota falta de valor o información en dicho lugar.

 ### Módulo test_ventas_mayoristas.

En el módulo de pruebas se han definido las siguientes funciones de pruebas, cada una de las cuales se usa para probar la función con que tiene el mismo nombre pero sin comenzar por `test\_` del módulo `ventas_mayoristas`. 

* **test_lee_ventas_mayoristas(fichero)**: en este caso, la función `test_lee_ventas_mayoristas` prueba la función `lee_ventas_mayoristas` que definimos anteriormente.

En el interior de este módulo podemos ver tres funciones auxiliares más:

 * **print("Se han cargado", len(datos), "registros de ventas mayoristas.")**: muesra el número total de datos que hay en el csv.
 * **print("Mostrando los 3 primeros:")**: muestra las 3 primeras líenas del del csv.
 * **print("Mostrando los 3 útimos:")**: muestra las 3 últimas líenas del del csv.

