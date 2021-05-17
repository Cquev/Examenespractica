#1.-
# idem punto 4 de Examen3

#2.-
def procesar(lista):
    return[x * 3 for x in lista if x >= 10]

print(procesar([1, 4, 10, 20, 21, 30, 9, 10])) #debe devolver [30, 60, 63, 90, 30]
print(procesar([])) #debe devolver []
print(procesar([1, 4])) #debe devolver []
print(procesar([10, 30])) #debe devolver [30, 90]

#3.-
#idem Examen3

#4.- idem otro examen
