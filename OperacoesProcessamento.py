# NESSE ARQUIVO ESTÃO OPERAÇÕES QUE SÃO USADAS PARA PERCORRER E MODIFICAR UMA IMAGEM.

#Legenda:
# listaImagem => lista com todas as informações da imagem
# matrizPixels => matriz com todos os pixels da imagem
# listaMascara => lista com todas as informações da mascara
# mascaraPixels => matriz com todos os pixels da mascara

import Arquivos
import Operacoes

def media(imagem, altura, largura):
    enderecoMask = input("Digite o nome do arquivo com a máscara: ")
    listaMascara = Arquivos.lerMascara(enderecoMask)

    tamanho = listaMascara[0].split()
    larguraMask = int(tamanho[0])
    alturaMask = int(tamanho[1])

    mascaraPixel = Operacoes.conteudoMascara(listaMascara) # Pega os pixels da mascara

    peso = sum([sum(linha) for linha in mascaraPixel])

    a = int((alturaMask-1)/2)
    b = int((larguraMask-1)/2)

    novaMatriz = Operacoes.geraMatriz(largura, altura)

    for i in range(0,altura): # Percorre a Imagem
        for j in range(0,largura):
            if (i - a >= 0 and j - b >= 0 and i + a < altura and j + b < largura):   # Se a mascara cabe na imagem
                for s in range(-a,a+1):     # Percorre a Mascara
                    for t in range(-b,b+1):
                        novaMatriz[i - a][j - b] += mascaraPixel[a + s][b + t] * imagem[i + s][j + t]
                        
                novaMatriz[i - a][j - b] = round(novaMatriz[i - a][j - b]/peso)
    return novaMatriz

def mediana(matrizPixels, altura, largura, enderecoMask):
    print("Executando Mediana.")
    listaMascara = Arquivos.lerMascara(enderecoMask)

    tamanho = listaMascara[0].split()
    larguraMask = int(tamanho[0])
    alturaMask = int(tamanho[1])

    a = int((alturaMask-1)/2)    # Ponto central da mascara => (b,a) => (x,y) do Centro
    b = int((larguraMask-1)/2)

    novaMatriz = Operacoes.geraMatriz(largura, altura)
    listaMediana = []
    for i in range(0,altura): # Percorre a Imagem
        for j in range(0,largura):
            if (i - a >= 0 and j - b >= 0 and i + a < altura and j + b < largura):   # Se a mascara cabe na imagem
                for s in range(-a,a+1):     # Percorre a Mascara
                    for t in range(-b,b+1):
                        listaMediana.append(int(matrizPixels[i + s][j + t]))
                listaMediana.sort()
                novaMatriz[i - a][j - b] = listaMediana[round(len(listaMediana)/2)]
                listaMediana = []
    print("Mediana concluída.")
    return novaMatriz

def dilatacao(matrizPixels, altura, largura, enderecoMask):
    print("Executando Dilatação.")
    listaMascara = Arquivos.lerMascara(enderecoMask)

    tamanho = listaMascara[0].split()
    larguraMask = int(tamanho[0])
    alturaMask = int(tamanho[1])

    mascaraPixel = Operacoes.conteudoMascara(listaMascara) # Pega os pixels da mascara
    mascaraPixel = Operacoes.reflexao(mascaraPixel, larguraMask, alturaMask) # Reflete a mascara

    a = int((alturaMask-1)/2)  # Ponto central da mascara => (b,a) => (x,y) do Centro
    b = int((larguraMask-1)/2)

    novaMatriz = Operacoes.geraMatriz(largura, altura)
    toques = 0
    for i in range(0,altura):   # Percorre a Imagem
        for j in range(0,largura):
            if (i - a >= 0 and j - b >= 0 and i + a < altura and j + b < largura):  # Se a mascara cabe na imagem  
                for s in range(-a,a+1):   # Percorre a Mascara
                    for t in range(-b,b+1):
                        if mascaraPixel[a + s][b + t] + matrizPixels[i + s][j + t] == 2: # Se na posicao atual da mascara e imagem os pixels são 1
                            toques += 1
                if toques >= 1:
                    novaMatriz[i - a][j - b] = 1        # Marque um ponto preto
                toques = 0      # Resete o toque
    print("Dilatação concluída.")
    return novaMatriz

