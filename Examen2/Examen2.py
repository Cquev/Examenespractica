#1.-
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

#2.-
def procesar(lista):
    return [int(x*x) for x in lista if x < 0]


print(procesar([4.0, -2.0, -10.0, 12.0])) #debe devolver [4, 100]
print(procesar([])) #debe devolver []
print(procesar([-2.0, -2.0, -2.0])) #debe devolver [4, 4, 4]
print(procesar([4.0, 1.0])) #debe devolver []

#3.-
# idem Examen1 (subo el test)

#4.- idem Examen1 (pongo con tus correcciones)
#2.-
#a)
# La funcion tendrá complejidad de O(N*(M+M))= O(N*M)
#vos decís que aclare eso de la estimación N*M asumiendo que todos los
#anaqueles tienen la misma cantidad de libros? Dice la complejidad en el peor
#de los casos y acá el peor de los casos sería el N más grande si la cantidad
#de libros es distinta en cada anaquel.
# Esto es así porque el for loop de la línea 14 itera sobre cada uno de los
# anaqueles que hubiera con complejidad O(N).
# Dentro del loop que itera sobre cada anaquel la función listar libros tiene
# complejidad O(M).
# Luego la función f_aux libros itera sobre todos los libros del anaquel
# con complejidad O(M).
# Todas las demás operaciones tienen complejidad O(1).

#b)
#fraccion_de_libros_sigloXX_lengua_extranjera_en_anaqueles
#La funcion itera sobre todos los anaqueles y devuelve la division de la cantidad
#de libros del siglo XX que no estén en espaniol sobre la cantidad total
#de libros de los anaqueles
#contador_de_libros_sigloXX_lengua_extranjera_por_anaquel
#la funcion itera sobre todos los libros de un anaquel y devuelve el número
#de libros que sean del siglo XX y se encuentren en español

#c)
#I)el valor de la variable l después de salir del ciclo for será la cantidad
#total de libros en todos los anaqueles
#II)La función no devolverá nada porque se produce un error
#del tipo ZeroDivisionError: division by zero #porque tratará de
#dividir 0 (r = 0 + k = 0) por 0 (0 + len(libros) que es 0).
