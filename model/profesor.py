class Profesor:
    def __init__(self, nombre_profesor="Profesor desconocido", especialidad="Especialidad no encontrada",
                 tiempoExperiencia = "Tiempo de experiencia desconocido", email="Email desconocido"):
        self._nombre_profesor = nombre_profesor
        self._especialidad = especialidad
        self._tiempoExperiencia = tiempoExperiencia
        self._email = email

    @property
    def nombre_profesor(self):
        return self._nombre_profesor
    
    @nombre_profesor.setter
    def nombre_profesor(self, nombre_profesor):
        self._nombre_profesor = nombre_profesor

    @property
    def especialidad(self):
        return self._especialidad
    
    @especialidad.setter
    def especialidad(self, especialidad):
        self._especialidad = especialidad

    @property
    def tiempoExperiencia(self):
        return self._tiempoExperiencia
    
    @tiempoExperiencia.setter
    def tiempoExperiencia(self, tiempoExperiencia):
        self._tiempoExperiencia = tiempoExperiencia

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    def mostrar_datos(self):
        print(f"El nombre del profesor/a es: {self.nombre_profesor}")
        print(f"La especialidad del profesor/a es: {self.especialidad}")
        print(f"El tiempo de experiencia en años del profesor/a es de: {self.tiempoExperiencia}")
        print(f"El email del profesor/a es: {self.email}")