def erosao(matrizPixels, altura, largura, enderecoMask):
    print("Executando Erosão.")
    listaMascara = Arquivos.lerMascara(enderecoMask)

    tamanho = listaMascara[0].split()
    larguraMask = int(tamanho[0])
    alturaMask = int(tamanho[1])

    mascaraPixel = Operacoes.conteudoMascara(listaMascara) # Pega os pixels da mascara
    peso = sum([sum(linha) for linha in mascaraPixel])     # Soma todos os pixels da mascara

    a = int((alturaMask-1)/2)     # Ponto central da mascara => (b,a) => (x,y) do Centro
    b = int((larguraMask-1)/2)

    novaMatriz = Operacoes.geraMatriz(largura, altura)
    toques = 0
    for i in range(0,altura):       # Percorre a Imagem
        for j in range(0,largura):
            if (i - a >= 0 and j - b >= 0 and i + a < altura and j + b < largura):  # Se a mascara cabe na imagem 
                for s in range(-a,a+1):        # Percorre a Mascara
                    for t in range(-b,b+1):
                        if mascaraPixel[a + s][b + t] + matrizPixels[i + s][j + t] == 2: # Se na posicao atual da mascara e imagem os pixels são 1
                            toques += 1
                if toques == peso:
                    novaMatriz[i - a][j - b] = 1 # Marque um ponto preto
                toques = 0 # Resete o toque
    print("Erosão concluída.")
    return novaMatriz

def abertura(matrizPixels, altura, largura, enderecoMask):
    novaMatriz1 = erosao(matrizPixels, altura, largura, enderecoMask)
    novaMatriz2 = dilatacao(novaMatriz1, altura, largura, enderecoMask)
    return novaMatriz2

def fechamento(matrizPixels, altura, largura, enderecoMask):
    novaMatriz1 = dilatacao(matrizPixels, altura, largura, enderecoMask)
    novaMatriz2 = erosao(novaMatriz1, altura, largura, enderecoMask)
    return novaMatriz2

def contaColunas(matrizPixels, largura):
    print("Contando Colunas.")
    numeroColunas = 0
    leitor = [0 for x in range(75)]
    b = 37   # Posição do meio do leitor
    listaPontosColunas = []  # Guarda os xs dos pontos dentro de cada coluna
    pesoAnterior = 0
    for j in range(0,largura):
        if (j + b < largura):  # Se o leitor cabe na imagem
            leitor = [x for x in matrizPixels[214][j:j+75]]
            pesoAtual = sum(leitor)     # Soma todos os pixels do leitor
            if pesoAnterior > pesoAtual and pesoAtual == 0:  # Se antes tinha pixels pretos no leitor e agora não tem mais significa que ele acabou de ler uma coluna
                numeroColunas += 1
                # listaPontosColunas.append(j-3) # Ponto onde o leitor toca no ultimo pixel preto da coluna => j-1
            elif pesoAtual > 0 and pesoAnterior == 0:
                listaPontosColunas.append(j + 76)  # Ponto onde o leitor toca no primeiro pixel preto da coluna => j + 74
            pesoAnterior = pesoAtual
    return (numeroColunas, listaPontosColunas)

