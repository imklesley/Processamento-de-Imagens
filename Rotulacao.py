from PIL import Image
import numpy as np
from random import randint

def show_matriz(m):  # printa matriz ---> somente para análise dos resultados
    print('\n\n')
    for i in m:
        for j in i:
            print(j, end=' ')
        print('')
    print('\n\n')


imagem = Image.open("teste01.jpg") # MOSTRA O TESTE100 PRO HIAGO
imagem = imagem.convert('L')
imagem.show()
matriz = np.asanyarray(imagem)

altura = np.size(matriz, 0)
largura = np.size(matriz, 1)

######## Binarização
mB = []  # matriz binarizada
aux = []
for i in range(altura):
    for j in range(largura):
        if matriz[i][j] <= 127:
            aux.append(1)
        else:
            aux.append(0)
    mB.append(aux.copy())
    aux.clear()
######### Binarização


show_matriz(mB)
labels = {} #posição (i,j) vai ter uma determinada lable
nomeLabel = 1 #Inicialização da nomeclatura das lables
flag = 0 #vai auxiliar para quando devemos mudar o nomeLable
equivalentes = {} # vai guardar os equivalentes

#Procura-se e insere-se as lables
for i in range(altura):
    for j in range(largura):
        if mB[i][j] == 0:  # Se p = 0, move-se para o próximo pixel;
            try:
                if mB[i][j-1] == 1:
                    nomeLabel += 1
            except:
                if mB[i-1][-1] == 1:
                    nomeLabel += 1
            # labels[(i, j)] = -1
            continue
        else: #se for 1
            if mB[i-1][j] == 0 and mB[i][j-1] == 0: # se R e S são zeros logo o valor encontrado vai receber uma lable isoladamente(uma nova)
                labels[(i, j)] = nomeLabel

            elif mB[i-1][j] == 1 and mB[i][j-1] == 1: # Se R e S forem 1
                try:
                    if labels[(i-1, j)] != labels[(i, j-1)]:# mas o lable for diferente, escolho um deles e faços equivalentes
                        equivalentes[labels[(i-1, j)]] = labels[(i, j-1)]#no dicionario guarda-se o equivalente da vez, mais tarde será tratado as equivalências
                    labels[(i,j)] = labels[(i-1, j)]
                except:
                    pass
            elif mB[i-1][j] == 1 or mB[i][j-1] == 1:  # R ou S é 1? então coloca-se a lable do que é um na lable da posicao (i,j) ----#Mudar a ordem por causa do ou e and precedencia
                try:
                    if mB[i-1][j] == 1:
                        labels[(i, j)] = labels[(i-1, j)]
                    elif mB[i][j-1] == 1:
                        labels[(i, j)] = labels[(i, j-1)]
                except:
                    pass



print(f"Lables antes tratamento de equivalencia{labels}")


#trata equivalencias do lables, para que na hr da mudança das cores não haja conflito
for e in equivalentes.keys():
    for k, lable in labels.items(): # k == (i,j) lable == 0 ou 1 ...
        if lable == e:
            labels[k] = equivalentes[e] # faz as lables da posicao (i,j) virarem a lable do valor da sua equivalente

print(f"Lables após tratamento de equivalencia{labels}")



matrizFinal=[]
aux = []

#Ajeita-se as equivalências, porém só da matriz   tem que usar a função acima pra fazer as alterações na relação das lables e cores
for i in range(altura):
    for j in range(largura):
        for k in sorted(equivalentes):
            if mB[i][j] == k:
                aux.append(equivalentes[k])
                break #Para não repetir a inserção
            else:
                aux.append(mB[i][j])
                break #Para não repetir a inserção
    matrizFinal.append(aux.copy())
    aux.clear()

print('\n\nApos tratar equivalencias')
show_matriz(matrizFinal)

listaLables = list(set(labels.values()))
listaLables.sort()
print(f"Lista de Lables {listaLables}")


print('Matriz após todas as alterações')
for k in listaLables:
    corAlea = randint(50, 250) # escolhe uma cor para colocar em uma das lables
    for i in range(altura):
        for j in range(largura):
                try:
                    if labels[(i, j)] == k:
                        matrizFinal[i][j] = corAlea
                except:
                    continue

show_matriz(matrizFinal)
matrizFinal = np.asanyarray(matrizFinal)
imagem = Image.fromarray(matrizFinal)
imagem.show()