import unittest;

class Persona:
    def __init__(self, param_nombre, param_email):
        self.nombre = param_nombre;
        self.email = param_email;
        self.asistencia = 0;
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre;
    def asistencia_clase(self):
        self.asistencia += 1;

class Profesor(Persona):
    def __init__(self, param_nombre, param_email, legajo_empleado):
        self.legajo_empleado = legajo_empleado;
        super().__init__(param_nombre, param_email)

class Alumno(Persona):
    def __init__(self, param_nombre, param_email, numero_alumno):
       self.numero_alumno = numero_alumno;
       super().__init__(param_nombre, param_email)

class Materia:
    def __init__(self, param_nombre, param_codigo):
        self.nombre = param_nombre;
        self.codigo = param_codigo;
    
class test(unittest.TestCase):
    def test_uno(self):
        self.assertTrue(Alumno("Lisandro", "brasolinlisandro0", "68832"))
    def test_dos(self):
        self.assertTrue(Materia("Computación", "234234"));
    def test_tres(self):
        self.assertTrue(Profesor("Gabriel", "dkasd11", "299399"))
if __name__ == '__main__':
    unittest.main()