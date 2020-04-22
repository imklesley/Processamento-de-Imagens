from PIL import Image
import numpy as np

#####printa matriz
def showMatriz(matriz):
    print("\n\n")
    for i in matriz:  # mostra matriz
        for j in i:
            print(j, end=' ')
        print('')

aux = []

# abre imagem
nome = 'seta'
img = Image.open(nome+'.jpg')


matriz = np.asanyarray(img.convert('L'))  # converte imagem em matriz
showMatriz(matriz)
# img.show()

# altura e largura
lin = np.size(matriz, 0)
col = np.size(matriz, 1)
# altura e largura

# # Vizinho Mais Próximo

# # Criamos uma matriz auxiliar para tratarmos das alterações na imagem sem perda de informaões (BACKUP)
m2 = []
aux = []
for i in range(lin):
    for j in range(col):
        aux.append(matriz[i][j])
    m2.append(aux.copy())
    aux.clear()
############


################ Ampliação #################
# cria-se uma nova matriz com as dimensões necessárias para suportar o resultado do algoritmo
m2Vizinho = []
for i in range(lin*2):
    for j in range(col*2):
        aux.append(0)
    m2Vizinho.append(aux.copy())
    aux.clear()

#Preenchimento da nova matriz pelo algorítmo
#Ampliação

i = -2
j = 0
for a1 in m2:
    i += 2
    j = 0
    for a2 in a1:
        while i < lin*2:
            while j < col*2:
                m2Vizinho[i][j] = a2
                m2Vizinho[i][j+1] = a2
                m2Vizinho[i+1][j] = a2
                m2Vizinho[i+1][j+1] = a2
                j += 2
                break
            break


imgFinal = np.asanyarray(m2Vizinho)  # Tranforma a matriz m2 no tipo array Numpy
imgAmp = Image.fromarray(imgFinal)  # Transforma array Numpy em formato de Imagem
imgAmp.save(nome+'AmpliadoVizinho.jpg')
imgAmp.show()# mostra resultado
################ Ampliação #################

################ Redução #################
# Criamos uma matriz auxiliar para tratarmos das alterações na imagem sem perda de informaões (BACKUP)
m2 = []
aux = []
for i in range(lin):
    for j in range(col):
        aux.append(matriz[i][j])
    m2.append(aux.copy())
    aux.clear()

# cria-se uma nova matriz com as dimensões necessárias para suportar o resultado do algoritmo
m2Vizinho = []

# showMatriz(m2Vizinho)
k = l = -1;
aux = []
flag = 0
for i in m2: # i == k(linha)  e j ==l(coluna)
    k += 1 #forçar iniciar com zero e manter a contagem
    for j in i:
        l += 1  #forçar iniciar com zero e manter a contagem
        if k % 2 == 0: # se a linha for par
            if flag == 0: # pega o valor de uma coluna sim e outra não até o fim da linha
                aux.append(j)
                flag = 1
            else: #apenas pula a coluna e permite que um valor possa ser add novamente
                flag = 0
        else: # caso a linha seja impar, damos um break e a ignoramos... mas antes salvamos os resultados da linha anterior na matriz m2Vizinho
            m2Vizinho.append(aux.copy())
            aux.clear()
            l = 0
            break




imgFinal = np.asanyarray(m2Vizinho)  # Tranforma a matriz m2 no tipo array Numpy
# showMatriz(imgFinal)
imgRedu = Image.fromarray(imgFinal)  # Transforma array Numpy em formato de Imagem
imgRedu.save(nome+'ReduzidoVizinho.jpg')
imgRedu.show()# mostra resultado

################ Redução #################

######Interpolação Bilinear #######

################ Ampliação #################
# cria-se uma nova matriz com as dimensões necessárias para suportar o resultado do algoritmo
m2Vizinho = []
for i in range(lin*2):
    for j in range(col*2):
        aux.append(-1)
    m2Vizinho.append(aux.copy())
    aux.clear()
# Coloca os valores da matriz original na sua posição ideal de acordo com o algoritmo
i = -2
j = 0
for a1 in m2:
    i += 2
    j = 0
    for a2 in a1:
        while i < lin*2:
            while j < col*2:
                m2Vizinho[i][j] = a2
                j += 2
                break
            break
# Coloca os valores da matriz original na sua posição ideal de acordo com o algoritmo

flagAE = 0 # 0 pra dizer que é pra fazer a linha que tem os 'a' e 1 para as que tem 'e'
flagBCD = 0 #
for i in range(len(m2Vizinho)):
    for j in range(len(m2Vizinho[0])):
        try:
            if i%2 == 0:
                if flagAE == 0:
                    if m2Vizinho[i][j] == -1:
                        a = m2Vizinho[i][j-1]
                        b = m2Vizinho[i][j+1]
                        c = (a+b)//2
                        print(c)
                        m2Vizinho[i][j] = c # A
                    if m2Vizinho[i][j] == m2Vizinho[i][19]:
                        flagAE = 1
                else:
                    m2Vizinho[i][j] = (m2Vizinho[i][j-1]+m2Vizinho[i][j+1])//2 # E

            else: # se for linha impar
                if flagBCD == 0: # 0 calculo do B, 1 do C e 2 do D
                    m2Vizinho[i][j] = (m2Vizinho[i-1][j]+m2Vizinho[i+1][j])//2 # B
                    flagBCD = 1
                elif flagBCD == 1:
                    m2Vizinho[i][j] = (m2Vizinho[i-1][j-1]+m2Vizinho[i+1][j-1]+m2Vizinho[i-1][j+1]+m2Vizinho[i+1][j+1])//4 #C
                    flagBCD = 2
                else:
                    m2Vizinho[i][j] = (m2Vizinho[i-1][j] +m2Vizinho[i+1][j]) // 2 # D
                    flagBCD = 0
                if m2Vizinho[i][j] == m2Vizinho[i][-1]:
                    flagAE = 0
        except:
            continue
showMatriz(m2Vizinho)


# imgFinal = np.asanyarray(m2Vizinho)  # Tranforma a matriz m2 no tipo array Numpy
# imgAmp = Image.fromarray(imgFinal)  # Transforma array Numpy em formato de Imagem
# imgAmp.save(nome+'AmpliadoBilinear.jpg')
# imgAmp.show()# mostra resultado
################ Ampliação #################
