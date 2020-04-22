from PIL import Image
import numpy as np
import math
from collections import deque
from time import sleep


def show_matriz(m):  # printa Matriz
    print("\n\n\n")
    for i in m:
        for j in i:
            print(j, end=' ')
        print('')
    print("\n\n\n")


# Abre a imagem 1
img1 = Image.open("kill.jpg")
img1 = img1.convert('L')  # ESSE ARGUMENTO TRANFORMA DE RGB PARA PRETO E BRANCO, LOGO CADA PIXEL VARIA DE 0 À 255
img1.show()
show_matriz(np.asanyarray(img1))
sleep(3)
# Abre imagem 2
img2 = Image.open('kill.jpg')
img2 = img2.convert('L')
show_matriz(np.asanyarray(img2))

imgFinal = Image.new('L', (int(img1.width), int(img1.height)), color='white')  # imagemFinal recebe uma imagem em branco

#
nova = imgFinal  # nova recebe imagem em branco
n1 = img1.load()  # carrega a primeira imagem
n2 = img2.load()  # carrega a segunda imagem
n3 = nova.load()  #

# percorre as matrizes fazendo a operação de SOMA
for i in range(img1.width):
    for j in range(img1.height):
        if int(n1[i, j] + n2[i, j] / 2) > 255:
            n3[i, j] = 255
        else:
            n3[i, j] = int(n1[i, j] + n2[i, j] / 2)

#Mostra Imagem
nova.show()
print(np.asanyarray(imgFinal))

#######################SUBTRAÇÃO#########

nova2 = imgFinal
n5 = img1.load()
n6 = img2.load()
n7 = nova.load()

for i in range(img1.width):
    for j in range(img1.height):
        if int(n5[i, j] - n6[i, j] / 2) < 0:
            n7[i, j] = 0
        else:
            n7[i, j] = int(n5[i, j] - n6[i, j] / 2)

nova.show()
print(np.asanyarray(imgFinal))



##############Rotação

img = Image.open("kill.jpg")
img = img.convert('L')
img.show()
matriz = np.asanyarray(img)

larg = np.size(matriz, 0)
alt = np.size(matriz, 1)

matrizFinal = []
aux = []
print(matrizFinal)
# show_matriz(matrizFinal)

# Rotaciona de 90 em 90 (USAR ESSE)
aux = deque()  # para ser possível inserir no início

for k in range(1):  # 1 == 90º, 2 == 180º ...
    for i in range(larg - 1):  # inverti linha e colunas
        for j in range(alt - 1):
            try:
                aux.appendleft(matriz[j][i])
            except:
                continue
        matrizFinal.append(aux.copy())
        aux.clear()
    matriz = matrizFinal.copy()
    matrizFinal.clear()

# Funcionando Com BUG
# graus = float(input("Informe quantos graus deseja rotacionar a imagem: "))
#
# for h in range(alt):
#     for w in range(larg):
#         try:
#             x = int((w * math.cos(graus)) - (h * math.sin(graus)))
#             y = int((w * math.sin(graus) + h * math.cos(graus)))
#             matrizFinal[x, y] = matriz[w, h]
#         except:
#             continue

img = Image.fromarray(np.asanyarray(matriz))
img.show()
show_matriz(matrizFinal)