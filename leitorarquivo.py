class LeitorArquivo:
    def __init__(self, nomeArquivo):
       self.arq = open(nomeArquivo, "r")
       self.__leValores()
    
    def __leValores(self):
        self.valores = []

        for line in self.arq.readlines():
            lista = [float(x) for x in line.split()]
            self.valores.append(lista)
 
    def getValores(self):
       return self.valores