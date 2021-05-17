def procesar(lista):
    return[x // 2 for x in lista if x % 2 == 0]

# print(procesar([4, 1, 10, 17]))
# print(procesar([]))
# print(procesar([2, 2, 2]))
# print(procesar([3, 1]))

#2.-
#a)
# La funcion tendrá complejidad de O(N*(M+M))= O(N*M)
# Esto es así porque el for loop de la línea 14 itera sobre cada uno de los
# anaqueles que hubiera con complejidad O(N).
# Dentro del loop que itera sobre cada anaquel la función listar libros tiene
# complejidad O(M).
# Luego la función f_aux libros itera sobre todos los libros del anaquel
# con complejidad O(M).
# Todas las demás operaciones tienen complejidad O(1).

#b)
#fraccion_de_libros_del_siglo_XX_en_espaniol_en_anaqueles
#La funcion itera sobre todos los anaqueles y devuelve la division de la cantidad
#de libros del siglo XX en espaniol sobre la cantidad total de libros de los
#anaqueles
#contador_de_libros_del_siglo_XX_en_espaniol_por_anaquel
#la funcion itera sobre todos los libros de un anaquel y devuelve el número
#de libros que sean del siglo XX y se encuentren en español

#c)
#I)el valor de la variable l después de salir del ciclo for será la cantidad
#total de libros en todos los anaqueles
#II)La función f devolverá ZeroDivisionError: division by zero
#porque tratará de dividir 0 (r = 0 + k = 0) por 0 (0 + len(libros) que es 0).


#3.-
#a) el primer test será exitoso pues ambas funciones devuelven el mismo
#resultado (1.0). Tanto el segundo como el tercer test fallarán porque la lista
#suma i -1 elementos de la lista y además devuelve un float y no un integer
#pues la operación resultad/len(lista) devuelve un float.

#b)
# def test_v1(self):
#     cm1 = CondicionMeteorologica(4, 1024, 50)
#     cm2 = CondicionMeteorologica(0, 1024, 50)
#     self.assertEqual(type(temp_promedio_v1([cm1,cm2]), type(2)))
# def test_v2(self):
#     cm1 = CondicionMeteorologica(0, 1024, 50)
#     cm2 = CondicionMeteorologica(8, 1024, 50)
#     self.assertTrue(temp_promedio_v2([cm1,cm2]) == float(4))
# Elegí los tests para demostrar por un lado que las funciones devuelven un
#float en vez de un integer y por otro lado que aún si devolvieran un float,
#al no sumar todos los elementos de la lista, el resultado no es el correcto

#Tuve que hacer las funcioens para darme cuenta
# def temp_promedio_v1(lista):
#     resultado = 0
#     i = 0
#     while i < len(lista) -1:
#         resultado = resultado + lista[i]
#         i = i + 1
#     return resultado/len(lista)
#
# def temp_promedio_v2(lista):
#     resultado = 0
#     i = len(lista) - 1
#     while i > 0:
#         resultado = resultado + lista[i]
#         i = i - 1
#     return resultado/len(lista)
# #
# print(temp_promedio_v1([4, 0]))
# print(temp_promedio_v2([4, 0]))

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
