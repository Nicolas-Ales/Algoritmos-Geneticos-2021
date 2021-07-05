
class Mochila(object):
    volumenMax = 4200
    pesoMax = 3000

    #el binario = 0 es por si no mando parametros, que el default sea cero. me pidio si o si lo mismo para elementos
    def __init__(self, binario = 0, elementos = 0, volumen = True):
        self.elementos = elementos
        self.volumen = volumen
        if (binario != 0):
            self.binario = binario
            self.contenido = self.getContenido()
            self.espacioOcupado = self.setEspacioOcupado()
            self.valor = self.setValor()
        else:
            self.contenido = self.armarMochila()
            self.espacioOcupado = self.setEspacioOcupado()
            self.valor = self.setValor()
    
    #deberia agregar en contenidos todos los elementos presentes en mochila
    def getContenido(self):
        contenido = []
        e = self.elementos.copy()
        for i in range(0, len(self.binario)):
            if (self.binario[i] == '1'):
                contenido.append(e[i])
        return contenido

    #Suma el espacio ocupado del contenido de la Mochila
    def setEspacioOcupado(self):
        esp = 0
        for i in range(0, len(self.contenido)):
            esp += self.contenido[i].espacioOcupado
        return esp
    
    #Suma el valor de el contenido de la Mochila
    def setValor(self):
        val = 0
        for i in range(0, len(self.contenido)):
            val += self.contenido[i].valor
        return val

    #
    def armarMochila(self):
        self.elementos.sort(key=lambda x: x.ve, reverse=True)
        contenido = []
        esp = 0
        i = 0
        if (self.volumen):
            while (esp <= 4200):  #como hago referencia a volumenMax?
                contenido.append(self.elementos[i])
                esp += contenido[i].espacioOcupado
                i += 1
        else: 
            while (esp <= 3000):  #como hago referencia a volumenMax?
                contenido.append(self.elementos[i])
                esp += contenido[i].espacioOcupado
                i += 1
        contenido.pop()
        return contenido
        #este while no esta parando cuando lo necesito