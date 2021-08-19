'''
Hacer un programa que utilice un Algoritmo Genético

Canónico para buscar un máximo de la función
f(x) = (x/coef)2 en el dominio [0 , 2^30 -1]
donde coef = 2^30 -1

teniendo en cuenta los siguientes datos:
–Probabilidad de Crossover = 0,75
–Probabilidad de Mutación = 0,05
–Población Inicial: 10 individuos
–Ciclos del programa: 20
–Método de Selección: Ruleta
–Método de Crossover: 1 Punto
–Método de Mutación: invertida

• El programa debe mostrar, finalmente, el Cromosoma correspondiente al valor máximo, el valor máximo,
mínimo y promedio obtenido de cada población.
• Mostrar la impresión de las tablas de mínimos, promedios y máximos
para 20, 100 y 200 corridas.
• Deben presentarse las gráficas de los valores Máximos, Mínimos y Promedios de la
función objetivo por cada generación luego de correr el algoritmo genético 20, 100 y 200 iteraciones (una gráfica por
cada conjunto de iteraciones)
• Realizar comparaciones de las salidas corriendo el mismo programa en distintos ciclos
de corridas y además realizar todos los cambios que considere oportunos en los parámetros de entrada de manera de
enriquecer sus conclusiones.
'''
import random
import pandas as pd
import os
import xlsxwriter
import matplotlib.pyplot as plt
import copy
from numpy import mean

elitismo = True
convergencia = False
ciclos = 200
tipoSeleccion = 1 #Torneo = 1 | Ruleta = 0
torneoParticipantes = 3

probabilidadCrossover = 0.75
probabilidadMutacion = 0.05
poblacionInicial = 10
cantidadGenes = 30
coef = 2 ** 30 - 1


class Cromosoma:
    # valor = int()
    fitness = float()

    # objetivo = float()

    def __init__(self):
        self.genes = []
        for _ in range(cantidadGenes):
            self.genes.append(random.randint(0, 1))
        self.valor = self.getValue()
        self.objetivo = (self.valor / coef) ** 2

    def cambiarGenes(self, genes):
        self.genes = genes
        self.valor = self.getValue()
        self.objetivo = (self.valor / coef) ** 2

    def getValue(self):
        valor = 0
        for posicion, gen in enumerate(self.genes[::-1]):
            valor += gen * 2 ** posicion
        return valor

    def funcObjetivo(self):
        self.objetivo = (self.valor / coef) ** 2
        return self.objetivo

    def funcFitness(self, total):
        self.fitness = self.funcObjetivo() / total
        return self.fitness

def generarPoblacion():
    poblacion = []
    for _ in range(poblacionInicial):
        poblacion.append(Cromosoma())
    return poblacion


# Devuelve el promedio de valores de los cromosomas de la poblacion
def mediaValor(poblacion):
    c = 0
    total = 0
    for crom in poblacion:
        c += 1
        total += crom.valor
    return total / c


# Devuelve el promedio de los valores de las funciones objetivos de los cromosomas de la poblacion
def mediaOjetivo(poblacion):
    c = 0
    total = 0
    for crom in poblacion:
        c += 1
        total += crom.objetivo
    return total / c


# Muestra en consola cada cromosoma de la poblacion, el de valor maximo, el de valor minimo y el promedio
def muestra(poblacion):
    i = 0
    print(
        'Cromosoma \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t valor \t\t\t funcion Objetivo \t\t funcion Fitness ')
    for crom in poblacion:
        print(crom.genes, '\t', round(crom.valor, 16), '\t\t', round(crom.objetivo, 16), '\t', round(crom.fitness, 16))
        if i == 0:
            maxCrom = crom.genes
            minCrom = crom.genes
            maxValue = crom.valor
            minValue = crom.valor
            maxObj = crom.objetivo
            minObj = crom.objetivo
            maxFit = crom.fitness
            minFit = crom.fitness
        elif crom.valor > maxValue:
            maxCrom = crom.genes
            maxValue = crom.valor
            maxObj = crom.objetivo
            maxFit = crom.fitness
        elif crom.valor < minValue:
            minCrom = crom.genes
            minValue = crom.valor
            minObj = crom.objetivo
            minFit = crom.fitness
        i += 1
    print('\n')
    print('Maximo:\t', maxCrom, '\t', round(maxValue, 16), '\t\t', round(maxObj, 16), '\t', round(maxFit, 16))
    print('Minimo:\t', minCrom, '\t', round(minValue, 16), '\t\t', round(minObj, 16), '\t', round(minFit, 16))
    print('Valor Promedio:\t', round(mean(mediaValor(poblacion)), 16), '\nFuncion Objetivo Media',
          round(mean(mediaOjetivo(poblacion)), 16))


