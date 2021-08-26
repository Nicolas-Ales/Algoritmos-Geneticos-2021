from numpy import random
import numpy as np

class Cromosoma:
    def __init__(self, capitales):
        # OBTENGO UNA PERMUTACION DE LA LISTA DE CAPITALES
        self.genes = random.permutation(range(24))
        self.objetivo = self.getFuncObjetivo(capitales)



    # OBTENGO VALOR DE LA FUNCION OBJETIVO /// HACER MAS LINDO EL CODIGO
    def getFuncObjetivo(self, capitales):
        distancia = 0
        # RECORRO LA MI LISTA DE INT/IDS
        for i in range(len(self.genes)): # i ES EL ID ACTUAL
            # Cuando llego al penultimo id salgo del loop, asi no se va de rango la lista
            if i == len(self.genes) - 1:
                break
            # Con el id de la lista de genes busco la capital que corresponde al i
            ciudad1 = capitales[self.genes[i]] # Ciudad actual
            ciudad2 = capitales[self.genes[i+1]] # Ciudad proxima
            id2 = ciudad2[0]
            distancia += ciudad1[2][id2]
        # Vuelvo a la primera ciudad desde la ultima
        ciudad1 = capitales[self.genes[-1]]
        ciudad2 = capitales[self.genes[0]]
        id2 = ciudad2[0]
        distancia += ciudad1[2][id2]
        return distancia

    def getFuncFitness(self, total, capitales):
        self.fitness = self.getFuncObjetivo(capitales) / total
        return self.fitness