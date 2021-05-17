def procesar(lista):
    return[len(x) for x in lista if "p" in x]

print(procesar(["hola", "pepe", "ppppp", "chau", "pu"])) #debe devolver [4, 5, 2]
print(procesar([])) #debe devolver []
print(procesar(["hola", "chau"])) #debe devolver []
print(procesar(["pepe", "ppppp"])) #debe devolver [4, 5]

#2.-
#ambos tests fallarán porque el constructor de la clase Fecha crea elementos
#de la clase con el anio en sus 3 atributos (ej. para f=Fecha(25, 5, 1977),
#el objeto de la clase será 1977, 1977, 1977.)
#cuando se pruebe el Equal del primer test será 1980 == 4, cuando se pruebe
#el Equal del segundo test será 1976 == 3.

#3.-
#a)
#la función f_aux tiene complejidad O(T) porque itera sobre todas las cartas
#de un mazo con una T cantidad de elementos debido al while loop de la linea 4.
#la función f itera sobre S cofres debido al for loop de la linea 12 (que a su
#vez contiene la función auxiliar f_aux de complejidad O(T)).
#la función t tiene complejidad O(1) así que no altera el orden de complejidad.
#Por lo tanto la función f tiene complejidad O(S*T).
#b)
#contador_mazos_ordenados_forma_creciente
#la función devuelve el número de los mazos cuyas cartas están completamente
#ordenadas de menor a mayor
#indicador_mazo_ordenado_forma_creciente
#c)
#I el valor de i será igual a len(mazo)-1
#II si todos los mazos tienen una sola carta la función f devolverá el número
#de cofres pues la función f_aux va a devolver true para todos los mazos pues no
#entrará al ciclo while por ser i == len(mazo) y devolverá
#b = 0 == len(mazo - 1) = 0 lo que será True.

#4.-
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
