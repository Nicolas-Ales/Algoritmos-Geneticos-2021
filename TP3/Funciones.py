from prettytable import PrettyTable
import cv2


def Exhaustivo():
    pass


def Heuristico():
    pass


def Genetico():
    pass


def MuestraDatos(seleccion, capitales):
    print('Camino Seleccionado:')
    distancia = 0
    tabla = PrettyTable(['Capital', 'Distancia Recorrida'])
    for i in range(len(seleccion)):
        tabla.add_row([capitales[seleccion[i]].Nombre, str(distancia)])
        if i < 24:
            distancia += capitales[seleccion[i]].Distancias[seleccion[i + 1]]
    print(tabla)
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
        (188, 445),  # 23 Vietma
    ] #Lista con las coordenadas de cada ciudad en el mapa
    imagen = cv2.resize(cv2.imread('mapa-provincias-argentina.png'), (454, 791)) #Carga la imagen del mapa y la redimenciona
    for i in range(len(seleccion)): #Recorre la lista con el orden seleccionado de las ciudades
        if i <24: #Si no es la ultima ciudad dibuja la linea a la siguiente ciudad
            cv2.line(imagen, coordenadas_capitales[capitales[seleccion[i]].id],
                     coordenadas_capitales[capitales[seleccion[i + 1]].id], (255-i*10, i*10, i*10), 2)
        else: #Si es la ultima ciudad dibuja una linea hasta la primera
            cv2.line(imagen, coordenadas_capitales[capitales[seleccion[i]].id],
                     coordenadas_capitales[capitales[seleccion[0]].id], (255-i*10, i*10, i*10), 2)
    for c in coordenadas_capitales: #Recorre la lista de coordenadas de las capitales
        cv2.circle(imagen, c, 4, (0, 0, 255), -1) #Dibuja un punto en cada capital
    cv2.imshow('imagen', imagen) #Muestra la imagen con los dibujos
    cv2.waitKey(0) #Sin esta linea la ventana se cierra automaticamente
