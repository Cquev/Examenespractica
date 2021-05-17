
class Pieza:
    def __init__(self, peso, altura):
        self._peso = peso
        self._altura = altura

    def peso(self):
        return self._peso
    def altura(self):
        return self._altura

def maximo(piezas, umbral):
    peso_maximo = 0
    piezas_que_superan_umbral = 0
    for pieza in piezas:
        if pieza.altura() > umbral and pieza.peso() > peso_maximo:
            peso_maximo = pieza.peso()
            piezas_que_superan_umbral += 1
    if piezas_que_superan_umbral == 0:
        return -1
    else:
        return peso_maximo

piezas = []
piezas.append(Pieza(1, 2))
piezas.append(Pieza(5, 5))
piezas.append(Pieza(7, 5))
piezas.append(Pieza(40, 2))
piezas.append(Pieza(3, 5))
print(maximo(piezas, 3)) # imprime 7
print(maximo(piezas, 2)) # imprime 7
print(maximo(piezas, 1)) # imprime 40
print(maximo(piezas, 7)) # imprime -1
