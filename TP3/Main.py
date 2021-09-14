from TP3.Datos import *
from TP3.Funciones import *


nroPoblacion = 50
nroCiclos = 200
elitismo = True
ruleta = True

probCrossover = 0.5
probMutacion = 0.5

print('id\tNombre de la Capital')
tabla = PrettyTable(['Capital', 'Id'])
for c in capitales:
    tabla.add_row([c.Nombre, c.id])
print(tabla)
seleccionCapital = int(input('Seleccione capital desde la que desea partir (por id): '))
print('Seleccionó ', capitales[seleccionCapital].Nombre)
print('Seleccione un método para la obtención del camino mínimo: ')
print('1- Utilizar Método Exhaustivo')
print('2- Utilizar Algoritmo Genético')
print('3- Utilizar Método Heuristico')
metodo = 0
while metodo != 1 and metodo != 2 and metodo != 3:
    metodo = int(input())
if metodo == 1:
    resultado = Exhaustivo(capitales,seleccionCapital) #resultado tiene que ser una lista con el id de las capitales en el orden seleccionado
    print('Seleccionó Exhaustivo')
elif metodo == 2:
    # resultado = Genetico(capitales,seleccionCapital) #resultado tiene que ser una lista con el id de las capitales en el orden seleccionado
    resultado = Genetico(capitales, nroPoblacion, nroCiclos, ruleta, elitismo, probCrossover, probMutacion)
    print('Seleccionó Genético')
elif metodo == 3:
    resultado = Heuristico(capitales,seleccionCapital) #resultado tiene que ser una lista con el id de las capitales en el orden seleccionado
    print('Seleccionó Heurístico')

#print(resultado1) #Print de prueba para el metodo Heurístico

# resultado = list(range(24))  # Esta es una lista de prueba para testear el muestra datos
resultado.append(resultado[0])  # Con esto resolvemos el que tenga qu evolver, al menos para la parte visual
MuestraDatos(resultado, capitales)
