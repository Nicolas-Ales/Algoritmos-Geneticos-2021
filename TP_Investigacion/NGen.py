import copy
import numpy as np
import random
from TP_Investigacion.nFunciones import *
from TP_Investigacion.GeneradorTerrenoFractal import hacerImagen
from TP_Investigacion.nCromosoma import Cromosoma
from PIL import Image, ImageDraw, ImageFont

nroPoblacion = 50
ciclos = 100
rango = 0.1 #porcentaje de poblacion por rango
probabilidad_crossover = 0.9
probabilidad_mutacion_largo = 0.02
probabilidad_mutacion_gen = 0.05
step = 20    #de cuanto es el step de la step mutation

graf_rate = 10 #Cada cuantas generaciones grafica

def generar_ciudad(lab, dim):
    c = (0, 0)
    while lab[c] != 1:
        c = (np.random.randint(0, dim), np.random.randint(0, dim))
    return c


def generarPoblacion(lab, dim, nro, c1, c2):
    n = 0
    poblacion = []
    while n < nro:
        crom = Cromosoma(lab, dim, c1, c2)
        if c2 in crom.genes:
            poblacion.append(crom)
            n += 1
            print('Cromosoma Aceptado nro: ', n)
    return poblacion


def seleccion(poblacion,rango):
    nuevaPoblacion = []
    poblacion.sort(key=lambda c: c.objetivo) #Ordeno de Menor a Mayor
    rem = 0 #contador para empezar a elegir a los primeros
    for i,c in enumerate(poblacion):
        if i >= len(poblacion)*(1-rango):
            nuevoC = copy.deepcopy(poblacion[rem])
            nuevaPoblacion.append(nuevoC)
            rem+=1
        else:
            nuevaPoblacion.append(c)
    return nuevaPoblacion


def crossover(lab, dim,pob,pCross,rango):
    nuevaPoblacion = []
    poblacion = copy.copy(pob)
    elite = len(poblacion)*rango
    for pos, crom in enumerate(poblacion):
        if pos < elite:
            nuevaPoblacion.append(copy.deepcopy(crom))
            poblacion.remove(crom)
    np.random.shuffle(poblacion)
    cantCrom = len(poblacion)
    contador = 1
    while contador < cantCrom:
        contador += 2
        p1 = poblacion.pop()  # Padre 1
        p2 = poblacion.pop()  # Padre 2
        if np.random.uniform(0,1) <= pCross:
            if len(p1.genes) > len(p2.genes):
                lenMaximo = len(p2.genes)-1
            else:
                lenMaximo = len(p1.genes)-1
            factible = False
            count = 0
            while not factible:
                if count > lenMaximo:
                    break
                count += 1
                if 1 < lenMaximo-1 :
                    x = np.random.randint(1, lenMaximo-1)
                    genes1 = []
                    genes2 = []
                    genes1.extend(p1.genes[0:x])
                    genes1.extend(p2.genes[x+1:len(p2.genes)])
                    genes2.extend(p2.genes[0:x])
                    genes2.extend(p1.genes[x+1:len(p1.genes)])
                    linea1 = get_line(genes1[x-1],genes1[x])
                    linea2 = get_line(genes2[x-1],genes2[x])
                    factible = True
                    factible = linea_factible(genes1[x-1],genes1[x],lab)
                    if factible:
                        factible = linea_factible(genes2[x-1],genes2[x],lab)

            if factible:
                h1 = Cromosoma(lab, dim, reescribir=True)
                h1.cambiarGenes(genes1)
                h2 = Cromosoma(lab, dim, reescribir=True)
                h2.cambiarGenes(genes2)
                nuevaPoblacion.extend([h1, h2])
                print('\033[1;31m hay crossover \033[0m')
            else:
                nuevaPoblacion.extend([p1, p2])
        else:
            nuevaPoblacion.extend([p1, p2])
    return nuevaPoblacion


