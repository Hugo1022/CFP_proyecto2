import validation as v
import const as c

class User():
    def __init__(self, dni, nombre, direccion, telefono):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.situacion = "L"
        self.alquiler = " "

    def crearUser():
        dni = int(input("ingrese su dni:\n"))
        validacion = v.validarBusqueda(c.u, dni)
        if validacion[0] != True:
            nombre = str(input("ingrese su nombre:\n"))
            direc = input("ingrese su direccion:\n")
            tel = int(input("ingrese su telefono:\n"))
            newUser = User(dni, nombre, direc, tel)
            with open(f"{c.u}", "a") as archivo:
                archivo.write(f"{newUser.dni},{newUser.nombre},{newUser.direccion},{newUser.telefono},{newUser.situacion},{newUser.alquiler}\n")
            print("usuario creado correctamente")
            return (True, newUser)
        else:
            print("el usuario ya existe")
            return (False,0)

    def modificarUser(self):
        on = 1
        while on == 1:
            on = 0
            opcion = int(input("que dato desea modificar?\n1.direcion\n2.telefono\n"))
            if opcion == 1:
                newdire = input("ingrese su nueva direccion:\n")
                self.direccion = newdire
            elif opcion == 2:
                newtel = int(input("ingrese su nuevo telefono:\n"))
                self.telefono = newtel
            else:
                on = 1
                print("elija una opcion correcta")
        with open(f"{c.u}", "r") as archivo:
            lineas = archivo.readlines()
            for i in lineas:
                i2 = i.split(",")
                if i2[0] == str(self.dni):
                    newdato = str(self.dni), self.nombre, self.direccion, str(self.telefono), self.situacion, self.alquiler + "\n"
                    lineas[lineas.index(i)] = ",".join(newdato)
                    with open(f"{c.u}", "w") as archivo2:
                        for j in lineas:
                            archivo2.write(j)
        print("usuario modificado correcetamente")

    def deleteUser(self):
        with open(f"{c.u}", "r") as archivo:
            lineas = archivo.readlines()
            for i in lineas:
                i2 = i.split(",")
                if i2[0] == str(self.dni):
                    lineas.pop(lineas.index(i))
                    with open(f"{c.u}", "w") as archivo2:
                        for j in lineas:
                            archivo2.write(j)
                    print("usuario borrado correctamente")

    def modificarPelicula(self):
        cod = int(input("ingrese el codigo de la pelicula\n"))
        validacion = v.validarBusqueda(c.p, cod)
        if validacion[0] == True:
            desea = input("usted desea 1.alquilar o 2.devolver ?\n")
            if desea == 1:
                if validacion[1][3] == "L":
                    validacion[1][3] = "A"
                    validacion[1][4] = self.dni + "\n"
                    self.situacion = "A"
                    self.alquiler = cod
                else:
                    print("la pelicula no se puede alquilar")
            else:
                validacion[1][3] = "L"
                validacion[1][4] = " \n"
                self.situacion = "L"
                self.alquiler = " "
            with open(f"{c.p}", "r") as archivo:
                lineas = archivo.readlines()
                lineas[validacion[2]] = ",".join(validacion[1])
                with open(f"{c.p}", "w") as archivo2:
                    for i in lineas:
                        archivo2.write(i)
            with open(f"{c.u}", "r") as archivo:
                lineas = archivo.readlines()
                for i in lineas:
                    i2 = i.split(",")
                    if i2[0]:
                        newline = str(self.dni), self.nombre, self.direccion, str(self.telefono), self.situacion, self.alquiler + "\n"
                        lineas[lineas.index[i]] = ",".join(newline)
                        with open(f"{c.u}", "w") as archivo2:
                            for i in lineas:
                                archivo2.write(i)