from Elementos import *
from Mochila import * 

#Exhaustivo?
exhaustivo = True
volumen = False

#Convierte decimal a binario
def convertirBinario(num):
    list1 = []
    list1[:0] = bin(num).replace("0b", "")
    return list1

def llenarMochilas(elementos):
    for i in range(0, 2**(len(elementos))):
        binario = convertirBinario(i)
        mochilas.append(Mochila(binario, elementos))
        if (volumen):
            if (mochilas[i].espacioOcupado < Mochila.volumenMax):
                mochilasPosibles.append(mochilas[i])
                #print('Valor: ', mochilasPosibles[i].valor, '\tVolumen: ', mochilasPosibles[i].espacioOcupado)
        else:
            if (mochilas[i].espacioOcupado < Mochila.pesoMax):
                mochilasPosibles.append(mochilas[i])
                #print('Valor: ', mochilasPosibles[i].valor, '\tPeso: ', mochilasPosibles[i].espacioOcupado)
    return mochilasPosibles


#Inicializo la lista de mochilas posibles
mochilas = []
mochilasPosibles = []


if (volumen):
    if (exhaustivo):
        #Lleno la lista mochilas con todas las mochilas posibles y filtro las que tienen volúmen menor al volúmen máximo
        m = max(llenarMochilas(elementos1), key = lambda mochila: mochila.valor)

    else:
        m = Mochila(elementos = elementos1)

    print('Valor: ', m.valor, '\tVolumen: ', m.espacioOcupado)
    print('Contenido de Mochila: ', m.contenido)
else:
    if (exhaustivo):
        m = max(llenarMochilas(elementos2), key = lambda mochila: mochila.valor)
    else:
        m = Mochila(elementos = elementos2, volumen = False)
    print('Valor: ', m.valor, '\tPeso: ', m.espacioOcupado)
    print('Contenido de Mochila: ', m.contenido)