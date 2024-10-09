from .profesor import Profesor

class Asignatura:
    def __init__(self, nombre_asignatura="Nombre de asignatura no disponible", 
                 descripcion="Descripción no disponible", 
                 creditos=0, 
                 profesor_responsable=None):
        self._nombre_asignatura = nombre_asignatura
        self._descripcion = descripcion
        self._creditos = creditos
        self._profesor_responsable = profesor_responsable if profesor_responsable else Profesor()

    @property
    def nombre_asignatura(self):
        return self._nombre_asignatura

    @nombre_asignatura.setter
    def nombre_asignatura(self, nombre_asignatura):
        self._nombre_asignatura = nombre_asignatura

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    @property
    def creditos(self):
        return self._creditos

    @creditos.setter
    def creditos(self, creditos):
        self._creditos = creditos

    @property
    def profesor_responsable(self):
        return self._profesor_responsable

    @profesor_responsable.setter
    def profesor_responsable(self, profesor_responsable):
        self._profesor_responsable = profesor_responsable

    def mostrar_datos(self):
        print(f"El nombre de la asignatura es: {self.nombre_asignatura}")
        print(f"Descripción de la asignatura: {self.descripcion}")
        print(f"Créditos de la asignatura: {self.creditos}")
        print(f"El profesor responsable de esta asignatura es: {self.profesor_responsable.nombre_profesor}")
