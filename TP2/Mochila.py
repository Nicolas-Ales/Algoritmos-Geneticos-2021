
class Mochila(object):
    volumenMax = 4200

    #el binario = 0 es por si no mando parametros, que el default sea cero. me pidio si o si lo mismo para elementos
    def __init__(self, binario = 0, elementos = 0):
        self.elementos = elementos
        if (binario != 0):
            self.binario = binario
            self.contenido = self.getContenido()
            self.volumen = self.setVolumen()
            self.valor = self.setValor()
        else:
            self.contenido = self.armarMochila()
            self.volumen = self.setVolumen()
            self.valor = self.setValor()
    #deberia agregar en contenidos todos los elementos presentes en mochila
    def getContenido(self):
        contenido = []
        e = self.elementos.copy()
        for i in range(0, len(self.binario)):
            if (self.binario[i] == '1'):
                contenido.append(e[i])
        return contenido

    #Suma el volumen de el contenido de la Mochila
    def setVolumen(self):
        vol = 0
        for i in range(0, len(self.contenido)):
            vol += self.contenido[i].volumen
        return vol
    
    #Suma el valor de el contenido de la Mochila
    def setValor(self):
        val = 0
        for i in range(0, len(self.contenido)):
            val += self.contenido[i].valor
        return val

    def armarMochila(self):
        self.elementos.sort(key=lambda x: x.vv, reverse=True)
        contenido = []
        vol = 0
        i = 0
        while (vol < 4200):  #ES ESTA LA MANERA CORRECTA DE REFERIRME A ESTA VARIABLE??? me referia a volumenMax
            contenido.append(self.elementos[i])
            vol += contenido[i].volumen
            i += 1
        contenido.pop() #hay una mejor manera?
        return contenido
        #este while no esta parando cuando lo necesito