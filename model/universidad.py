class Universidad:
    def __init__(self, nombre_uni="Universidad desconocida", ubicacion_uni="Ubicación no asignada", num_facultades=0, num_estudiantes=0):
        self._nombre_uni = nombre_uni
        self._ubicacion_uni = ubicacion_uni
        self._num_facultades = num_facultades
        self._num_estudiantes = num_estudiantes

    @property
    def nombre_uni(self):
        return self._nombre_uni
    
    @nombre_uni.setter
    def nombre_uni(self, nombre_uni):
        self._nombre_uni = nombre_uni

    @property
    def ubicacion_uni(self):
        return self._ubicacion_uni
    
    @ubicacion_uni.setter
    def ubicacion_uni(self, ubicacion_uni):
        self._ubicacion_uni = ubicacion_uni

    @property
    def num_facultades(self):
        return self._num_facultades

    @num_facultades.setter
    def num_facultades(self, num_facultades):
        self._num_facultades = num_facultades

    @property
    def num_estudiantes(self):
        return self._num_estudiantes
    
    @num_estudiantes.setter
    def num_estudiantes(self, num_estudiantes):
        self._num_estudiantes = num_estudiantes

    def mostrar_datos(self):
        print(f"El nombre de la universidad es: {self.nombre_uni}")
        print(f"La universidad está ubicada en: {self.ubicacion_uni}")
        print(f"Número de facultades de la universidad: {self.num_facultades}")
        print(f"Número de estudiantes de la universidad: {self.num_estudiantes}")
