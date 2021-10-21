import csv
from collections import namedtuple
from datetime import datetime

VentasMayoristas =  namedtuple('VentasMayoristas', 'medio_pedido, tipo_tienda, tipo_producto, \
                            producto, fecha_compra, unidades_venta, \
                            precio_unidad, margen_de_ganancia, libre_de_impuestos')

def lee_ventas_mayoristas(fichero):
    
    with open(fichero, encoding='utf-8') as f:
        
        lector = csv.reader(f , delimiter=";")    
        next(lector)
        registro=[]
        for medio_pedido, tipo_tienda, tipo_producto, producto, fecha_compra, unidades_venta, \
            precio_unidad, margen_de_ganancia, libre_de_impuestos in lector:
            
            fecha_compra = datetime.strptime(fecha_compra, "%d/%m/%Y").date()
            unidades_venta = int(unidades_venta)
            precio_unidad = float(precio_unidad)
            margen_de_ganancia = float(margen_de_ganancia)
                         
            tupla = VentasMayoristas(medio_pedido, tipo_tienda, tipo_producto, producto, fecha_compra,\
                 unidades_venta, precio_unidad, margen_de_ganancia, libre_de_impuestos)

            registro.append(tupla)

    return registro