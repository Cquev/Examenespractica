
class Fecha:
    def __init__(self, d, m, a):
        self._dia = a
        self._mes = a
        self._anio = a

    def dia(self):
        return self._dia
    def mes(self):
        return self._mes
    def anio(self):
        return self._anio

# def avanzar_dias(personas, DNI):
#     deuda_mayor = 0.0
#     for persona in personas:
#         if persona.dni() in DNI:
#             if persona.deuda() > deuda_mayor:
#                 deuda_mayor = persona.deuda()
#     return deuda_mayor

f = Fecha(25,5,1977)
print(f.dia())
print(f.mes())
print(f.mes())
