def main():
    # Federico Maya Santander A01411914
    # escribe tu código abajo de esta línea
 
 mensajes = int(input("Dame número de mensajes: "))
 megas = float(input("Dame el número de megas: "))
 minutos = int(input("Dame el número de minutos: "))
 costo = (mensajes + megas + minutos) * 0.80
 print("El costo mensual es:", costo)


if __name__ == '__main__':
    main()
