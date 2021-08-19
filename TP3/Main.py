from TP3.Datos import *

print('id\tNombre de la Capital')
for c in capitales:
    print(c.id,'\t',c.Nombre)
seleccionCapital = int(input('Seleccione capital desde la que desea partir (por id): '))
print('Seleccionó ', capitales[seleccionCapital].Nombre)
print('Seleccione un método para la obtención del camino mínimo: ')
print('1- Utilizar Método Exhaustivo')
print('2- Utilizar Algoritmo Genético')
print('3- Utilizar Método Heuristico')
metodo = 0
while metodo != 1 and metodo !=2 and metodo !=3:
    metodo = int(input())
if metodo == 1:
    #resultado = Exhaustivo(capitales,seleccionCapital) #resultado tiene que ser una lista con el id de las capitales en el orden seleccionado
    print('Seleccionó Exhaustivo')
elif metodo == 2:
    #resultado = Genetico(capitales,seleccionCapital) #resultado tiene que ser una lista con el id de las capitales en el orden seleccionado
    print('Seleccionó Genético')
elif metodo == 3:
    #resultado = Heuristico(capitales,seleccionCapital) #resultado tiene que ser una lista con el id de las capitales en el orden seleccionado
    print('Seleccionó Heurístico')