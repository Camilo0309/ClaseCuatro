class Persona:
    nombre = ""
    edad = 0
    pais = ""

    def __init__(self, nombre, edad, pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais

    # Metodo 1
    def saludar(self):
        print("Hola mi nombre es: {}".format(self.nombre))

    # Metodo 2
    def despedir(self):
        print("Hasta pronto: {}".format(self.nombre))

    # Metodo 3
    def comprar(self):
        print("Puedo comprar X cosa")

# crear la instancia de la clase persona
camilo = Persona('Camilo lasso', 31, 'Colombia')

# para acceder a los atributos.....
print(camilo.nombre)
camilo.saludar()


class Estudiante(Persona):
    colegio = ""

    def __init__(self, nombre, edad, pais,colegio):
        Persona.__init__(self, nombre, edad, pais)
        self.colegio = colegio

    def get_colegio(self):
        print("Su colegio es: {}".format(self.colegio))

#cREAMOS LA HERENCIA
Andrea = Estudiante('Andrea Lasso', 22, 'Pasto','Bethlemitas')
Andrea.saludar()
Andrea.get_colegio()

class Universidad(Estudiante):
    programa = ""

    def __init__(self, nombre, edad, pais, colegio, programa):
        Estudiante.__init__(self, nombre, edad, pais, colegio)
        self.programa = programa


    def get_programa(self):
        print("Su programa es: {}".format(self.programa))

cesmag = Universidad('David lasso', 25, 'Colombia', 'Champagnat', 'Ingenieria electronica')
cesmag.saludar()
cesmag.comprar()
cesmag.despedir()
cesmag.get_colegio()
cesmag.get_programa()

class Cargo:
    nombre_cargo =""

    def __init__(self, nombre_cargo):
        self.nombre_cargo = nombre_cargo

    def get_cargo(self):
        print('Su cargo es: {}'.format(self.nombre_cargo))

class Trabajador(Persona, Cargo):
    sueldo = 0

    def __init__(self, nombre, edad, pais, nombre_cargo, sueldo):
        Persona.__init__(self, nombre, edad, pais)
        Cargo.__init__(self,nombre_cargo)
        self.sueldo = sueldo

    def get_sueldo(self):
        print('Su Salario es de: {}'.format(self.sueldo))

Diana = Trabajador('Diana', 27, 'Colombia', 'Ingeniera', 170000000)
Diana.saludar()
Diana.comprar()
Diana.get_cargo()
Diana.get_sueldo()