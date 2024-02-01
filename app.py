from menu import Menu
from user import User
from pelicula import Pelicula

import texts as t

print(t.bv)
opcion = Menu(t.mpr).imprimirMenu()
if opcion == 1:
    opcion = Menu(t.mu).imprimirMenu()
    if opcion == 1:
        User.modificarUser()
    elif opcion == 2:
        User.deleteUser()
    else:
        pass
elif opcion == 2:
    opcion = Menu(t.mp).imprimirMenu()
    if opcion == 1:
        Pelicula.verDisponibles()
    elif opcion == 2:
        User.modificarPelicula()
    else:
        pass    
elif opcion == 3:
    Pelicula.verTodas()
else:
    print(t.dp)
    quit()
