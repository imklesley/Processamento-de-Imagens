from PIL import Image
import numpy as np


def show_matriz(m): # printa matriz ---> somente para análise dos resultados
    print('\n\n')
    for i in m:
        for j in i:
            print(j,end=' ')
        print('')
    print('\n\n')



def showHistograma(m):
    aux = {}
    # conta a quantidade de cada nível
    for i in m:
        for j in i:
            if j not in aux:
                aux[j] = 1
            else:
                aux[j] += 1
    print('\n\nH i s t o g r a m a\n')
    for k in sorted(aux):
        print('{0:5d} {1}'.format(k, '+' * aux[k]))


def equali_histograma(m, qtdPixels):
    aux = {}
    #conta a quantidade de cada nível
    for i in m:
        for j in i:
           if j not in aux:
               aux[j] = 1
           else:
               aux[j] +=1
    tabela= {} # vai guardar o nivel e sua Pr
    frequencia = 0
    EQ = 0 # vai ser a soma de uma sequência de multiplicações, logo para não afetar o resultado inicializa com zero
    L = sorted(aux) ###só pra montar a formula, ordeno todos os níveis pra saber qual é o último
    L = L[-1] - 1 # pego a última posição e subtraio um( de acordo com a formula )
    for k in sorted(aux):
        Pr = (aux[k]/qtdPixels) # calcula a probabilidade
        frequencia += Pr #frequência acumulada
        EQ += L * Pr # calcula o EQ e vai acumulando
        tabela[k] = [k, aux[k], Pr, frequencia, EQ, round(EQ)] # monta toda a tabela, naqual a chave do dicionário é o nível de cinza da matriz original

    return tabela


imagem = Image.open("paisagem.jpg")
imagem = imagem.convert('L')
matriz = np.asanyarray(imagem)
imagem.show()
altura = np.size(matriz, 0)
largura = np.size(matriz, 1)
qtdPixels = altura*largura

tabela = equali_histograma(matriz, qtdPixels)  # printa o histograma e já retorna a tabela LUT
newTable = {} # vai guardar o valor antigo e o novo


for i in sorted(tabela): #retorna só as keys
    newTable[i] = tabela[i][5] # a newTable vai ter como chave o valor do nível de cinza da imagem original(que é inserido de forma ordenada) e como valor o novo valor da respectiva célula

# show_matriz(matriz)


matrizFinal = [] #vai guardar os resultados finais
aux = []

#substituição
for i in matriz:
    for j in i:
        aux.append(newTable[j]) #vai pegar o valor de j(valor da matriz orginal), vai buscar no dicionário (newTable) e vai colocar na sua posição seu novo valor
    matrizFinal.append(aux.copy())#adiciona a linha aux
    aux.clear() # limpa aux para repetir o processo na segunda linha


# print(matrizFinal)
#faz-se o processo inverso e mostra a imagem
matrizFinal = np.asanyarray(matrizFinal)
imagemFinal = Image.fromarray(matrizFinal)
imagemFinal.show()
# show_matriz(matrizFinal)