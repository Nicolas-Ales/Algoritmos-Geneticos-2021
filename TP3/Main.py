from TP3.Datos import *
from TP3.Funciones import *


nroPoblacion = 50
nroCiclos = 200
elitismo = True

probCrossover = 0.8
probMutacion = 0.05


print('Seleccione un método para la obtención del camino mínimo: ')
print('1- Utilizar Método Exhaustivo')
print('2- Utilizar Método Heuristico seleccionando ciudad')
print('3- Camino mínimo con método heurístico.')
print('4- Utilizar Algoritmo Genético')
metodo = 0
while metodo != 1 and metodo != 2 and metodo != 3 and metodo != 4:
    metodo = int(input())
if metodo == 1:
    # resultado = Exhaustivo(capitales,seleccionCapital) #resultado tiene que ser una lista con el id de las capitales en el orden seleccionado
    print('Seleccionó Exhaustivo y no podemos devolverle un resultado por este método')
elif metodo == 2:
    iDCapitalSeleccionada = SeleccionCapital(capitales)
    resultado = Heuristico(capitales, iDCapitalSeleccionada)[0] #resultado tiene que ser una lista con el id de las capitales en el orden seleccionado.
elif metodo == 3:
    resultado = CaminoMinimo(capitales) #resultado tiene que ser un recorrido de ids de capitales y la distancia minima.
    print('Seleccionó Camino Mínimo con Heurístico.')
elif metodo == 4:
    # resultado = Genetico(capitales,seleccionCapital) #resultado tiene que ser una lista con el id de las capitales en el orden seleccionado
    print('Seleccionó Genético')
    resultado = Genetico(capitales, nroPoblacion, nroCiclos, elitismo, probCrossover, probMutacion)
    resultado.append(resultado[0])



print(resultado) #Print de prueba para el metodo Heurístico 

# resultado = list(range(24))  # Esta es una lista de prueba para testear el muestra datos
# resultado.append(resultado[0])  # Con esto resolvemos el que tenga que volver, al menos para la parte visual
MuestraDatos(resultado, capitales)