def mutacionLargo(poblacion,pMut,cActual,cTotales):
    nuevaPoblacion = []
    if cActual < 20:
        elimProb = 1 - cActual/cTotales
    else:
        elimProb = 0.1
    for c in poblacion:
        if np.random.uniform(0,1) <= pMut:
            genes = c.genes
            if np.random.uniform(0,1) < elimProb:
                p1 = genes[0]
                p2 = genes[len(genes)-1]
                nodoMasLejPos = 0
                distMax = 0
                for i,g in enumerate(genes):
                    distTotal = abs(g[0]-p1[0]) + abs(g[0]-p2[0]) + abs(g[1]-p1[1]) + abs(g[1]-p2[1])
                    if distTotal > distMax:
                        nodoMasLejPos = i
                        distMax = distTotal
                if nodoMasLejPos != 0 and nodoMasLejPos < len(genes)-1:
                    factible = True
                    linea = get_line(genes[nodoMasLejPos-1],genes[nodoMasLejPos+1])
                    for p in linea:
                        if lab[p] == 0:
                            factible = False
                            break
                    if factible:
                        print('f obj vieja: ',c.objetivo)
                        genes.pop(nodoMasLejPos)
                        c.cambiarGenes(genes)
                        print('f obj nueva: ', c.objetivo)
            else:
                if len(genes) == 2:
                    puntero = 1
                else:
                    puntero = np.random.randint(1,len(genes)-1)
                linea = get_line(genes[puntero-1],genes[puntero])
                if len(linea)-2 > 1:
                    nuevoIndice = np.random.randint(1,len(linea)-1)
                    nuevoNodo = linea[nuevoIndice]
                    genes.insert(puntero, nuevoNodo)
                c.cambiarGenes(genes)
        nuevaPoblacion.append(c)
    return nuevaPoblacion


def mutacionGen(poblacion,pMut,step,lab):
    nuevaPoblacion = []
    for c in poblacion:
        newGenes = []
        for i,g in enumerate(c.genes):
            if np.random.uniform(0,1) <= pMut and c.genes.index(g) > 0 and c.genes.index(g) < len(c.genes)-2:
                if g[0] <= c.genes[len(c.genes)-1][0]:
                    movX = 1
                else:
                    movX = -1
                if g[1] <= c.genes[len(c.genes)-1][1]:
                    movY = 1
                else:
                    movY = -1
                op = np.random.randint(0,2)
                if op == 0:
                    nGen = (g[0]+movX*step,g[1]+movY*step)
                elif op == 1:
                    nGen = (g[0] + movX * step, g[1])
                else:
                    nGen = (g[0], g[1] + movY * step)
                factNext = linea_factible(nGen,c.genes[i+1],lab)
                factAnt = linea_factible(nGen,c.genes[i-1],lab)
                if factAnt and factNext:
                    newGenes.append(nGen)
                else:
                    newGenes.append(g)
            else:
                newGenes.append(g)
        c.cambiarGenes(newGenes)
        nuevaPoblacion.append(c)
    return nuevaPoblacion


def dibuja_poblacion(poblacion, p1, p2, n=-1):
    im = Image.open("lab.png")
    draw = ImageDraw.Draw(im)
    for c in poblacion:
        colors = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))
        for i in range(len(c.genes) - 1):
            coords = (c.genes[i][0], c.genes[i][1], c.genes[i + 1][0], c.genes[i + 1][1])
            draw.line(coords, fill=colors, width=2)
    draw.ellipse(p1, fill=(255, 255, 0))
    draw.ellipse(p2, fill=(255, 0, 0))
    if n>=0:
        title_font = ImageFont.truetype(r'C:\windows\fonts\arial.ttf', 40)
        title_text = 'Generacion: ' + (str)(n)
        draw.text((15,15),title_text,font=title_font,fill=(255,0,0))
        im.save('AlgoritmoGenetico\Gen '+(str)(n)+'.png')
    else:
        im.save('AlgoritmoGenetico\Resultado ' + (str)(n) + '.png')
    im.show()


