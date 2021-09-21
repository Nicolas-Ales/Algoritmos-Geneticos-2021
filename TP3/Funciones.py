from prettytable import PrettyTable
import cv2
from numpy import random
import random
import copy
from TP3.Clases import Cromosoma
import matplotlib.pyplot as plt


def Exhaustivo():
    pass

def SeleccionCapital(listadoCapitales):
    # Muestra tabla con ID y Nombre de las capitales y habilita la selección de una como capital de origen.
    print('id\tNombre de la Capital')
    tabla = PrettyTable(['Capital', 'Id'])
    for c in listadoCapitales:
        tabla.add_row([c.Nombre, c.id])
    print(tabla)
    numIDCapitalSeleccionada = int(input('Seleccione capital desde la que desea partir (por id): '))
    print('Seleccionó ' + listadoCapitales[numIDCapitalSeleccionada].Nombre + ' como capital de origen.')
    iDCapitalSeleccionada = listadoCapitales[numIDCapitalSeleccionada].id
    return iDCapitalSeleccionada

def Heuristico(listCapitales, idCapitalDeOrigen):
    recorrido = []
    distanciaRecorrida = 0
    recorrido.append(idCapitalDeOrigen)  # Añado al inicio del recorrido la ciudad de origen.

    # Establezco limites del recorrido, me paro en la ultima capital del recorrido y busco su distancia minima o capital más cercana.
    while len(recorrido) < 24:
        distMinima = float('inf')
        idDistMin = None  # esta variable va a determinar a que capital corresponde la distancia minima.
        for indiceDistancia, distancia in enumerate(listCapitales[recorrido[
            -1]].Distancias):  # NOTA: indiceDistancia coincide con idCapital pero no son lo mismo.
            if listCapitales[
                indiceDistancia].id not in recorrido and distancia < distMinima:  # si hay dos capitales a una misma distancia, vamos a la primera enumerada.
                distMinima = distancia
                idDistMin = listCapitales[indiceDistancia].id
        recorrido.append(idDistMin)
        distanciaRecorrida += distMinima

    distanciaRecorrida = distanciaRecorrida + (listCapitales[idDistMin].Distancias[
        idCapitalDeOrigen])  # sumo la distancia entre la última del recorrido y la de origen.
    recorrido.append(idCapitalDeOrigen)  # agrego la vuelta a la capital de origen.

    print('La distancia total recorrida es ' + str(distanciaRecorrida) + ' para el recorrido: ')

    return recorrido, distanciaRecorrida

def CaminoMinimo(listCapitales):
    # Ejecuto el método heurístico y guardo sus resultados para cada capital.
    listRecorridos = []
    listDistanciasTotales = []
    for capital in listCapitales:
        resultadoHeuristico = Heuristico(listCapitales,
                                         capital.id)  # Recibo la tupla de resultados (listadoRecorrido y distanciaDelRecorrido)
        listRecorridos.append(resultadoHeuristico[0])  # Se guardan los datos en dos listas con un indice paralelo.
        listDistanciasTotales.append(resultadoHeuristico[1])
    # Busco cual es el resultado mínimo de distancias y guardo su índice.
    distanciaMinima = float('inf')
    indiceDistanciaMin = None
    for indiceDistancia, distancia in enumerate(listDistanciasTotales):
        if distancia < distanciaMinima:
            distanciaMinima = distancia
            indiceDistanciaMin = indiceDistancia
    # devuelvo la distancia del recorrido y el recorrido realizado que es el mínimo posible entre todos los Heurísticos.
    print('La distancia minima recorrida para el recorrido nro' + str(indiceDistanciaMin) + ' es: ' + str(
        distanciaMinima) + '\n')
    return listRecorridos[indiceDistanciaMin]

def actualizaObjetivo(poblacion,capitales):
    for s in poblacion:
        s.getFuncObjetivo(capitales)

