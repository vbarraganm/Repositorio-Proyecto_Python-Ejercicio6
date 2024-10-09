from model.universidad import Universidad  
from model.profesor import Profesor
from model.asignatura import Asignatura

def main():

    universidad1 = Universidad() 
    profesor1 = Profesor() 
    asignatura1 = Asignatura()

    universidad2 = Universidad(
        nombre_uni="Universidad de Cartagena",
        ubicacion_uni="Cartagena, Bolívar",
        num_facultades=9,
        num_estudiantes=33500
    )
    
    profesor2 = Profesor(
        nombre_profesor="Jhon Carlos Arrieta Arrieta",
        especialidad="Ingeniería de Sistemas",
        tiempoExperiencia=8,
        email="jarrieta2@unicartagena.edu.co",
    )
    
    asignatura2 = Asignatura(
        nombre_asignatura="Programación Orientada a Objetos",
        descripcion="Curso orientado a la creación de aplicaciones robustas y escalables a partir de conceptos de POO",
        creditos=3,
        profesor_responsable=profesor2
    )

    print("     Código: 7502410031")
    print(" Valentina Barragán Martínez")
    print("*****************************")
    print("")

    universidad1.mostrar_datos()
    print("")
    profesor1.mostrar_datos()
    print("")
    asignatura1.mostrar_datos()
    print("")

    print("*****************************")
    print("")

    universidad2.mostrar_datos()
    print("")
    profesor2.mostrar_datos()
    print("")
    asignatura2.mostrar_datos()
    print("")

if __name__ == "__main__":
    main()
