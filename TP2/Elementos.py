from collections import namedtuple

#Creo namedtuple con los atributos de los elementos
Elemento = namedtuple('elemento', ['id', 'valor', 'espacioOcupado', 've'])

#Inicializo los elementos en la namedtuple
elementos1 = [
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
for i in range(0, len(elementos1)):
    elementos1[i] = elementos1[i]._replace(ve = '%.3f'%(elementos1[i].valor / elementos1[i].espacioOcupado))


elementos2 = [
    Elemento(1, 72, 1800, 0),
    Elemento(2, 36, 600, 0),
    Elemento(3, 60, 1200, 0)
]

#Calculo el $valor/peso con 3 decimales de exactitud
for i in range(0, len(elementos2)):
    elementos2[i] = elementos2[i]._replace(ve = '%.3f'%(elementos2[i].valor / elementos2[i].espacioOcupado))