def Genetico(capitales, nroPoblacion, nroCiclos, elitismo, probCrossover, probMutacion):
    generaciones = []
    poblacion = GeneroPoblacion(capitales, nroPoblacion)
    funcObjProm = []  # Valor de funcion objetivo promedio
    fitnessProm = []  # Valor de fitness promedio
    cromMin = []  # Cromosoma minimo
    funcObjMax = []  # Valor promedio de funcion objetivo maxima
    funcObjMin = []  # Valor promedio de funcion objetivo minima

    FO =[]
    for crom in poblacion:
        FO.append(crom.getFuncObjetivo(capitales))
    bestFObj = min(FO)
    bestSeleccion = poblacion[FO.index(bestFObj)].genes

    for i in range(nroCiclos):
        funcionesObj = []
        f = 0
        maxO = 0
        minO = 99999
        minCrom = []
        # Hago una lista con todas las funciones objetivo
        for crom in poblacion:
            funcionesObj.append(crom.getFuncObjetivo(capitales))

        # Sumo el valor de todas las funciones para calcular el fitness
        totalObj = sum(funcionesObj)

        # Calculo la funcion fitness de cada cromosoma
        for crom in poblacion:
            crom.getFuncFitness(totalObj, capitales)
            if crom.objetivo > maxO:
                maxO = copy.copy(crom.objetivo)
            if crom.objetivo < minO:
                minO = copy.copy(crom.objetivo)
                minCrom = copy.copy(crom.genes)
            f += crom.fitness

        #Reviso si hay algun camino con menor distancia que el mejor que tengo
        if minO < bestFObj:
            bestFObj = minO
            bestSeleccion = minCrom

        generaciones.append(i)
        funcObjMax.append(maxO)
        funcObjMin.append(minO)
        cromMin.append(minCrom)
        funcObjProm.append(sum(crom.objetivo for crom in poblacion) / len(poblacion))
        fitnessProm.append(f / nroPoblacion)
        poblacion = seleccion(poblacion, elitismo)
        print(i)
        print(bestSeleccion, ' ', bestFObj)
        print(minO)
        print(maxO)
        poblacion = crossover(poblacion, elitismo, probCrossover)
        poblacion = mutacion(poblacion, probMutacion)
        actualizaObjetivo(poblacion, capitales)

    muestraGraficas(funcObjMax,funcObjMin,funcObjProm, elitismo)
    return bestSeleccion

def muestraGraficas(oMax,oMin,oProm,e):
    plt.plot(oMax, label='Valor Maximo de la FO')
    plt.plot(oMin, label='Valor Minimo de la FO')
    plt.plot(oProm, label='Valor Promedio de la FO')
    plt.autoscale(tight=True)
    plt.ylim(ymin=0)
    plt.legend()
    if e:
        plt.savefig('Graf Genetico Con Elitismo')
    else:
        plt.savefig('Graf Genetico Sin Elitismo')

    plt.show()

def muestraCromosomas(poblacion):
    for i,c in enumerate(poblacion):
        print(i,': ',c.genes, ' ', c.objetivo)

def GeneroPoblacion(capitales, nroPoblacion):
    poblacion = []
    for _ in range(nroPoblacion):
        poblacion.append(Cromosoma(capitales))
    return poblacion

def seleccion(poblacion, elitismo):
    nuevaGeneracion = []
    if elitismo:
        poblacion.sort(key=lambda cromosoma: cromosoma.objetivo) # Ordeno de menor a mayor
        k = 0
        # Si se usa elitismo, el 20% de la poblacion que tenga el menor? de objetivo pasara a la prox generacion
        for crom in poblacion:
            if k < len(poblacion) * 0.2:
                cElite = copy.copy(crom)
                nuevaGeneracion.append(cElite)
            else:  # Una vez que el 20% de la poblacion pasa a la prox generacion, se utiliza el metodo de
                # torneo para seleccionar el resto
                cRep = torneo(poblacion)  # Llama al metodo torneo para hacer la seleccion
                c = copy.deepcopy(cRep)
                nuevaGeneracion.append(c)
            k += 1
    else:
        for _ in poblacion:
            cRep = torneo(poblacion)  # Llama al metodo torneo para hacer la seleccion
            c = copy.deepcopy(cRep)
            nuevaGeneracion.append(c)
    return nuevaGeneracion


