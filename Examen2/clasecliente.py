class Cliente:
    def __init__(self, codigo, consumo):
        self._codigo = codigo
        self._consumo = consumo

    def codigo(self):
        return self._codigo
    def consumo(self):
        return self._consumo


def consumo_promedio(clientes, codigos):
    consumo_total = 0.0
    clientes_con_codigo = 0
    for cliente in clientes:
        if cliente.codigo() in codigos:
                consumo_total += cliente.consumo()
                clientes_con_codigo += 1
    if clientes_con_codigo != 0:
        return consumo_total / clientes_con_codigo
    else:
        return 0.0

clientes = []
clientes.append(Cliente(1, 60.0))
clientes.append(Cliente(2, 70.0))
clientes.append(Cliente(3, 80.0))
clientes.append(Cliente(4, 90.0))
print(consumo_promedio(clientes, [1])) # imprime 60.0
print(consumo_promedio(clientes, [3,2])) # imprime 75.0
print(consumo_promedio(clientes, [3,4,6])) # imprime 85.0
print(consumo_promedio(clientes, [6,7,8])) # imprime 0.0
print(consumo_promedio(clientes, [1,2,3,4])) # imprime 75.0