# Reproduce a la poblacion
def seleccion(poblacion):
    nuevaGeneracion = []
    if elitismo:  # Consulta si usa o no elitismo
        poblacion.sort(key=lambda cromosoma: cromosoma.objetivo,
                       reverse=True)  # Ordena los cromosomas por funcion objetivo
        k = 0
        # hace que el 20% de la poblacion pase a la siguiente generacion empezando por los mejores
        for cRep in poblacion:
            if k < poblacionInicial * 0.2:
                cElite = copy.copy(cRep)
                nuevaGeneracion.append(cElite)
            else:
                # Con la funcion ruleta recibe un cromosoma para la nueva generacion
                if tipoSeleccion == 0:
                    c = copy.deepcopy(ruleta(poblacion)) #Llama al metodo ruleta para hacer la seleccion
                elif tipoSeleccion == 1:
                    c = copy.deepcopy(torneo(poblacion)) #Llama al metodo torneo para hacer la seleccion
                nuevaGeneracion.append(c)
            k += 1
    else:
        for _ in poblacion:
            # Con la funcion ruleta recibe un cromosoma para la nueva generacion
            if tipoSeleccion == 0:
                cRep = ruleta(poblacion) #Llama al metodo ruleta para hacer la seleccion
            elif tipoSeleccion == 1:
                cRep = torneo(poblacion) #Llama al metodo torneo para hacer la seleccion
            c = copy.deepcopy(cRep)
            nuevaGeneracion.append(c)
    return nuevaGeneracion

#Seleccion por medio de Torneo
def torneo(poblacion):
    nroCompetidores = torneoParticipantes     #el nro de cromosomas que van a participar en el torneo
    random.shuffle(poblacion)
    competidores = []
    for i in range(nroCompetidores): 
        competidores.append(poblacion[i]) #meto los tres primeros cromosomas de una poblacion en la lista competidores
    competidores.sort(key = lambda cromosoma: cromosoma.fitness, reverse = True) #ordena los cromosomas de forma descendiente por fitness
    return competidores[0]




# Devuelve un cromosoma utilizando el metodo de la ruleta
def ruleta(poblacion):
    sumFitness = sum(crom.fitness for crom in
                     poblacion)  # suma todas las funciones fitness para sacar un numero entre 0 y dicha suma
    pick = random.uniform(0, sumFitness)
    current = 0
    # cada cromosoma tiene un rango dependiendo su funcion fitness, cuando el numero random este dentro del rango de un
    # cromosoma especifico devolvera ese cromosoma
    for cRul in poblacion:
        current += cRul.fitness
        if current > pick:
            return cRul


def crossover(poblacion):
    nuevaGeneracion = []
    rango = poblacionInicial
    if elitismo:
        poblacion.sort(key=lambda cromosoma: cromosoma.objetivo, reverse=True)
        for pos, cElit in enumerate(poblacion):
            if pos < poblacionInicial * 0.2:
                nuevaGeneracion.append(cElit)
                poblacion.remove(cElit)
        rango = poblacionInicial - (int)(poblacionInicial * 0.2)
        random.shuffle(poblacion)
    for _ in range((int)(rango / 2)):
        padre1 = poblacion.pop(random.randrange(0,len(poblacion)))
        padre2 = poblacion.pop(random.randrange(0,len(poblacion)))
        if random.uniform(0, 1) <= probabilidadCrossover:
            x = random.randint(0, cantidadGenes)
            genes1 = []
            genes2 = []
            genes1.extend(padre1.genes[0:x])
            genes1.extend(padre2.genes[x:cantidadGenes])
            genes2.extend(padre2.genes[0:x])
            genes2.extend(padre1.genes[x:cantidadGenes])
            hijo1 = Cromosoma()
            hijo1.cambiarGenes(genes1)
            hijo2 = Cromosoma()
            hijo2.cambiarGenes(genes2)
            nuevaGeneracion.extend([hijo1, hijo2])
        else:
            nuevaGeneracion.extend([padre1, padre2])
    return nuevaGeneracion


def mutacion(poblacion):
    nuevaGeneracion = []
    if elitismo:
        k = 0
        poblacion.sort(key=lambda cromosoma: cromosoma.objetivo,
                       reverse=True)  # Ordena los cromosomas por funcion objetivo
        for cMut in poblacion:
            if k < poblacionInicial * 0.2:
                nuevaGeneracion.append(cMut)
            else:
                if random.randint(0, 100) > probabilidadMutacion * 100:
                    nuevaGeneracion.append(cMut)
                else:
                    x = random.randint(0, cantidadGenes - 1)
                    genesMutados = cMut.genes
                    if genesMutados[x] == 0:
                        genesMutados[x] = 1
                    else:
                        genesMutados[x] = 0
                    cMut.cambiarGenes(genesMutados)
                    nuevaGeneracion.append(cMut)
            k += 1
    else:
        for cMut in poblacion:
            if random.randint(0, 100) > probabilidadMutacion * 100:  # corrobora si hay mutacion
                nuevaGeneracion.append(cMut)
            else:
                # si hay mutacion elige un punto donde cambiar 1 por 0 o al reves y hace el cambio
                x = random.randint(0, cantidadGenes - 1)
                genesMutados = cMut.genes
                if genesMutados[x] == 0:
                    genesMutados[x] = 1
                else:
                    genesMutados[x] = 0
                cMut.cambiarGenes(genesMutados) # cambiar genes vuelve a calcular su valor, funcion objetiva
                nuevaGeneracion.append(cMut)
    return nuevaGeneracion