# Seleccion por medio de Torneo
def torneo(poblacion):
    nroCompetidores = 5  # ¿Hecemos que esta sea una variable global p/ elegir?
    random.shuffle(poblacion)
    competidores = []
    # Meto los primeros 17 cromosomas dentro de la lista de competidores
    for i in range(nroCompetidores):
        competidores.append(poblacion[i])
    # Ordeno los cromosomas de forma descendiente segun su fitness
    competidores.sort(key=lambda cromosoma: cromosoma.fitness)
    return competidores[0]

def mutacion(poblacion, probMutacion):
    nuevaPoblacion = []

    for crom in poblacion:
        # Me fijo en la probabilidad de que suceda la mutacion
        if random.uniform(0, 1) > probMutacion:
            nuevaPoblacion.append(crom)
        else:
            genesMutados = crom.genes
            # Obtengo lista con dos numeros random del 0 al 23
            n1 = random.randint(0,len(crom.genes)-1)
            n2 = random.randint(0,len(crom.genes)-1)
            # Intercambio los valores de la lista en los lugares dados por los nros random
            genesMutados[n1], genesMutados[n2] = genesMutados[n2], genesMutados[n1]
            crom.cambiarGenes(genesMutados)
            nuevaPoblacion.append(crom)
    return nuevaPoblacion


def crossover(poblacion, elitismo, probCrossover):
    nuevaGeneracion = []
    rango = len(poblacion)
    if elitismo:
        poblacion.sort(key=lambda cromosoma: cromosoma.objetivo)
        for pos, cElit in enumerate(poblacion):
            if pos < rango * 0.2:
                nuevaGeneracion.append(cElit)
                poblacion.remove(cElit)
        rango = (int)(rango * 0.8)
        random.shuffle(poblacion)
    for _ in range((int)(rango / 2)):
        p1 = poblacion.pop(random.randrange(0, len(poblacion)))  # Padre 1: cromosoma
        p2 = poblacion.pop(random.randrange(0, len(poblacion)))  # Padre 2: cromosoma
        if random.uniform(0, 1) <= probCrossover:
            c = 0  # Cursor
            ciclos = []
            x = 0
            while sum([len(s) for s in ciclos]) == 24:
                ciclo = []
                while ciclo[0][0] == ciclo[x][1]:
                    permutacion = [c, p2.index(
                        p1[c])]  # Par con la pocicion del elemento c en p1 y la pocicion de ese elemento en p2
                    ciclo.append(permutacion)
                    c = ciclo[x][1]
                    x += 1
                ciclos.append(ciclo)
            for m, ciclo in enumerate(ciclos):
                if m % 2 == 0:
                    cambios = [c[0] for c in ciclo]
                    for i in cambios:
                        p1[i], p2[i] = p2[i], p1[i]
        nuevaGeneracion.extend([p1, p2])
    return nuevaGeneracion


def MuestraDatos(seleccion, capitales, m,e):
    print('Camino Seleccionado:')
    distancia = 0
    tabla = PrettyTable(['Capital', 'Distancia Recorrida'])  # Crea una tabla para luego ser mostrada
    for i in range(len(seleccion)):  # Recorre las ciudades seleccionadas
        tabla.add_row([capitales[seleccion[i]].Nombre, str(distancia)])  # Agrega la fila a la tabla
        if i < 24:  # Como estan descoordinadas a posta la tabla y la distancia
            # la ultima excederia la lista, por eso el if
            distancia += capitales[seleccion[i]].Distancias[
                seleccion[i + 1]]  # Suma la distancia entre la ciudad actual
            # y siguiente a la total
    print(tabla)  # Muestra la tabla
    print('Distancia total del camino: ', distancia)
    TablaTxt(seleccion,capitales,m,e)
    MuestraMapa(seleccion, capitales,m,e)
    

