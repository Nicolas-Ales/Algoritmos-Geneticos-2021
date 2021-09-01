from prettytable import PrettyTable
import cv2
from numpy import random
import random as rd
from TP3 import *
import copy


def Exhaustivo():
    pass


def Heuristico():
    pass


def Genetico(capitales, nroPoblacion, nroCiclos, ruleta, elitismo, probCrossover, probMutacion):
    generaciones = []
    poblacion = GeneroPoblacion(capitales, nroPoblacion)
    funcObjProm = []    # Valor de funcion objetivo promedio
    fitnessProm = []    # Valor de fitness promedio
    cromMax = []        # Cromosoma maximo
    funcObjMax = []     # Valor promedio de funcion objetivo maxima
    funcObjMin = []     # Valor promedio de funcion objetivo minima


    for i in range(nroCiclos):
        funcionesObj = []
        f = 0
        maxO = 0
        minO = 1
        maxCrom = []
        # Hago una lista con todas las funciones objetivo
        for crom in poblacion:
            funcionesObj.append(crom.getFuncObj(capitales))

        # Sumo el valor de todas las funciones para calcular el fitness
        totalObj = sum(funcionesObj)

        # Calculo la funcion fitness de cada cromosoma
        for crom in poblacion:
            crom.getFuncFitness(totalObj, capitales)
            if crom.objetivo > maxO:
                maxO = copy.copy(crom.objetivo)
                maxCrom = copy.copy(crom.objetivo)
            if crom.objetivo < minO:
                minO = copy.copy(crom.objetivo)
            f += crom.fitness

        generaciones.append(i)
        funcObjMax.append(maxO)
        funcObjMin.append(minO)
        cromMax.append(maxCrom)
        funcObjProm.append(sum(crom.objetivo for crom in poblacion)/len(poblacion))
        fitnessProm.append(f/nroPoblacion)


        poblacion = seleccion(poblacion, elitismo, nroPoblacion)
        poblacion = crossover(poblacion)
        poblacion = mutacion(poblacion)


def GeneroPoblacion(capitales, nroPoblacion):
    poblacion = []
    for _ in range(nroPoblacion):
        poblacion.append(Cromosoma(capitales))
    return poblacion

def seleccion(poblacion, ruleta, elitismo, nroPoblacion):
    nuevaGeneracion = []

    if elitismo:
        poblacion.sort(key = lambda cromosoma: cromosoma.objetivo, reverse = True) # Ordeno de menor a mayor? Preguntar
        k = 0
        # Si se usa elitismo, el 20% de la poblacion que tenga el menor? de objetivo pasara a la prox generacion
        for crom in nroPoblacion:
            if k < poblacion * 0.2:
                cElite = copy.copy(crom)
                nuevaGeneracion.append(cElite)
            else:   # Una vez que el 20% de la poblacion pasa a la prox generacion, se utiliza el metodo de 
                    # ruleta o torneo para seleccionar el resto
                for _ in poblacion:
                    if ruleta:                     # Llama al metodo ruleta para hacer la seleccion
                        cRep = ruleta(poblacion)
                    else:                           # Llama al metodo torneo para hacer la seleccion
                        cRep = torneo(poblacion)
                    c = copy.deepcopy(cRep)
                    nuevaGeneracion.append(cRep)
            k += 1
    else:
        for _ in poblacion:
            if ruleta:                     # Llama al metodo ruleta para hacer la seleccion
                cRep = ruleta(poblacion)
            else:                           # Llama al metodo torneo para hacer la seleccion
                cRep = torneo(poblacion)
            c = copy.deepcopy(cRep)
            nuevaGeneracion.append(cRep)

    return nuevaGeneracion

# Seleccion por medio de Ruleta
def ruleta(poblacion):
    sumaFitness = sum(crom.fitness for crom in poblacion)       # Suma las funciones fitness para sacar un nro entre
                                                                # cero y la suma total
    pick = random.uniform(0, sumFitness)
    current = 0
    for cRul in poblacion:              # Cada cromosoma tiene un rango dependiendo de su funcion fitness.
        current += cRul.fitness         # Cuando el nro random este dentor del rango del cromosoma especifico
        if cRul > pick:                 # devolvera ese cromosoma
            return cRul

