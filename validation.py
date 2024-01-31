def validarBusqueda(txt, valor):
    with open(f"{txt}", "r") as archivo:
        lineas  = archivo.readlines()
        cont = 0
        for i in lineas:
            i2 = i.split(",")
            if i2[0] == str(valor):
                cont += 1
                return (True, i2, lineas.index(i))
        if cont == 0:
            return (False,0)