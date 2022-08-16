from leitorarquivo import LeitorArquivo
import numpy as np
import matplotlib.pyplot as plt

def main():
   leitor = LeitorArquivo('data.txt')
   valores = leitor.getValores()
   medias = leitor.getMedias()
   
   print(valores)
   print(medias)

   plt.subplot(1, 2, 1)

   i = 1
   for serie in valores:
      plt.plot(serie, label='Série ' + str(i))   
      i += 1
   plt.legend(loc='upper left')

   plt.title('Gráfico de linhas')
   plt.ylabel('Valores de entrada')
   plt.xlabel('Amostragem')

   plt.subplot(1, 2, 2)
   
   xvalues = np.arange(1, len(medias) + 1)
   plt.bar(xvalues, medias)
   plt.xticks(xvalues, ['Série ' + str(x) for x in xvalues])
   plt.title('Médias das séries')

   plt.show() 
   
     
 
main()