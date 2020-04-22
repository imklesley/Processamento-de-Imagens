from PIL import Image
import numpy as np


def show_matriz(m): # printa matriz ---> somente para análise dos resultados
    print('\n\n')
    for i in m:
        for j in i:
            print(j,end=' ')
        print('')
    print('\n\n')




imagem = Image.open("test0.jpg")
imagem = imagem.convert('L')
imagem.show()
matriz = np.asanyarray(imagem)

altura = np.size(matriz, 0)
largura = np.size(matriz, 1)

#Binarização
mB = [] #matriz binarizada
aux = []
for i in range(altura):
    for j in range(largura):
        if matriz[i][j] <= 127:
            aux.append(1)
        else:
            aux.append(0)
    mB.append(aux.copy())
    aux.clear()
#Binarização

show_matriz(mB)

labels = {}

for i in range(altura):
    for j in range(largura):
        if mB[i][j] == 0:
            continue
        else:
            if mB[i-i][j] == 0 and mB[i][j-1] == 0:
                labels[(i, j)] = 1
            elif mB[i-i][j] == 1 or mB[i][j-1] == 1:
                labels[(i, j)] = labels[(i-1, j)]

