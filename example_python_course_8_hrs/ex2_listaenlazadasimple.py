class nodo:
    def __init__(self, nombre = None, cedula = None, sig = None):
        self.nombre = nombre
        self.cedula = cedula
        self.sig = sig
    
    def __str__(self):
        return "%s %s" %(self.nombre, self.cedula)

class lsimples:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, elemento):
        if self.cabeza == None:
            self.cabeza = elemento

        if self.cola != None:
            self.cola.sig = elemento

        self.cola = elemento

if __name__ == "__main__":
    ls = lsimples()

    while(True):
        print("----Menu----\n"+"1. Agregar")
        num = input("ingrese la opción: ")
        if num == "1":
            nombre = input("ingrese el nombre: ")
            cedula = input("ingrese la cedula: ")
            nod = nodo(nombre, cedula)
            ls.agregar(nod)
        