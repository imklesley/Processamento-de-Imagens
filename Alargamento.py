from PIL import Image
import numpy as np


def buscaMenorMaior(m): # vai buscar menor e maior valor da imagem
    aux = {}
    for i in m:
        for j in i:
            if j not in aux:
                aux[j] = 1
            else:
                aux[j] += 1
    aux = sorted(aux) # retorna as chaves em ordem
    return aux[0], aux[-1] # retorna o menor valor e maior valor da imagem

imagem = Image.open('teste3.jpg')
imagem = imagem.convert('L')
imagem.show()
matriz = np.asanyarray(imagem)

c, d = buscaMenorMaior(matriz) # busca o menor(c) e maior valor(d)
print("")
print(c, d)

matrizFinal = []
aux = []
for i in matriz:#vai passar de nó em nó
    for j in i:
        aux.append((j-c)*(255/(d-c))) #aplica-se a formula de alargamento na linha aux
    matrizFinal.append(aux.copy())#adiciona - se a linha a matriz
    aux.clear()# limpa-se a linha auxiliar para refazer o processo


#Gera-se a imagem
matrizFinal = np.asanyarray(matrizFinal)
imagem = Image.fromarray(matrizFinal)
imagem.show()


