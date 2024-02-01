import const as c

class Pelicula:
    
    def verTodas(self):
        with open(f"{c.p}", "r") as archivo:
            lineas = archivo.readlines()
            for i in lineas:
                print(i[0:-2])

    def verDisponibles(self):
        with open(f"{c.p}", "r") as archivo:
            lineas = archivo.readlines()
            for i in lineas:
                i2 = i.split(",")
                if i2[3] == "L":
                    print(i[0:-2])