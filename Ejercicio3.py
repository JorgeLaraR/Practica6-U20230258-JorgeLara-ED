class Estudiante:
    def __init__(self, nombre, apellido, carnet, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.carrera = carrera


    def actualizar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre


    def actualizar_apellido(self, nuevo_apellido):
        self.apellido = nuevo_apellido


    def actualizar_carnet(self, nuevo_carnet):
        self.carnet = nuevo_carnet


    def actualizar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera


    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}\nCarnet: {self.carnet}\nCarrera: {self.carrera}"



estudiante1 = Estudiante("Jorge", "Lara", "U20230258", "Técnico en Desarrollo de Software")
print(estudiante1)

estudiante1.actualizar_nombre("Jorge")
estudiante1.actualizar_carnet("U20230258")
print(estudiante1)