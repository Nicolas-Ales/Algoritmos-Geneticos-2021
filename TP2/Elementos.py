from collections import namedtuple

Elemento = namedtuple('elemento', ['id', 'valor', 'volumen', 'vv'])

#Inicializo los elementos en la namedtuple
elementos = [
    Elemento(1, 20, 150, 0),
    Elemento(2, 40, 325, 0),
    Elemento(3, 50, 600, 0),
    Elemento(4, 36, 805, 0),
    Elemento(5, 25, 430, 0),
    Elemento(6, 64, 1200, 0),
    Elemento(7, 54, 770, 0),
    Elemento(8, 18, 60, 0),
    Elemento(9, 46, 930, 0),
    Elemento(10, 28, 353, 0)
]

#Calculo el $valor/volumen con 3 decimales de exactitud
for i in range(0, len(elementos)):
    elementos[i] = elementos[i]._replace(vv = '%.3f'%(elementos[i].valor / elementos[i].volumen))