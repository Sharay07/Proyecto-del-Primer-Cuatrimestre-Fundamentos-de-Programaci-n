from ventas_mayoristas import *  

def main():
    datos = lee_ventas_mayoristas('data/ventas_mayorista.csv')
    print("Se han cargado", len(datos), "registros de ventas mayoristas.")
    print("")

    print("Mostrando los 3 primeros:")
    for r in datos[:3]:
        print("\t", r)
    print("")

    print("Mostrando los 3 últimos:")
    for s in datos[-3:]:
        print("\t", s)
    
if __name__ == '__main__': 
    main()