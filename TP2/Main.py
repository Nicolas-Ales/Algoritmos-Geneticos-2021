from TP2.Elementos import *
from TP2.Mochila import *

exhaustivo = False  # True para busqueda exhaustiva | False para Algoritmo Greedy
volumen = False  # True para el primer set de items | False para el segundo set de items


# Convierte decimal a binario
def convertirBinario(num):
    list1 = []
    list1[:0] = bin(num).replace("0b", "")
    return list1


def llenarMochilas(elementos):  # Funcion que utilizamos para la busqueda exhaustiva
    # Creo una lista de binarios para crear todas las posibles soluciones
    # un 0 en la posicion en la lista del item es que el item no esta en la mochila y un 1 es que esta
    for i in range(0, 2 ** (len(elementos))):
        binario = convertirBinario(i)
        # Ya que nuestra funcion devuelve binarios sin importar su largo el siguiente codigo completa los binarios mas
        # cortos con 0s
        if len(binario) < (len(elementos)):
            binarioCompleto = []
            for j in range(len(elementos) - len(binario)):
                binarioCompleto.append("0")
            binarioCompleto.extend(binario)
        else:
            binarioCompleto = binario
        # Crea una mochila con los elementos segun el binario y calculo su valor y peso/volumen
        mochila = Mochila(binarioCompleto, elementos)
        if (volumen):  # division dependiendo el ejercicio
            # En caso de no superar el limite de volumen se agrega a mochilas posibles
            if (mochila.espacioOcupado <= Mochila.volumenMax):
                mochilasPosibles.append(mochila)
                # print('Valor: ', mochila.valor, '\tVolumen: ', mochila.espacioOcupado)
        else:
            # En caso de no superar el limite de peso se agrega a mochilas posibles
            if (mochila.espacioOcupado < Mochila.pesoMax):
                mochilasPosibles.append(mochila)
                # print('Valor: ', mochilasPosibles[i].valor, '\tPeso: ', mochilasPosibles[i].espacioOcupado)
    return mochilasPosibles


# Inicializo la lista de mochilas posibles
mochilas = []
mochilasPosibles = []

if (volumen):
    if (exhaustivo):
        # Lleno la lista mochilas con todas las mochilas posibles y luego las ordeno por valor de forma decreciente
        m = max(llenarMochilas(elementos1), key=lambda mochila: mochila.valor)
        print('Busqueda Exhaustiva\nMochila Optima')

    else:
        m = Mochila(elementos=elementos1)
        print('Algortimo Greedy\nMochila Seleccionada:')
    # Muestra caracteristicas de la mochila y su contenido
    print('Valor: ', m.valor, '\tVolumen: ', m.espacioOcupado)
    print('Contenido de Mochila: ')
    for i in m.contenido:
        print('  Id:', i[0], '\t valor:', i[1], '\t volumen:', i[2])
else:
    if (exhaustivo):
        # Lleno la lista mochilas con todas las mochilas posibles y luego las ordeno por valor de forma decreciente
        m = max(llenarMochilas(elementos2), key=lambda mochila: mochila.valor)
        print('Busqueda Exhaustiva\nMochila Optima')
    else:
        m = Mochila(elementos=elementos2, volumen=False)
        print('Algortimo Greedy\nMochila Seleccionada:')

    # Muestra caracteristicas de la mochila y su contenido
    print('Valor: ', m.valor, '\tPeso: ', m.espacioOcupado)
    print('Contenido de Mochila: ')
    for i in m.contenido:
        print('  Id:', i[0], '\t valor:', i[1], '\t peso:', i[2])