# Seleccion por medio de Torneo
def torneo(poblacion):
    nroCompetidores = 17                # ¿Hecemos que esta sea una variable global p/ elegir?
    random.shuffle(poblacion)
    competidores = []
    # Meto los primeros 17 cromosomas dentro de la lista de competidores
    for i in range(poblacion):
        competidores.append(i)
    # Ordeno los cromosomas de forma descendiente segun su fitness
    competidores.sort(key = lambda cromosoma: cromosoma.fitness, reverse = True)
    return competidores[0]

def mutacion(poblacion, probMutacion):
    nuevaPoblacion = []

    for crom in poblacion:
        # Me fijo en la probabilidad de que suceda la mutacion
        if random.uniform(0,1) > probMutacion:
            nuevaPoblacion.append(crom)
        else:
            genesMutados = crom.genes
            # Obtengo lista con dos numeros random del 0 al 23 no repetidos
            nros = rd.sample(range(0, len(poblacion) - 1), 2) 
            # Intercambio los valores de la lista en los lugares dados por los nros random
            genesMutados[nros[0]], genesMutados[nros[1]] = genesMutados[nros[1]], genesMutados[nros[0]]
            crom.cambiarGenes(genesMutados)
            nuevaPoblacion.append(crom)


def MuestraDatos(seleccion, capitales):
    print('Camino Seleccionado:')
    distancia = 0
    tabla = PrettyTable(['Capital', 'Distancia Recorrida'])             #Crea una tabla para luego ser mostrada
    for i in range(len(seleccion)):                                     #Recorre las ciudades seleccionadas
        tabla.add_row([capitales[seleccion[i]].Nombre, str(distancia)]) #Agrega la fila a la tabla
        if i < 24:                                            #Como estan descoordinadas a posta la tabla y la distancia
                                                              # la ultima excederia la lista, por eso el if
            distancia += capitales[seleccion[i]].Distancias[seleccion[i + 1]] #Suma la distancia entre la ciudad actual
                                                                              # y siguiente a la total
    print(tabla)                                                              #Muestra la tabla
    print('Distancia total del camino: ', distancia)
    MuestraMapa(seleccion, capitales)


def MuestraMapa(seleccion, capitales):
    coordenadas_capitales = [
        (270, 300),  # 0  Buenos Aires
        (167, 222),  # 1  Cordoba
        (272, 137),  # 2  Corrientes
        (281, 105),  # 3  Formosa
        (274, 307),  # 4  La Plata
        (121, 192),  # 5  La Rioja
        (85, 265),   # 6  Mendoza
        (100, 403),  # 7  Neuqeun
        (239, 235),  # 8  Parana
        (327, 140),  # 9  Posadas
        (158, 501),  # 10 Rawson
        (264, 134),  # 11 Resistencia
        (115, 698),  # 12 Rio Gallegos
        (133, 160),  # 13 Catamarca
        (144, 126),  # 14 Tucuman
        (145, 64),   # 15 Jujuy
        (141, 74),   # 16 Salta
        (87, 235),   # 17 San Juan
        (127, 269),  # 18 San Luis
        (233, 230),  # 19 Santa Fe
        (168, 350),  # 20 Santa Rosa
        (163, 143),  # 21 Santiago del Estero
        (139, 765),  # 22 Ushuaia
        (188, 445),  # 23 Vietma
    ]       #Lista con las coordenadas de cada ciudad en el mapa
    imagen = cv2.resize(cv2.imread('mapa-provincias-argentina.png'), (454, 791)) #Carga la imagen del mapa y la redimenciona
    for i in range(len(seleccion)):     #Recorre la lista con el orden seleccionado de las ciudades
        if i <24:                       #Si no es la ultima ciudad dibuja la linea a la siguiente ciudad
            cv2.line(imagen, coordenadas_capitales[capitales[seleccion[i]].id],
                     coordenadas_capitales[capitales[seleccion[i + 1]].id], (255-i*10, i*10, i*10), 2)
        else:                           #Si es la ultima ciudad dibuja una linea hasta la primera
            cv2.line(imagen, coordenadas_capitales[capitales[seleccion[i]].id],
                     coordenadas_capitales[capitales[seleccion[0]].id], (255-i*10, i*10, i*10), 2)
    for c in coordenadas_capitales:     #Recorre la lista de coordenadas de las capitales
        cv2.circle(imagen, c, 4, (0, 0, 255), -1) #Dibuja un punto en cada capital
    cv2.imshow('imagen', imagen)        #Muestra la imagen con los dibujos
    cv2.waitKey(0)                      #Sin esta linea la ventana se cierra automaticamente
