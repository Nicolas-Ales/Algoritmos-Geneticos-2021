
class Mochila(object):
    volumenMax = 4200

    def __init__(self, binario, elementos):
        self.binario = binario
        self.elementos = elementos
        self.contenido = self.getElementos()
        self.volumenActual = self.setVolumen()
        self.valor = self.setValor()

    #deberia agregar en contenidos todos los elementos presentes en mochila
    def getElementos(self):
        contenido = []
        e = self.elementos.copy()
        for i in range(0, len(self.binario)):
            if (self.binario[i] == '1'):
                contenido.append(e[i])
        return contenido

    def setVolumen(self):
        vol = 0
        for i in range(0, len(self.contenido)):
            vol = vol + self.contenido[i].volumen
        return vol
    
    def setValor(self):
        val = 0
        for i in range(0, len(self.contenido)):
            val = val + self.contenido[i].valor
        return val