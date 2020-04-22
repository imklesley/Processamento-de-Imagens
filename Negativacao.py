from PIL import Image
import numpy as np


imagem = Image.open('teste0.jpg')
imagem = imagem.convert('L')
imagem.show()
matriz = np.asanyarray(imagem)
matrizFinal = []
aux = []

for i in matriz:
    for j in i:
       aux.append(255-j)
    matrizFinal.append(aux.copy())
    aux.clear()

matrizFinal = np.asanyarray(matrizFinal)
imagem = Image.fromarray(matrizFinal)
imagem.show()

