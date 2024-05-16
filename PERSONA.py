Fr


class Empleado(Persona):
    def __init__(self, id_empleado, sueldo, nombre, genero, edad, direccion):
        self._id_empleado = id_empleado
        self._sueldo = sueldo
        self._nombre = nombre
        self._genero = genero
        self._edad = edad
        self._direccion = direccion

    # Decorador property para el atributo 'id_empleado'
    @property
    def id_empleado(self):
        return self._id_empleado

    # Setter para el atributo 'id_empleado'
    @id_empleado.setter
    def id_empleado(self, value):
        self._id_empleado = value

    # Decorador property para el atributo 'sueldo'
    @property
    def sueldo(self):
        return self._sueldo

    # Setter para el atributo 'sueldo'
    @sueldo.setter
    def sueldo(self, value):
        self._sueldo = value

    # Decorador property para el atributo 'nombre'
    @property
    def nombre(self):
        return self._nombre

    # Setter para el atributo 'nombre'
    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    # Decorador property para el atributo 'genero'
    @property
    def genero(self):
        return self._genero

    # Setter para el atributo 'genero'
    @genero.setter
    def genero(self, value):
        self._genero = value

    # Decorador property para el atributo 'edad'
    @property
    def edad(self):
        return self._edad

    # Setter para el atributo 'edad'
    @edad.setter
    def edad(self, value):
        self._edad = value

    # Decorador property para el atributo 'direccion'
    @property
    def direccion(self):
        return self._direccion

    # Setter para el atributo 'direccion'
    @direccion.setter
    def direccion(self, value):
        self._direccion = value

    def __str__(self):
        return f"Empleado(id_empleado={self.id_empleado}, sueldo={self.sueldo}, nombre='{self.nombre}', genero='{self.genero}', edad={self.edad}, direccion='{self.direccion}')"

# Ejemplo de uso
empleado1 = Empleado(id_empleado=1, sueldo=3000.0, nombre="Juan", genero="Masculino", edad=30, direccion="Av. Principal 123")
print(empleado1)
