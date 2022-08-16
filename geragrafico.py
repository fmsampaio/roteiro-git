from leitorarquivo import LeitorArquivo
import numpy as np
import matplotlib.pyplot as plt

def main():
   leitor = LeitorArquivo('data.txt')
   valores = leitor.getValores()
   print(valores)

   plt.plot(valores)
   plt.ylabel('Valores de entrada')
   plt.xlabel('Amostragem')
   
   plt.show() 
   
     
 
main()