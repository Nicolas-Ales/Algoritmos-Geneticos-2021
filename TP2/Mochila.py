
class Mochila(object):
    volumenMax = 4200

    def __init__(self, binario, elementos):
        self.binario = binario
        self.elementos = elementos
        self.contenido = self.getElementos()
        self.volumenActual = 0
        self.valor = 0

    #deberia agregar en contenidos todos los elementos presentes en mochila
    def getElementos(self):
        contenido = []
        e = self.elementos.copy()
        for i in range(0, len(self.binario)):
            if (self.binario[i] == '1'):
                self.contenido.append(e[i])
        return contenido
