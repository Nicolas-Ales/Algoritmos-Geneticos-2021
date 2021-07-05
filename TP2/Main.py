from Elementos import *
from Mochila import * #NO FUNCIONA IMPORT PORQUE no toquen este comentario

#Exhaustivo?
exhaustivo = True

#Convierte decimal a binario
def convertirBinario(num):
    list1 = []
    list1[:0] = bin(num).replace("0b", "")
    return list1

#Inicializo la lista de mochilas posibles
mochilas = []
mochilasPosibles = []

if (exhaustivo):
    #Lleno la lista mochilas con todas las mochilas posibles y filtro las que tienen volúmen menor al volúmen máximo
    for i in range(0, 1024):
        binario = convertirBinario(i)
        mochilas.append(Mochila(binario, elementos))
        if (mochilas[i].volumen < Mochila.volumenMax):
            mochilasPosibles.append(mochilas[i])
            print('Valor: ', mochilasPosibles[i].valor, '\tVolumen: ', mochilasPosibles[i].volumen)
            #hay un error que se va de rango. REVISAR!! 
    print('')       
    #Selecciono la mochila que tiene el mayor valor
    m = max(mochilasPosibles, key = lambda mochila: mochila.valor)

else:
    m = Mochila(elementos = elementos)

print('Solucion: ', m.valor, '\tVolumen: ', m.volumen)
print('Contenido de Mochila: ', m.contenido)