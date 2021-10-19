from ventas_mayoristas import *  #importa el método que he creado

def main():
    datos = lee_ventas_mayoristas('data/ventas_mayorista.csv')
    print("Se han cargado", len(datos), "registros.")
    
if __name__ == '__main__': 
    main()