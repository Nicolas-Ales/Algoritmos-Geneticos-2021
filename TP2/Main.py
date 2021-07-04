from Elementos import *
from Mochila import * #NO FUNCIONA IMPORT PORQUE

#Convierte decimal a binario
def convertirBinario(num):
    list1 = []
    list1[:0] = bin(num).replace("0b", "")
    return list1

#Inicializo la lista de mochilas posibles
mochilas = []

#Lleno la lista mochilas con todas las mochilas posibles
'''for i in range(0, 1024):
    binario = convertirBinario(i)
    mochilas.append(Mochila(binario, elementos))
    print(mochilas[i].contenido)'''

mochilas.append(Mochila(convertirBinario(12), elementos))

print(mochilas[0].contenido)