def muestraGrafica(v, o, f, vMax, vMin, gMax):
    plt.plot(o, label='Valor Promedio de la FO')
    plt.plot(vMax, label='Valor Maximo de la FO')
    plt.plot(vMin, label='Valor Minimo de la FO')
    plt.autoscale(tight=True)
    plt.ylim(ymin=0, ymax=1)
    plt.legend()
    plt.show()


def toExcel(g, vProm, oProm, oMax, oMin, gMax):
    Datos = pd.DataFrame({'Generacion': g, 'Valor Promedio': vProm, 'Valor Promedio de la FO': oProm,
                          'Valor Maximo de la FO': oMax, 'Valor Minimo de la FO': oMin, \
                          'Cromosoma de mayor FO': gMax})

    Tabla = pd.ExcelWriter(r'C:\Users\barbi\OneDrive\Escritorio\AG\Geneticos.xlsx', engine='xlsxwriter')
    Datos.to_excel(Tabla, sheet_name='Valores', index=False)
    workbook = Tabla.book
    worksheet = Tabla.sheets["Valores"]
    formato = workbook.add_format({"align": "center"})
    worksheet.set_column("A:B", 15, formato)
    worksheet.set_column("C:C", 18, formato)
    worksheet.set_column("D:F", 15, formato)
    worksheet.set_column("G:G", 64, formato)
    worksheet.conditional_format("C1:C" + str(len(oProm) + 1), {"type": "3_color_scale"})
    # worksheet.conditional_format("B1:B" + str(len(vProm) + 1), {"type": "3_color_scale"})
    Tabla.save()


if __name__ == '__main__':

    poblacion = generarPoblacion()  # Genera la poblacion incial
    # Inicializa listas
    vProm = [] #valor promedio
    oProm = [] #valor de funcion de objetivo promedio
    fProm = [] #fitness promedio
    gMax = []  #genes de cromosoma max
    oMax = []  #valor de funcion objetivo promedio
    oMin = []  #valor de funcion objetivo minimo
    generaciones = []
    count = 0  # Contador de veces que el promedio de la funcion objetivo fue mayor a 0.99
    for i in range(ciclos):
        print('\n\n')
        print('Ciclo:', i)
        # incializa acumuladores poara sacar promedios y variables de maximas y minimas
        f = 0
        maxO = 0
        maxC = []
        minO = 1
        funcionesObjetivos = []
        for crom in poblacion:
            funcionesObjetivos.append(crom.funcObjetivo())

        totalObj = sum(funcionesObjetivos)  # Calcula la suma de funciones objetivo para poder calcular la fitness

        for crom in poblacion:
            crom.funcFitness(totalObj)  # Calcula la fitness de todos los cromosomas
            if crom.objetivo > maxO:  # Compara si es la funcion objetivo maxima o minima
                maxO = copy.copy(crom.objetivo)
                maxC = copy.copy(crom.genes)
            if crom.objetivo < minO:
                minO = copy.copy(crom.objetivo)
            f += crom.fitness

        # Agregan valores de este ciclo a las listas
        generaciones.append(i)
        vProm.append(mediaValor(poblacion))
        oProm.append(mediaOjetivo(poblacion))
        fProm.append(f / poblacionInicial)
        oMax.append(maxO)
        oMin.append(minO)
        cromStr = [str(int) for int in maxC]
        maxC = ''.join(cromStr)
        gMax.append(maxC)
        muestra(poblacion)
        if convergencia:
            if maxO == 1 and mediaOjetivo(poblacion) >= 0.99:
                count += 1
            if count >= 50:  # Si hace 50 generaciones que el promedio de objetivos es mayor a 0.99 y el maximo es 1
                # termina la simulacion
                break
        poblacion = seleccion(poblacion)
        poblacion = crossover(poblacion)
        poblacion = mutacion(poblacion)
    toExcel(generaciones, vProm, oProm, oMax, oMin, gMax)  # Crea el Excel
    muestraGrafica(vProm, oProm, fProm, oMax, oMin, gMax)  # Crea la grafica

    # Cuando se cierra la grafica se ejecuta esto que borra el excel para no llenar de excels el escritorio
    print('Pulse una tecla para finalizar el programa y eliminar el archivo de excel generado')
    # input()
    os.remove(r'C:\Users\barbi\OneDrive\Escritorio\AG\Geneticos.xlsx')
    print('Excel eliminado')
