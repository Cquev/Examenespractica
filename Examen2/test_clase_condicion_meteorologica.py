class CondicionMeteorologica:
    def __init__(self, temperatura, presion, humedad):
        self._temperatura = temperatura
        self._presion = presion
        self._humedad = humedad

    def temperatura(self):
        return self._temperatura
    def presion(self):
        return self._presion
    def humedad(self):
        return self._humedad

cm = CondicionMeteorologica(13, 1016, 70)
print(cm.temperatura())
print(cm.presion())
print(cm.humedad())

def temp_promedio_v1(lista):
    resultado = 0
    i = 0
    while i < len(lista) - 1:
        resultado = resultado + lista[i].temperatura()
        i = i + 1
    return resultado/len(lista)

def temp_promedio_v2(lista):
    resultado = 0
    i = len(lista) - 1
    while i > 0:
        resultado = resultado + lista[i].temperatura()
        i = i - 1
    return resultado/len(lista)

import unittest

class TestCondicionMeteorologica(unittest.TestCase):

    def test_funcionan_igual(self):
        cm1 = CondicionMeteorologica(1, 1024, 50)
        cm2 = CondicionMeteorologica(2, 1024, 50)
        self.assertEqual(temp_promedio_v1([cm1,cm2,cm1]), temp_promedio_v2([cm1,cm2,cm1]))

    def test_v1(self):
        cm1 = CondicionMeteorologica(4, 1024, 50)
        cm2 = CondicionMeteorologica(0, 1024, 50)
        self.assertEqual(temp_promedio_v1([cm1,cm2]), 2)

    def test_v2(self):
        cm1 = CondicionMeteorologica(0, 1024, 50)
        cm2 = CondicionMeteorologica(8, 1024, 50)
        self.assertEqual(temp_promedio_v2([cm1,cm2]), 4)

    def test_v1(self):
        cm1 = CondicionMeteorologica(4, 1024, 50)
        cm2 = CondicionMeteorologica(0, 1024, 50)
        self.assertEqual(type(temp_promedio_v1([cm1,cm2])), type(2))
    def test_v2(self):
        cm1 = CondicionMeteorologica(0, 1024, 50)
        cm2 = CondicionMeteorologica(8, 1024, 50)
        self.assertTrue(temp_promedio_v2([cm1,cm2]) == float(4))

    def test_v1(self):
        cm1 = CondicionMeteorologica(4, 1024, 50)
        cm2 = CondicionMeteorologica(2, 1024, 50)
        self.assertEqual(temp_promedio_v1([cm1,cm2]), 3)
    def test_v2(self):
        cm1 = CondicionMeteorologica(10, 1024, 50)
        cm2 = CondicionMeteorologica(8, 1024, 50)
        self.assertTrue(temp_promedio_v2([cm1,cm2]) == 9)

unittest.main()
