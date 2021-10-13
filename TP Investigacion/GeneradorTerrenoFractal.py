import random as rd
import numpy as np
from PIL import Image
import pandas as pd

def hacerImagen (ar,dimensions):
    img = Image.new('RGB', (dimensions, dimensions), "white")  # Create a new white image
    pixels = img.load()  # Create the pixel map
    for i in range(img.size[0]):  # For every pixel:
        for j in range(img.size[1]):
            t = int(255 * ar[i, j])
            pixels[i, j] = (t, t, t)  # Set the colour accordingly
    # img.show()
    return img

def recolor(ar, dimensions):
    img = Image.new('RGB', (dimensions, dimensions), "white")  # Create a new white image
    pixels = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            h = int(20+ar[x,y]*130)
            if h in range(140,150):
                pixels[x,y] = (255,0,0)
            elif h in range(130, 140):
                pixels[x, y] = (255, 55, 0)
            elif h in range(120, 130):
                pixels[x, y] = (255, 115, 0)
            elif h in range(110, 120):
                pixels[x, y] = (255, 170, 0)
            elif h in range(100, 110):
                pixels[x, y] = (255, 226, 0)
            elif h in range(90, 100):
                pixels[x, y] = (228, 245, 0)
            elif h in range(80, 90):
                pixels[x, y] = (176, 224, 0)
            elif h in range(70, 80):
                pixels[x, y] = (130, 206, 0)
            elif h in range(60, 70):
                pixels[x, y] = (90, 186, 0)
            elif h in range(50, 60):
                pixels[x, y] = (55, 167, 0)
            elif h in range(40, 50):            #agua
                pixels[x, y] = (0, 170, 255)
            elif h in range(30, 40):
                pixels[x, y] = (0, 128, 255)
            elif h in range(20, 30):
                pixels[x, y] = (0, 64, 255)
            elif h in range(10, 20):
                pixels[x, y] = (0, 0, 255)
            elif h in range(0,10):
                pixels[x, y] = (0, 0, 207)
            elif h in range(-40,0):
                pixels[x, y] = (0, 0, 150)
            elif h < -40:
                pixels[x, y] = (0, 0, 100)
            elif h < -60:
                pixels[x, y] = (0, 0, 50)
                print('negativo?: ',h)
            elif h >=150:
                pixels[x, y] = (255, 10, 10 )

    img.show()
    return img

def diamondSquare(ar, stepsize, scale, dimensions):
    half = int(stepsize / 2)
    # Diamante
    for y in range(half, dimensions + half, stepsize):
        for x in range(half, dimensions + half, stepsize):
            centerTemp = ((ar[x - half, y - half] + ar[x + half, y - half] + ar[x - half, y + half] + ar[
                x + half, y + half]) / 4
                        + rd.uniform(-1, 1) * scale)
            if centerTemp > 1:
                ar[x, y] = 1
            elif centerTemp < 0:
                ar[x, y] = 0
            else:
                ar[x,y] = centerTemp
    # Cuadrado
    for y in range(0, dimensions, stepsize):
        for x in range(0, dimensions, stepsize):
            topTemp = ((ar[x + half + half, y] + ar[x + half - half, y] + ar[x + half, y + half]
                                + ar[x + half, y - half]) / 4 + rd.uniform(-1, 1) * scale)
            if topTemp > 1:
                ar[x + half, y] = 1
            elif topTemp < 0:
                ar[x + half, y] = 0
            else:
                ar[x + half, y] = topTemp

            rightTemp = ((ar[x + half , y + half] + ar[x - half , y + half] + + ar[x, y + half + half] +
                                 ar[x, y + half - half]) / 4 + rd.uniform(-1, 1) * scale)
            if rightTemp > 1:
                ar[x, y + half] = 1
            elif rightTemp < 0:
                ar[x, y + half] = 0
            else:
                ar[x, y + half] = rightTemp
    return ar

def labyrinth (har, dimensions, pixelEq, pMax):
    maze = np.zeros((dimensions,dimensions))
    print('laberinto en 0s')
    print(maze)
    print('laberinto:\n\n')
    for x in range(dimensions):
        for y in range(dimensions):
            if x==0 or y==0 or x==dimensions or y==dimensions:
                maze[x,y] = 0
            else:
                condicion = (pMax < abs((har[x, y]-har[x + 1 , y ]) / pixelEq) * 100) or\
                            (pMax < abs((har[x, y]-har[x - 1 , y ]) / pixelEq) * 100) or\
                            (pMax < abs((har[x, y] - har[x, y + 1])/ pixelEq) * 100) or\
                            (pMax < abs((har[x, y] - har[x, y - 1]) / pixelEq) * 100) or\
                            har[x,y] <= 50
                if condicion:
                    maze[x,y] = 0
                    print(abs(har[x, y]-har[x + 1 , y ]),' ',abs(har[x, y]-har[x - 1 , y ]),' ',abs(har[x, y]-har[x , y + 1]),' ',' ',abs(har[x, y]-har[x , y - 1]))
                else:
                    maze[x,y] = 1
    print(pMax)
    print(maze)
    return maze

pixelEq = 100   #Distancia a la que equivale un pixel en nuestra imagen (en metros)
pendiente_maxima = 5   #porcentaje
num_cells = 5
cell_size = 256 #Esto tiene que ser potencia de 2, porque sino al momemento de hacer el metodo de dezplazamiento de
                 # cuadrados nos queda mal la escala y quedan los cuadrados bien definidos en las imagenes
dimensions = num_cells * (cell_size)

ar = np.eye(int(dimensions+1))
for i in range(0, dimensions):
    ar[i, i] = 0
for x in range(0, dimensions, cell_size):
    for y in range(0, dimensions, cell_size):
        ar[x, y] = rd.uniform(0, 1)

scale = 1.0
imagenes = []
p = 1
while cell_size > 1:
    print(scale,' ', cell_size)
    paso = hacerImagen(ar, dimensions)
    imagenes.append(paso)
    nroPaso = 'paso '+str(p)+'.png'
    paso.save('paso '+str(p)+'.png')
    p+=1
    ar = diamondSquare(ar, cell_size, scale, dimensions)
    scale *= 0.5
    cell_size = int(cell_size / 2)

# print(ar)
color = recolor(ar,dimensions)
color.save("color.png")
final = hacerImagen (ar,dimensions)
final.save('terreno.png')
final.show()
imagenes.append(final)
gif = Image.new('RGB', (dimensions, dimensions), "black")
gif.save('animacion.gif', save_all=True, append_images=imagenes,optimize=False, duration=500, loop=1)
# gif.show()

np.save("array.npy", ar)
nar = np.load('array.npy')
harray = np.array(ar)
for x in range(dimensions):
    for y in range(dimensions):
        harray[x,y] = ar[x,y]*120 + 30
# print(harray)
# print('\n\n\n Todavia no \n\n')
# df = pd.DataFrame(harray)
# df.to_excel("ar.xlsx", index=False)
# print('\n\n\n Ahora si \n\n')

lab = labyrinth(harray,dimensions,pixelEq,pendiente_maxima)
print(lab)
np.save("maze.npy", lab)
laberinto = hacerImagen(lab,dimensions)
laberinto.save('lab.png')
laberinto.show()

