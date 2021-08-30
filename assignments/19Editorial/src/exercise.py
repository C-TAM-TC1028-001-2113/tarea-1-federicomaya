def main():
    #Federico Maya Santander A01411914
    # escribe tu código abajo de esta línea
    
    import math
    num_palabras = int(input("Dame el número de palabras: "))
    num_paginas = math.ceil(num_palabras/475)
    costo_publicacion = (num_paginas)*60
    precio_total = (costo_publicacion)*.10
    print("El costo de la publicacion es:", precio_total)
    


if __name__ == '__main__':
    main()