def TablaTxt(seleccion, capitales, m,elitismo):
    distancia = 0
    if m == 2:
        met = "Heuristico_Con_Seleccion"
    elif m == 1:
        met = "Heuristico_Minimo"
    elif m == 3:
        if elitismo:
            met = "Genetico_Con_Elitismo"
        else:
            met = "Genetico_Sin_Elitismo"
    f = open("Tabla_de_Resultados_{}.txt".format(met), "w")
    f.write('\\begin{table}[]\n')
    f.write('\\begin{tabular}{c|c}\n')
    f.write('Capital & Distancia Recorrida \\\ \hline \n')
    
    for i in range(len(seleccion)):
        f.write('\t{} & {} \\\ \n'.format(capitales[seleccion[i]].Nombre,str(distancia)))
        if i < 24:  # Como estan descoordinadas a posta la tabla y la distancia
            # la ultima excederia la lista, por eso el if
            distancia += capitales[seleccion[i]].Distancias[
                seleccion[i + 1]]  # Suma la distancia entre la ciudad actual y siguiente a la total
    f.write('\end{tabular}\n')
    f.write('\end{table}\n')

def MuestraMapa(seleccion, capitales,m,elitismo):
    if m == 2:
        met = "Heuristico_Con_Seleccion"
    elif m == 1:
        met = "Heuristico_Minimo"
    elif m == 3:
        if elitismo:
            met = "Genetico_Con_Elitismo"
        else:
            met = "Genetico_Sin_Elitismo"
    coordenadas_capitales = [
        (270, 300),  # 0  Buenos Aires
        (167, 222),  # 1  Cordoba
        (272, 137),  # 2  Corrientes
        (281, 105),  # 3  Formosa
        (274, 307),  # 4  La Plata
        (121, 192),  # 5  La Rioja
        (85, 265),  # 6  Mendoza
        (100, 403),  # 7  Neuqeun
        (239, 235),  # 8  Parana
        (327, 140),  # 9  Posadas
        (158, 501),  # 10 Rawson
        (264, 134),  # 11 Resistencia
        (115, 698),  # 12 Rio Gallegos
        (133, 160),  # 13 Catamarca
        (144, 126),  # 14 Tucuman
        (145, 64),  # 15 Jujuy
        (141, 74),  # 16 Salta
        (87, 235),  # 17 San Juan
        (127, 269),  # 18 San Luis
        (233, 230),  # 19 Santa Fe
        (168, 350),  # 20 Santa Rosa
        (163, 143),  # 21 Santiago del Estero
        (139, 765),  # 22 Ushuaia
        (188, 445),  # 23 Viedma
    ]  # Lista con las coordenadas de cada ciudad en el mapa
    imagen = cv2.resize(cv2.imread('mapa-provincias-argentina.png'),
                        (454, 791))  # Carga la imagen del mapa y la redimenciona
    for i in range(len(seleccion)):  # Recorre la lista con el orden seleccionado de las ciudades
        if i < 24:  # Si no es la ultima ciudad dibuja la linea a la siguiente ciudad
            cv2.line(imagen, coordenadas_capitales[capitales[seleccion[i]].id],
                     coordenadas_capitales[capitales[seleccion[i + 1]].id], (255 - i * 10, i * 10, i * 10), 2)
        else:  # Si es la ultima ciudad dibuja una linea hasta la primera
            cv2.line(imagen, coordenadas_capitales[capitales[seleccion[i]].id],
                     coordenadas_capitales[capitales[seleccion[0]].id], (255 - i * 10, i * 10, i * 10), 2)
    for c in coordenadas_capitales:  # Recorre la lista de coordenadas de las capitales
        cv2.circle(imagen, c, 4, (0, 0, 255), -1)  # Dibuja un punto en cada capital
    cv2.circle(imagen, coordenadas_capitales[seleccion[0]], 4, (255, 255, 0), -1)
    cv2.imwrite("{}.jpg".format(met), imagen)
    cv2.imshow('imagen', imagen)  # Muestra la imagen con los dibujos
    cv2.waitKey(0)  # Sin esta linea la ventana se cierra automaticamente