def contaLinhas(matrizPixels, altura, listaPontosColunas):
    print("Contando Linhas.")
    leitor = [0 for x in range(10)]
    listaQuantidadeLinhas = []  # Guarda quantas linhas cada coluna possui
    listaPontosLinhas = []  # Guarda os ys dos pontos dentro de cada linha
    listaLinhasExtras = [] # Guarda a quantidade de linhas extras de cada coluna. Vai ser usado pelo conta palavras
    for j in range(0, len(listaPontosColunas)):
        numeroLinhas = 0
        linhasExtras = 0
        pesoAnterior = 0
        filaDeEstadosDoLeitor = "" # Guarda os estados 0 para o leitor vazio e 1 para não vazio
        for i in range(189,altura):     # Começa do 189 pra pular o espaço em branco antes da primeira linha do texto
            if (i + 10 < altura):  # Se o leitor cabe na imagem
                leitor = []
                for a in range(i, i+10):
                    leitor.append(matrizPixels[a][listaPontosColunas[j]])
                pesoAtual = sum(leitor)     # Soma todos os pixels do leitor
                if pesoAnterior > pesoAtual and pesoAtual == 0:  # Se antes tinha pixels pretos no leitor e agora não tem mais significa que ele acabou de ler uma linha
                    numeroLinhas += 1
                    listaPontosLinhas.append(i-1)
                elif pesoAtual > 0 and pesoAnterior == 0:
                    listaPontosLinhas.append(i + 9)
                pesoAnterior = pesoAtual
                if (i+1)%10==0:
                    if pesoAtual > 0:
                        filaDeEstadosDoLeitor += "1"
                    elif pesoAtual == 0:
                        filaDeEstadosDoLeitor += "0"
                    if "000000" in filaDeEstadosDoLeitor:
                        break
                    elif len(filaDeEstadosDoLeitor) >= 5 and j < (len(listaPontosColunas)-1) and "00001" == filaDeEstadosDoLeitor[len(filaDeEstadosDoLeitor) - 5 :: ]:    #Se encontrou um final de paragrafo (linha em branco) verifique se existe uma linha em outra coluna
                        
                        for coluna in range(0, len(listaPontosColunas)):
                            
                            if coluna != j: # Não verifica na coluna atual
                                leitor = []
                                for b in range(i-40, i-10): # Verifique outra coluna na posição onde há o espaço vazio => "0X000Y1" De X até Y
                                    leitor.append(matrizPixels[b][listaPontosColunas[coluna]])
                                pesoAtual = sum(leitor)     # Soma todos os pixels do leitor
                                
                                if pesoAtual > 0:
                                    linhasExtras += 1
                                    break

        
        listaLinhasExtras.append(linhasExtras)
        numeroLinhas += linhasExtras
        
        listaQuantidadeLinhas.append(numeroLinhas)
    numeroLinhas = max(listaQuantidadeLinhas)  # Como algumas colunas possuem mais linhas que outras, numeroLinhas final é o maior número de linhas encontrado numa coluna
            
    return (numeroLinhas, listaPontosLinhas, listaQuantidadeLinhas, listaLinhasExtras)

def contaColunasELinhas(matrizPixels, altura, largura):
    numeroColunas, listaPontosColunas = contaColunas(matrizPixels, largura)
    numeroLinhas, listaPontosLinhas, listaQuantidadeLinhas, listaLinhasExtras = contaLinhas(matrizPixels, altura, listaPontosColunas)
    return (numeroColunas, numeroLinhas, listaPontosLinhas, listaPontosColunas, listaQuantidadeLinhas, listaLinhasExtras)

def encontraPosicaoCentralLinha(listaPontosLinhas):
    listaHorizontal = []
    for i in range(0, len(listaPontosLinhas), 2):
        listaHorizontal.append(listaPontosLinhas[i] + int((listaPontosLinhas[i+1]-listaPontosLinhas[i])/2))
    return listaHorizontal  # Retorna uma lista com a posição central das linhas

