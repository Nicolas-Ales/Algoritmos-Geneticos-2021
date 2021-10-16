import random as rd
import numpy as np
from TP_Investigacion.nFunciones import *

class Cromosoma:
    def __init__(self,lab,dimension,p1=(0,0),p2=(0,0),reescribir=False):
        if not reescribir:
            self.genes = self.generarGenes(lab,dimension,p1,p2)
            self.objetivo = self.getFuncObjetivo()

    def generarGenes(self,lab,dimension,p1,p2):
        genes = []
        genes.append(p1)
        step = dimension/8
        for i in range(rd.randint(5,20)):
            factible = False
            while not factible:
                n = (rd.randint(0, dimension-1), rd.randint(0, dimension-1)) # n de nodo
                if lab[n] == 0:
                    continue
                linea = get_line(genes[i],n)
                factible = True
                for p in linea:
                    if lab[p] == 0:
                        factible = False
                        break
            if abs(n[0]-p2[0]) < 100 and abs(n[1]-p2[1]) < 100:
                factible = True
                linea = get_line(n,p2)
                for p in linea:
                    if lab[p] == 0:
                        factible = False
                        break
                if factible:
                    genes.append(n)
                    genes.append(p2)
                    break
            genes.append(n)
        return genes

    def getFuncObjetivo(self):
        obj = 0
        nodos = self.genes
        for i in range(len(nodos)-1):
            obj += np.sqrt((nodos[i][0]-nodos[i+1][0])**2 + (nodos[i][1]-nodos[i+1][1])**2)
        return obj

    def cambiarGenes(self, genes):
        self.genes = genes
        self.objetivo = self.getFuncObjetivo()