def dibuja_cromosoma(c,p1,p2):
    im = Image.open("lab.png")
    draw = ImageDraw.Draw(im)
    colors = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))
    for i in range(len(c.genes) - 1):
        coords = (c.genes[i][0], c.genes[i][1], c.genes[i + 1][0], c.genes[i + 1][1])
        draw.line(coords, fill=colors, width=2)
    draw.ellipse(p1, fill=(255, 0, 0))
    draw.ellipse(p2, fill=(255, 0, 0))
    im.show()

    im = Image.open("color.png")
    draw = ImageDraw.Draw(im)
    for i in range(len(c.genes) - 1):
        coords = (c.genes[i][0], c.genes[i][1], c.genes[i + 1][0], c.genes[i + 1][1])
        colors = (0, 0, 0)
        draw.line(coords, fill=colors, width=2)
    draw.ellipse(p1, fill=(255, 0, 0))
    draw.ellipse(p2, fill=(255, 0, 0))
    im.show()

def muestraGeneracion(i,poblacion,bestObj,promObj,worstObj,c1,c2):
    print('Generacion: ', i + 1)
    print('nro\tobjetivo\t\tcantgenes')
    poblacion.sort(key=lambda c: c.objetivo)
    for j,c in enumerate(poblacion):
        if c.genes[0]==c1 and c.genes[len(c.genes)-1]==c2:
            print(' ',j,'\t ',c.objetivo,'\t',len(c.genes),'\t ',c.genes[0],'\t',c.genes[len(c.genes)-1])
        else:
            print("\033[1;31m", j, '\t ', c.objetivo, '\t', len(c.genes), '\t ', c.genes[0], '\t',
                  c.genes[len(c.genes) - 1], "\033[0m")
            print(c1, c.genes[0], '\t ', c2, c.genes[len(c.genes) - 1], '\t')
    print('Generacion: ', i + 1,'Mejor F.Objetivo: ', bestObj, '\t\t Promeido F.Objetivo: ', promObj, '\t\t Peor F.Objetivo: ', worstObj)

lab = np.load("maze.npy")
dimensions = np.shape(lab)[1]
c1 = generar_ciudad(lab, dimensions)  # Primera Ciudad
c2 = generar_ciudad(lab, dimensions)  # Segunda Ciudad
# c1 = (100,30)
# c2 = (80,200)

# Muestra ubicacion de las ciudades
point1 = ((c1[0] - 5, c1[1] - 5), (c1[0] + 5, c1[1] + 5))
point2 = ((c2[0] - 5, c2[1] - 5), (c2[0] + 5, c2[1] + 5))
im = Image.open("lab.png")
draw = ImageDraw.Draw(im)
draw.ellipse(point1, fill=(255, 0, 0))
draw.ellipse(point2, fill=(255, 0, 0))
im.show()

# Inicializa listas y poblacion
generaciones = []
poblacion = generarPoblacion(lab, dimensions, nroPoblacion, c1, c2)
funcionesObjetivoPromedio = []
mejoresFuncionesObjetivo = []
mejoresCromosomas = []
peoresFuncionesObjetivos = []

for i in range(ciclos):
    sumObj = 0
    bestCrom = poblacion[0]
    bestObj = poblacion[0].objetivo
    worstObj = poblacion[0].objetivo
    for c in poblacion:
        if c.getFuncObjetivo() < bestObj:
            bestCrom = c
            bestObj = c.objetivo
        if c.objetivo > worstObj:
            worstObj = c.objetivo
        sumObj += c.objetivo
    promObj = sumObj / len(poblacion)
    funcionesObjetivoPromedio.append(promObj)
    mejoresFuncionesObjetivo.append(bestObj)
    mejoresCromosomas.append(bestCrom)
    peoresFuncionesObjetivos.append(worstObj)
    muestraGeneracion(i,poblacion,bestObj,promObj,worstObj,c1,c2)
    if i % graf_rate ==0:
        dibuja_poblacion(poblacion, point1, point2,i)
    generaciones.append(poblacion)
    poblacion = seleccion(poblacion,rango)
    poblacion = crossover(lab,dimensions,poblacion,probabilidad_crossover,rango)
    poblacion = mutacionLargo(poblacion,probabilidad_mutacion_largo,i,ciclos)
    poblacion = mutacionGen(poblacion, probabilidad_mutacion_gen,step,lab)

dibuja_cromosoma(bestCrom, point1, point2)
dibuja_poblacion(poblacion, point1, point2,ciclos)
