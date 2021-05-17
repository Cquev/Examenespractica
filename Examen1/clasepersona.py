
class Persona:
    def __init__(self, dni, deuda):
        self._dni = dni
        self._deuda = deuda

    def dni(self):
        return self._dni
    def deuda(self):
        return self._deuda


def deuda_maxima(personas, DNI):
    deuda_mayor = 0.0
    for persona in personas:
        if persona.dni() in DNI:
            if persona.deuda() > deuda_mayor:
                deuda_mayor = persona.deuda()
    return deuda_mayor

personas = []
personas.append(Persona(1, 10.0))
personas.append(Persona(2, 20.0))
personas.append(Persona(3, 30.0))
personas.append(Persona(4, 40.0))
print(deuda_maxima(personas, [1])) # imprime 10.0
print(deuda_maxima(personas, [3,2])) # imprime 30.0
print(deuda_maxima(personas, [3,4,6])) # imprime 40.0
print(deuda_maxima(personas, [6,7,8])) # imprime 0.0
print(deuda_maxima(personas, [1,2,3,4])) # imprime 40.0