def contaPalavras(matrizPixels, altura, largura, listaPontosLinhas, listaPontosColunas, listaQuantidadeLinhas, listaLinhasExtras):
    print("Contando Palavras.")
    numeroPalavras = 0
    listaDeX = []  # Guarda os valores de x para circular a palavra
    listaDeY = []  # Guarda os valores de y para circular a palavra
    matrizLeitor = Operacoes.geraMatriz(5, 35)
    listaCentroLinhas = encontraPosicaoCentralLinha(listaPontosLinhas)
    a = 17  # Meio da altura do leitor
    b = 2   # Meio da largura do leitor
    quantidadeDeLinhasNaColuna = []
    for w in range (0, len(listaQuantidadeLinhas)):
        quantidadeDeLinhasNaColuna.append(listaQuantidadeLinhas[w] - listaLinhasExtras[w])  #Pega apenas a quantidade de linhas de uma coluna e bota como elemento da lista
    
    listaDePontosIniciaisDaColuna = []
    for c in listaPontosColunas:
        listaDePontosIniciaisDaColuna.append(c - 5) #Ponto onde começa a coluna 5 pixels recuado
    listaDePontosIniciaisDaColuna.append(largura)   # final da imagem é o final da ultima coluna

    pesoAnterior = 0
    x0 = 0  # x inicial da palavra
    x1 = 0  # x final da palavra
    y0 = 0  # y inicial da palavra
    y1 = 0  # y final da palavra
    indiceDaColuna = 1
    for lin in quantidadeDeLinhasNaColuna:  # lin => quantas linhas aquela coluna tem

        ultimaLinhaDaColuna = lin
        inicioDaColuna = listaDePontosIniciaisDaColuna[indiceDaColuna-1]
        finalDaColuna = listaDePontosIniciaisDaColuna[indiceDaColuna]

        for i in range(0, ultimaLinhaDaColuna): # Percorra todas as linhas da coluna
            
            for j in range(inicioDaColuna,finalDaColuna):   #  Percorra a largura da coluna
                if (listaCentroLinhas[i] - a >= 0 and j - b >= 0 and listaCentroLinhas[i] + a < altura and j + b < finalDaColuna):   # Se a matrizLeitor cabe na imagem
                    for s in range(-a,a+1):     # Percorre a matrizLeitor
                        for t in range(-b,b+1):
                            matrizLeitor[a + s][b + t] = matrizPixels[listaCentroLinhas[i] + s][j + t]  # matrizLeitor recebe os valores da imagem onde ela está em cima
                    
                    pesoAtual = sum([sum(linha) for linha in matrizLeitor])     # Soma todos os pixels do leitor

                    if pesoAtual != 0:  #Se o leitor esta em uma palavra
                        for linhaMatrizLeitor in range(0, a):   # Vai do topo da matriz até proximo da metade
                            if 1 in matrizLeitor[linhaMatrizLeitor]:    #   se existe um 1 no topo da matriz salve no y0
                                y0 = listaCentroLinhas[i] - a
                                break
                        for linhaMatrizLeitor in range(34, a,-1):         # Vai do fim da matriz até proximo da metade   
                            if 1 in matrizLeitor[linhaMatrizLeitor]:    #   se existe um 1 no final da matriz salve no y1
                                y1 =  listaCentroLinhas[i] + a
                                break
                            
                    if pesoAnterior > pesoAtual and pesoAtual == 0:  # Se antes tinha pixels pretos no leitor e agora não tem mais significa que ele acabou de ler uma palavra
                        numeroPalavras += 1
                        x1 = j - 2
                        listaDeX.append((x0,x1))
                        listaDeY.append((y0,y1))
                    elif pesoAtual > 0 and pesoAnterior == 0:   #Encontrou o inicio de uma palavra
                        x0 = j + 2
                    pesoAnterior = pesoAtual
        listaCentroLinhas = listaCentroLinhas[lin::]    # Joga fora os pontos centrais das linhas que já foram lidas e fica com os pontos das próximas colunas
        indiceDaColuna += 1
        
    return (numeroPalavras, listaDeX, listaDeY)
    
def circularPalavras(matrizPixels, listaDeX, listaDeY):
    print("Circulando Palavras.")
    novaMatriz = matrizPixels[0::]
    for i in range(0, len(listaDeX)):   # Pega o conjunto com os 4 pontos para circular a palavra
        x0 = listaDeX[i][0]
        x1 = listaDeX[i][1]
        y0 = listaDeY[i][0]
        y1 = listaDeY[i][1]
        for j in range(x0, x1+1):   # Traça a linha na horizontal
            novaMatriz[y0][j] = 1
            novaMatriz[y1][j] = 1
        for a in range(y0, y1+1):   # Traça a linha na Vertical
            novaMatriz[a][x0] = 1
            novaMatriz[a][x1] = 1
    return novaMatriz